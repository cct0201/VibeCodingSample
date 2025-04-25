# Task ID: T004
# Title: Implement get-articles endpoint
# Status: TO-DO
# Dependencies: T001, T002
# Priority: High
# Description: Create API endpoint to return random unique article URLs
# Estimated time: M

# Details:
Implement the '/get-articles' API endpoint that returns random article URLs:
1. Define a route handler for '/get-articles' path using the @app.route decorator
2. Inside the handler function:
   - Use random.sample() to select 3 random, non-duplicate URLs from the article list
   - If the article list contains fewer than 3 items, return all available items
   - Return the selected URLs as a JSON response with jsonify()
   - Add proper type annotation (-> Tuple[Dict[str, Union[List[str], str]], int])
   - Implement error handling with try-except blocks
   - On success, return HTTP status 200
   - On error, return appropriate error message and HTTP status 500
3. Add detailed docstring explaining the function's purpose and return format
4. Ensure the function follows the business logic specified in the business_logic.mdc rule

# Acceptance Criteria:
- Endpoint correctly defined with @app.route('/get-articles')
- Returns exactly 3 unique URLs when article source list has ≥3 items
- Returns all available URLs when article source list has <3 items
- Uses random.sample() to ensure uniqueness and randomness
- Returns JSON in format {"success": true, "articles": ["url1", "url2", "url3"]}
- Implements proper error handling with try-except blocks
- On error, returns {"success": false, "error": "<error message>"}
- Function has proper type annotations and detailed docstring

# Test Strategy:
- Test with full article list: verify 3 unique URLs are returned
- Test by temporarily modifying article list to have <3 items
- Test by calling endpoint multiple times to verify different selections are returned
- Test error handling by temporarily introducing errors
- Verify JSON response format and HTTP status codes
- Check implementation against business logic requirements 