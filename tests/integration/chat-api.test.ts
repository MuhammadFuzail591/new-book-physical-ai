// Basic integration test for chat API service
import { chatAPI } from '../../src/services/api/chatbot-api';
import { SendMessageRequest, StartSessionRequest } from '../../src/services/types/chat-types';

// Mock fetch globally for testing
global.fetch = jest.fn();

describe('Chat API Service', () => {
  beforeEach(() => {
    (global.fetch as jest.MockedFunction<typeof global.fetch>).mockClear();
  });

  it('should send a message successfully', async () => {
    const mockResponse = {
      id: 'msg-1',
      message: 'Hello, I am the bot response',
      sessionId: 'session-1',
      timestamp: '2023-01-01T00:00:00Z',
      sender: 'bot'
    };

    (global.fetch as jest.MockedFunction<typeof global.fetch>).mockResolvedValueOnce({
      ok: true,
      json: async () => mockResponse,
    } as Response);

    const request: SendMessageRequest = {
      message: 'Hello, bot!',
      sessionId: 'session-1'
    };

    const result = await chatAPI.sendMessage(request);

    expect(result).toEqual(mockResponse);
    expect(global.fetch).toHaveBeenCalledWith(
      expect.stringContaining('/chat/send'),
      expect.objectContaining({
        method: 'POST',
        headers: expect.objectContaining({
          'Content-Type': 'application/json',
        }),
      })
    );
  });

  it('should start a new session successfully', async () => {
    const mockResponse = {
      sessionId: 'session-1',
      createdAt: '2023-01-01T00:00:00Z',
      bookId: 'book-1'
    };

    (global.fetch as jest.MockedFunction<typeof global.fetch>).mockResolvedValueOnce({
      ok: true,
      json: async () => mockResponse,
    } as Response);

    const request: StartSessionRequest = {
      bookId: 'book-1'
    };

    const result = await chatAPI.startSession(request);

    expect(result).toEqual(mockResponse);
    expect(global.fetch).toHaveBeenCalledWith(
      expect.stringContaining('/chat/session'),
      expect.objectContaining({
        method: 'POST',
      })
    );
  });
});