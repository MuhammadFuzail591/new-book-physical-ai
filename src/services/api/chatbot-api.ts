// API service for chatbot functionality
import {
  SendMessageRequest,
  SendMessageResponse,
  StartSessionRequest,
  StartSessionResponse,
  GetSessionHistoryResponse,
  ChatMessage
} from '../types/chat-types';
import { CHATBOT_CONFIG } from '../../config/chat-config';

// Configuration from chat config
const API_BASE_URL = CHATBOT_CONFIG.API_BASE_URL;
const WS_BASE_URL = CHATBOT_CONFIG.WS_BASE_URL;

export interface ChatAPI {
  sendMessage: (request: SendMessageRequest) => Promise<SendMessageResponse>;
  startSession: (request: StartSessionRequest) => Promise<StartSessionResponse>;
  getSessionHistory: (sessionId: string) => Promise<GetSessionHistoryResponse>;
}

class ChatAPIService implements ChatAPI {
  async sendMessage(request: SendMessageRequest): Promise<SendMessageResponse> {
    try {
      const response = await fetch(`${API_BASE_URL}/chat/send`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: request.message,
          sessionId: request.sessionId,
          bookId: request.bookId,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: SendMessageResponse = await response.json();
      return data;
    } catch (error) {
      console.error('Error sending message:', error);
      throw error;
    }
  }

  async startSession(request: StartSessionRequest): Promise<StartSessionResponse> {
    try {
      const response = await fetch(`${API_BASE_URL}/chat/session`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          bookId: request.bookId,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: StartSessionResponse = await response.json();
      return data;
    } catch (error) {
      console.error('Error starting session:', error);
      throw error;
    }
  }

  async getSessionHistory(sessionId: string): Promise<GetSessionHistoryResponse> {
    try {
      const response = await fetch(`${API_BASE_URL}/chat/session/${sessionId}/history`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: GetSessionHistoryResponse = await response.json();
      return data;
    } catch (error) {
      console.error('Error getting session history:', error);
      throw error;
    }
  }
}

// WebSocket service for real-time communication
export interface WebSocketService {
  connect: (sessionId: string, onMessage: (message: any) => void, onError?: (error: any) => void) => void;
  sendMessage: (message: any) => void;
  disconnect: () => void;
  isConnected: () => boolean;
}

export class WebSocketServiceImpl implements WebSocketService {
  private ws: WebSocket | null = null;
  private sessionId: string | null = null;

  connect(sessionId: string, onMessage: (message: any) => void, onError?: (error: any) => void) {
    this.disconnect(); // Ensure any existing connection is closed
    this.sessionId = sessionId;

    const wsUrl = `${WS_BASE_URL}/chat`;
    this.ws = new WebSocket(wsUrl);

    this.ws.onopen = () => {
      console.log('WebSocket connected');
      // Optionally send a message to join the session
      if (this.ws) {
        this.ws.send(JSON.stringify({ type: 'join_session', payload: { sessionId } }));
      }
    };

    this.ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        onMessage(data);
      } catch (error) {
        console.error('Error parsing WebSocket message:', error);
        if (onError) onError(error);
      }
    };

    this.ws.onerror = (error) => {
      console.error('WebSocket error:', error);
      if (onError) onError(error);
    };

    this.ws.onclose = () => {
      console.log('WebSocket disconnected');
      this.ws = null;
      this.sessionId = null;
    };
  }

  sendMessage(message: any) {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(message));
    } else {
      console.error('WebSocket is not connected');
      throw new Error('WebSocket is not connected');
    }
  }

  disconnect() {
    if (this.ws) {
      this.ws.close();
      this.ws = null;
      this.sessionId = null;
    }
  }

  isConnected(): boolean {
    return this.ws !== null && this.ws.readyState === WebSocket.OPEN;
  }
}

// Singleton instances
const chatAPI = new ChatAPIService();
const webSocketService = new WebSocketServiceImpl();

export { chatAPI, webSocketService };