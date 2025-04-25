# Feature: AI Article Website

## Objective
Allow users to receive 3 random links to curated articles about AI Vibe Coding after pressing a button.

## User Stories
- As a user, I want to visit the page and press a button to obtain 3 article links.
- As an engineer, I want the backend to provide different results each time.

## Requirements
- The `/get-articles` endpoint returns 3 random and non-duplicate article URLs.
- If there are fewer than 3, return all available ones.
- No login required.
- Must work properly on both desktop and mobile devices.

## Constraints
- This version does not use a database.
- Keep dependencies minimal and simple (e.g., only using Flask).
- The client should not reload the page during interaction.

## System Design (Optional if already merged)
See `plan.md` for detailed technical specifics.
