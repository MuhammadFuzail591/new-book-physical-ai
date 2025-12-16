// Basic unit test for MessageBubble component
import React from 'react';
import { render, screen } from '@testing-library/react';
import MessageBubble from '../../../src/components/ChatInterface/MessageBubble';
import { ChatMessage } from '../../../src/services/types/chat-types';

// Mock the CSS module
jest.mock('../../../src/styles/chat.css', () => ({}));

describe('MessageBubble', () => {
  const mockMessage: ChatMessage = {
    id: '1',
    content: 'Hello, this is a test message',
    sender: 'user',
    timestamp: new Date(),
    status: 'delivered',
    chatSessionId: 'session-1'
  };

  it('renders user message correctly', () => {
    render(<MessageBubble message={mockMessage} />);

    expect(screen.getByText('Hello, this is a test message')).toBeInTheDocument();
    expect(screen.getByText('You')).toBeInTheDocument(); // Should show "You" for user messages
  });

  it('renders bot message correctly', () => {
    const botMessage: ChatMessage = {
      ...mockMessage,
      sender: 'bot'
    };

    render(<MessageBubble message={botMessage} />);

    expect(screen.getByText('Hello, this is a test message')).toBeInTheDocument();
    expect(screen.getByText('BookBot')).toBeInTheDocument(); // Should show "BookBot" for bot messages
  });

  it('shows correct status indicator', () => {
    const errorMessage: ChatMessage = {
      ...mockMessage,
      status: 'error'
    };

    render(<MessageBubble message={errorMessage} />);

    expect(screen.getByText('❌')).toBeInTheDocument(); // Should show error indicator
  });
});