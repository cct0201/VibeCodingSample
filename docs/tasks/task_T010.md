# Task ID: T010
# Title: Write basic tests
# Status: TO-DO
# Dependencies: T001, T004
# Priority: Low
# Description: Create unit tests for the backend API
# Estimated time: M

# Details:
Develop a test suite for the Flask application focusing on the API functionality:
1. Create a test directory at the project root
2. Set up a test file for the API (test_api.py)
3. Implement the following tests:
   - Test that the root route returns status 200
   - Test that the /get-articles endpoint returns a JSON response
   - Test that the /get-articles endpoint returns exactly 3 articles when more are available
   - Test that the /get-articles endpoint handles the case with fewer than 3 articles
   - Test that the /get-articles endpoint never returns duplicate URLs
   - Test that error handling works correctly
4. Mock the article list to ensure consistent testing
5. Add fixtures and setup/teardown methods as needed
6. Include comments explaining the purpose of each test

Optional enhancements:
- Add test coverage reporting
- Include integration tests for frontend-backend interaction
- Add performance tests for response times

# Acceptance Criteria:
- Test suite exists and runs without errors
- Tests cover all critical functionality of the API
- Tests verify the business logic requirements
- All edge cases are covered (e.g., fewer than 3 articles)
- Tests are well-organized and documented
- Tests can be run easily with a simple command

# Test Strategy:
- Run the test suite with `pytest` or similar framework
- Verify that tests pass consistently
- Introduce deliberate bugs to confirm tests can catch issues
- Check that test coverage includes all critical components
- Ensure tests are independent and can run in any order 