# Task ID: T006
# Title: Implement JavaScript functionality
# Status: TO-DO
# Dependencies: T005
# Priority: Medium
# Description: Add frontend JS to handle button clicks and API calls
# Estimated time: M

# Details:
Implement the JavaScript functionality for the frontend:
1. Add a script section at the bottom of index.html or in a separate .js file
2. Set up an event listener for DOMContentLoaded to ensure DOM is fully loaded
3. Get references to the button, article list, error container, and loading indicator elements
4. Add a click event listener to the button that:
   - Clears any existing articles in the list
   - Hides any error messages
   - Shows the loading indicator
   - Disables the button to prevent multiple clicks
5. Implement fetch() call to the '/get-articles' endpoint
6. Handle the API response:
   - Check if response is successful (response.ok)
   - Parse the JSON response
   - Hide the loading indicator
   - Re-enable the button
7. Process the articles data:
   - Handle case where data.error exists (show error)
   - Handle case where articles array is empty (show "no articles" message)
   - For each article URL, create a list item with a link and add to the article list
8. Implement error handling:
   - Catch any fetch errors
   - Display appropriate error messages
   - Log detailed errors to the console
   - Ensure the UI always returns to a usable state

# Acceptance Criteria:
- JavaScript runs without errors on page load
- Click event on button triggers API call
- Loading indicator shows during API call
- Button is disabled during API call
- Article list is properly populated with clickable links
- Links open in new tabs (target="_blank")
- Error messages are displayed when API errors occur
- UI properly resets after API call (loading hidden, button re-enabled)
- Code is well-structured and follows JavaScript best practices

# Test Strategy:
- Test button click to verify API call is made
- Test with network throttling to ensure loading state works
- Test with different API responses (success with articles, empty articles, error)
- Check browser console for any JavaScript errors
- Verify behavior in multiple browsers (Chrome, Firefox, Safari)
- Test responsive behavior on different screen sizes 