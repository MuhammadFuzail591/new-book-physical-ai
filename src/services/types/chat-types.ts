// Types for the chatbot frontend

export type MessageSender = 'user' | 'bot';

export interface ChatMessage {
  id: string;
  content: string;
  sender: MessageSender;
  timestamp: Date;
  status: 'sent' | 'delivered' | 'error';
  chatSessionId: string;
}

export interface ChatSession {
  id: string;
  messages: ChatMessage[];
  createdAt: Date;
  updatedAt: Date;
  isActive: boolean;
}

export interface ChatConfig {
  apiEndpoint: string;
  websocketEndpoint: string;
  maxMessageLength: number;
  timeoutMs: number;
}

export interface SendMessageRequest {
  message: string;
  sessionId?: string;
  bookId?: string;
}

export interface SendMessageResponse {
  id: string;
  message: string;
  sessionId: string;
  timestamp: string; // ISO string format from API
  sender: 'bot';
}

export interface StartSessionRequest {
  bookId?: string;
}

export interface StartSessionResponse {
  sessionId: string;
  createdAt: string; // ISO string format from API
  bookId?: string;
}

export interface GetSessionHistoryResponse {
  sessionId: string;
  messages: Omit<ChatMessage, 'timestamp'> & { timestamp: string }[]; // API returns timestamp as string
}