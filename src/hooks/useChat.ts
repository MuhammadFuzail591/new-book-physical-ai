// Custom hook for chat functionality
import { useState, useEffect, useCallback, useRef } from 'react';
import { chatAPI, webSocketService } from '../services/api/chatbot-api';
import {
  ChatMessage,
  ChatSession,
  SendMessageRequest,
  StartSessionRequest,
  MessageSender
} from '../services/types/chat-types';

interface UseChatOptions {
  bookId?: string;
}

interface UseChatReturn {
  messages: ChatMessage[];
  sendMessage: (content: string) => Promise<void>;
  isLoading: boolean;
  error: string | null;
  sessionId: string | null;
  currentBookId: string | undefined;
  startNewSession: (bookId?: string) => Promise<void>;
  connectToSession: (sessionId: string, bookId?: string) => void;
  disconnectFromSession: () => void;
  isConnected: boolean;
}

export const useChat = ({ bookId: defaultBookId }: UseChatOptions = {}): UseChatReturn => {
  const [messages, setMessages] = useState<ChatMessage[]>(() => {
    // Try to load from localStorage if available
    if (typeof window !== 'undefined' && defaultBookId) {
      try {
        const savedMessages = localStorage.getItem(`chat_messages_${defaultBookId}`);
        if (savedMessages) {
          const parsed = JSON.parse(savedMessages);
          return parsed.map((msg: any) => ({
            ...msg,
            timestamp: new Date(msg.timestamp)
          }));
        }
      } catch (e) {
        console.warn('Could not load saved messages from localStorage', e);
      }
    }
    return [];
  });

  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [sessionId, setSessionId] = useState<string | null>(() => {
    // Try to load session ID from localStorage if available
    if (typeof window !== 'undefined' && defaultBookId) {
      try {
        return localStorage.getItem(`chat_sessionId_${defaultBookId}`) || null;
      } catch (e) {
        console.warn('Could not load session ID from localStorage', e);
        return null;
      }
    }
    return null;
  });
  const [isConnected, setIsConnected] = useState<boolean>(false);
  const [currentBookId, setCurrentBookId] = useState<string | undefined>(defaultBookId);

  const bookIdRef = useRef<string | undefined>(defaultBookId);

  // Update bookId ref when prop changes
  useEffect(() => {
    bookIdRef.current = defaultBookId;
    if (defaultBookId) {
      setCurrentBookId(defaultBookId);
    }
  }, [defaultBookId]);

  // Save messages to localStorage whenever they change
  useEffect(() => {
    if (typeof window !== 'undefined' && currentBookId) {
      try {
        // Only save recent messages (last 50) to avoid localStorage size limits
        const messagesToSave = messages.slice(-50).map(({ timestamp, ...rest }) => ({
          ...rest,
          timestamp: timestamp.toISOString()
        }));
        localStorage.setItem(`chat_messages_${currentBookId}`, JSON.stringify(messagesToSave));
      } catch (e) {
        console.warn('Could not save messages to localStorage', e);
      }
    }
  }, [messages, currentBookId]);

  // Save sessionId to localStorage whenever it changes
  useEffect(() => {
    if (typeof window !== 'undefined' && currentBookId) {
      try {
        if (sessionId) {
          localStorage.setItem(`chat_sessionId_${currentBookId}`, sessionId);
        } else {
          localStorage.removeItem(`chat_sessionId_${currentBookId}`);
        }
      } catch (e) {
        console.warn('Could not save session ID to localStorage', e);
      }
    }
  }, [sessionId, currentBookId]);

  // Handle WebSocket messages
  const handleMessage = useCallback((data: any) => {
    try {
      if (data.type === 'message' && data.payload) {
        const newMessage: ChatMessage = {
          id: data.payload.id || `msg-${Date.now()}`,
          content: data.payload.message,
          sender: data.payload.sender || 'bot',
          timestamp: new Date(data.payload.timestamp || Date.now()),
          status: 'delivered',
          chatSessionId: data.payload.sessionId || sessionId || '',
        };

        setMessages(prev => [...prev, newMessage]);
      } else if (data.type === 'session_update') {
        // Handle session-related updates if needed
        console.log('Session update received:', data.payload);
      }
    } catch (err) {
      console.error('Error handling WebSocket message:', err);
      setError('Error processing message from server');
    }
  }, [sessionId]);

  // Connect to WebSocket for session
  const connectToSession = useCallback(async (sessionId: string, bookId?: string) => {
    if (bookId) {
      bookIdRef.current = bookId;
    }

    try {
      // First, get the session history
      const historyResponse = await chatAPI.getSessionHistory(sessionId);

      // Convert the API response timestamps from strings to Date objects
      const historyMessages: ChatMessage[] = historyResponse.messages.map(msg => ({
        ...msg,
        timestamp: new Date(msg.timestamp),
        status: 'delivered' // History messages are already delivered
      }));

      // Set the initial messages from history
      setMessages(historyMessages);

      // Connect to WebSocket for real-time updates
      webSocketService.connect(sessionId, handleMessage, (err) => {
        console.error('WebSocket error:', err);
        setError('Connection error with chat service');
      });

      setIsConnected(true);
      setSessionId(sessionId);
    } catch (error) {
      console.error('Error fetching session history:', error);

      // Still connect to WebSocket even if history fetch fails
      webSocketService.connect(sessionId, handleMessage, (err) => {
        console.error('WebSocket error:', err);
        setError('Connection error with chat service');
      });

      setIsConnected(true);
      setSessionId(sessionId);

      setError('Could not load previous conversation history');
    }
  }, [handleMessage]);

  // Disconnect from WebSocket
  const disconnectFromSession = useCallback(() => {
    webSocketService.disconnect();
    setIsConnected(false);
    setSessionId(null);
  }, []);

  // Start a new session
  const startNewSession = useCallback(async (bookId?: string) => {
    try {
      setIsLoading(true);
      setError(null);

      const request: StartSessionRequest = {
        bookId: bookId || bookIdRef.current,
      };

      const response = await chatAPI.startSession(request);
      const newSessionId = response.sessionId;

      setSessionId(newSessionId);
      setMessages([]);

      // Connect to WebSocket for this session
      connectToSession(newSessionId, bookId || bookIdRef.current);
    } catch (err) {
      console.error('Error starting session:', err);
      setError(err instanceof Error ? err.message : 'Failed to start new session');
    } finally {
      setIsLoading(false);
    }
  }, [connectToSession]);

  // Send a message
  const sendMessage = useCallback(async (content: string) => {
    if (!content.trim() || isLoading) return;

    try {
      setIsLoading(true);
      setError(null);

      // Add user message to UI immediately
      const userMessage: ChatMessage = {
        id: `msg-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
        content,
        sender: 'user',
        timestamp: new Date(),
        status: 'sent',
        chatSessionId: sessionId || '',
      };

      setMessages(prev => [...prev, userMessage]);

      // Send to API
      const request: SendMessageRequest = {
        message: content,
        sessionId: sessionId || undefined,
        bookId: bookIdRef.current,
      };

      // If we have a WebSocket connection, use it for real-time messaging
      if (webSocketService.isConnected()) {
        // For now, we'll send via HTTP API and expect the WebSocket to receive the response
        // In a real implementation, you might send via WebSocket directly
        const response = await chatAPI.sendMessage(request);

        // The bot response will come via WebSocket, so we don't need to add it here
        // It will be handled by the handleMessage function
      } else {
        // Fallback to HTTP API only
        const response = await chatAPI.sendMessage(request);

        // Add bot response directly since no WebSocket
        const botMessage: ChatMessage = {
          id: response.id,
          content: response.message,
          sender: 'bot',
          timestamp: new Date(response.timestamp),
          status: 'delivered',
          chatSessionId: response.sessionId,
        };

        setMessages(prev => [...prev, botMessage]);
      }
    } catch (err) {
      console.error('Error sending message:', err);
      setError(err instanceof Error ? err.message : 'Failed to send message');

      // Update the user message status to error
      setMessages(prev => {
        const lastMessage = prev[prev.length - 1];
        if (lastMessage && lastMessage.sender === 'user' && lastMessage.status === 'sent') {
          return [
            ...prev.slice(0, -1),
            { ...lastMessage, status: 'error' }
          ];
        }
        return prev;
      });
    } finally {
      setIsLoading(false);
    }
  }, [sessionId, isLoading, bookIdRef]);

  // Clean up on unmount
  useEffect(() => {
    return () => {
      if (webSocketService.isConnected()) {
        webSocketService.disconnect();
      }
    };
  }, []);

  return {
    messages,
    sendMessage,
    isLoading,
    error,
    sessionId,
    currentBookId,
    startNewSession,
    connectToSession,
    disconnectFromSession,
    isConnected,
  };
};