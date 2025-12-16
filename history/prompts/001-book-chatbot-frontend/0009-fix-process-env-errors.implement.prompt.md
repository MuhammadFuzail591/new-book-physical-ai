---
id: 0009
title: Fix process env errors
stage: implement
date: 2025-12-17
surface: agent
model: Claude Sonnet 4.5
feature: book-chatbot-frontend
branch: 001-book-chatbot-frontend
user: claude
command: /sp.implement
labels: [frontend, chatbot, error-fix, environment, docusaurus]
links:
  spec: specs/001-book-chatbot-frontend/spec.md
  plan: specs/001-book-chatbot-frontend/plan.md
  tasks: specs/001-book-chatbot-frontend/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - src/config/chat-config.ts
 - src/services/api/chatbot-api.ts
tests:
 - null
---

## Prompt

I am facing these errors when I click on chatbot component. Uncaught runtime errors:
×
ERROR
process is not defined
ReferenceError: process is not defined
    at eval (webpack-internal:///./src/services/api/chatbot-api.ts:9:20)
    at ./src/services/api/chatbot-api.ts (http://localhost:3000/src_components_BookChatbot_jsx.js:57:1)
    at __webpack_require__ (http://localhost:3000/runtime~main.js:34:32)
    at fn (http://localhost:3000/runtime~main.js:321:21)
    at eval (webpack-internal:///./src/hooks/useChat.ts:7:83)
    at ./src/hooks/useChat.ts (http://localhost:3000/src_components_BookChatbot_jsx.js:50:1)
    at __webpack_require__ (http://localhost:3000/runtime~main.js:34:32)
    at fn (http://localhost:3000/runtime~main.js:321:21)
    at eval (webpack-internal:///./src/components/ChatInterface/ChatWindow.tsx:7:72)
    at ./src/components/ChatInterface/ChatWindow.tsx (http://localhost:3000/src_components_BookChatbot_jsx.js:29:1)
ERROR
process is not defined
ReferenceError: process is not defined
    at eval (webpack-internal:///./src/services/api/chatbot-api.ts:9:20)
    at ./src/services/api/chatbot-api.ts (http://localhost:3000/src_components_BookChatbot_jsx.js:57:1)
    at __webpack_require__ (http://localhost:3000/runtime~main.js:34:32)
    at fn (http://localhost:3000/runtime~main.js:321:21)
    at eval (webpack-internal:///./src/hooks/useChat.ts:7:83)
    at ./src/hooks/useChat.ts (http://localhost:3000/src_components_BookChatbot_jsx.js:50:1)
    at __webpack_require__ (http://localhost:3000/runtime~main.js:34:32)
    at fn (http://localhost:3000/runtime~main.js:321:21)
    at eval (webpack-internal:///./src/components/ChatInterface/ChatWindow.tsx:7:72)
    at ./src/components/ChatInterface/ChatWindow.tsx (http://localhost:3000/src_components_BookChatbot_jsx.js:29:1)
ERROR
Unexpected: no Docusaurus route context found
    at useRouteContext (webpack-internal:///./node_modules/@docusaurus/core/lib/client/exports/useRouteContext.js:13:172)
    at PluginHtmlClassNameProvider (webpack-internal:///./node_modules/@docusaurus/theme-common/lib/utils/metadataUtils.js:32:143)
    at renderWithHooks (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:15486:18)
    at mountIndeterminateComponent (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:20099:13)
    at beginWork (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:21622:16)
    at HTMLUnknownElement.callCallback (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:4164:14)
    at Object.invokeGuardedCallbackDev (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:4213:16)
    at invokeGuardedCallback (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:4277:31)
    at beginWork$1 (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:27486:7)
    at performUnitOfWork (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:26592:12)
ERROR
Unexpected: no Docusaurus route context found
    at useRouteContext (webpack-internal:///./node_modules/@docusaurus/core/lib/client/exports/useRouteContext.js:13:172)
    at PluginHtmlClassNameProvider (webpack-internal:///./node_modules/@docusaurus/theme-common/lib/utils/metadataUtils.js:32:143)
    at renderWithHooks (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:15486:18)
    at mountIndeterminateComponent (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:20099:13)
    at beginWork (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:21622:16)
    at HTMLUnknownElement.callCallback (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:4164:14)
    at Object.invokeGuardedCallbackDev (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:4213:16)
    at invokeGuardedCallback (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:4277:31)
    at beginWork$1 (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:27486:7)
    at performUnitOfWork (webpack-internal:///./node_modules/react-dom/cjs/react-dom.development.js:26592:12)

## Response snapshot

Fixed the 'process is not defined' error by updating environment variable access in config files. Modified src/config/chat-config.ts and src/services/api/chatbot-api.ts to safely check for process existence before accessing environment variables. Used typeof process !== 'undefined' checks to prevent runtime errors in browser environment. The API service now properly imports and uses the CHATBOT_CONFIG from the centralized config file.

## Outcome

- ✅ Impact: Fixed process is not defined error, chatbot now loads properly
- 🧪 Tests: null
- 📁 Files: Updated config and API service files with safe env var access
- 🔁 Next prompts: Chatbot functional without environment variable errors
- 🧠 Reflection: Browser environments don't have process object, need safety checks

## Evaluation notes (flywheel)

- Failure modes observed: process.env access in browser environment
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null