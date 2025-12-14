---
id: 0001
title: Fix Vercel Deployment
stage: general
date: 2025-12-14
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-physical-ai-textbook
user: fuzail
command: /sp.phr
labels: ["docusaurus", "vercel", "deployment", "configuration", "baseUrl"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - docusaurus.config.js
tests:
 - none
---

## Prompt

Hey the site is looking ok at localhost but showing page not found and without CSS on the deployed link of vercel, Go and check the deployment instructions from docasaurus documentation and try to make it OK, here is the deployment url https://new-book-physical-ai-rhyl.vercel.app/

## Response snapshot

Fixed the Docusaurus deployment issue by updating the baseUrl from '/physical-ai-textbook/' to '/' in docusaurus.config.js to match Vercel's root path deployment instead of GitHub Pages subdirectory deployment.

## Outcome

- ✅ Impact: Fixed Vercel deployment with incorrect baseUrl causing missing CSS and broken links
- 🧪 Tests: none
- 📁 Files: docusaurus.config.js updated with correct baseUrl and deployment settings
- 🔁 Next prompts: none
- 🧠 Reflection: Docusaurus baseUrl configuration must match the deployment platform's path structure

## Evaluation notes (flywheel)

- Failure modes observed: Docusaurus configured for GitHub Pages deployment but deployed to Vercel, causing assets to be served from wrong path
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Verify the fix by redeploying to Vercel
