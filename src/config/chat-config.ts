// Configuration for the chatbot API endpoints
// These can be overridden by environment variables

export const CHATBOT_CONFIG = {
  API_BASE_URL: (typeof process !== 'undefined' && process.env
    ? (process.env.REACT_APP_CHATBOT_API_URL || process.env.CHATBOT_API_URL)
    : undefined)
    || 'http://localhost:8000/api',
  WS_BASE_URL: (typeof process !== 'undefined' && process.env
    ? (process.env.REACT_APP_CHATBOT_WS_URL || process.env.CHATBOT_WS_URL)
    : undefined)
    || 'ws://localhost:8000/ws',
  MAX_MESSAGE_LENGTH: parseInt(
    (typeof process !== 'undefined' && process.env
      ? (process.env.REACT_APP_MAX_MESSAGE_LENGTH || '1000')
      : '1000'), 10),
  REQUEST_TIMEOUT_MS: parseInt(
    (typeof process !== 'undefined' && process.env
      ? (process.env.REACT_APP_REQUEST_TIMEOUT_MS || '30000')
      : '30000'), 10),
};

// Validate configuration
if (CHATBOT_CONFIG.MAX_MESSAGE_LENGTH <= 0) {
  console.warn('Invalid MAX_MESSAGE_LENGTH, using default value of 1000');
  CHATBOT_CONFIG.MAX_MESSAGE_LENGTH = 1000;
}

if (CHATBOT_CONFIG.REQUEST_TIMEOUT_MS <= 0) {
  console.warn('Invalid REQUEST_TIMEOUT_MS, using default value of 30000');
  CHATBOT_CONFIG.REQUEST_TIMEOUT_MS = 30000;
}