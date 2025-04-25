# Feature: AI Article Site

## Objective
Let users press a button and receive 3 random links to curated articles about AI Vibe Coding.

## User Stories
- As a user, I want to visit a page and press a button to get 3 article links.
- As an engineer, I want the backend to give different results each time.

## Requirements
- Endpoint `/get-articles` returns 3 random, non-repeating article URLs.
- If there are fewer than 3, return all.
- No login required.
- Should work on both desktop and mobile.

## Constraints
- No use of database in this version.
- Keep dependencies minimal and simple (e.g., Flask only).
- Client should not reload page on interaction.

## System Design (optional if merged)
See `plan.md` for detailed technical breakdown.
