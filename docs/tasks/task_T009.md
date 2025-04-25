# Task ID: T009
# Title: Style the frontend
# Status: TO-DO
# Dependencies: T005
# Priority: Low
# Description: Add CSS styling for better user experience
# Estimated time: M

# Details:
Enhance the frontend appearance by adding CSS styling:
1. Create a style section in the head of index.html or a separate CSS file in the static directory
2. Implement styling for the main container:
   - Set maximum width and center on page
   - Add padding and margin for spacing
   - Use a clean, readable font family
3. Style the heading:
   - Choose an appropriate color that stands out
   - Set font weight and size
   - Add margin for spacing
4. Style the button:
   - Add background color, text color, padding
   - Include hover and active states
   - Add transition effects for smooth interactions
   - Style disabled state for when API is loading
5. Style the article list:
   - Format list items with padding and margin
   - Add subtle borders or background colors
   - Style links with appropriate colors and hover effects
6. Style the loading indicator:
   - Create a visually appealing loading state
   - Position it appropriately on the page
7. Style the error container:
   - Use appropriate colors for error messages (red/orange)
   - Make it visually distinct
8. Ensure responsive design:
   - Use relative units (em, rem, %) for sizing
   - Add media queries for different screen sizes
   - Test on mobile and desktop viewports

# Acceptance Criteria:
- Clean, professional visual design
- Responsive layout that works on mobile and desktop
- Interactive elements have appropriate hover/active states
- Button has clear enabled/disabled visual states
- Article links are easily readable and clickable
- Loading indicator is visually clear
- Error messages stand out visually
- Design follows modern web design principles
- CSS is well-organized and commented

# Test Strategy:
- Test on multiple screen sizes and browsers
- Verify all states (loading, error, success) have appropriate styling
- Check accessibility (contrast ratios, text size)
- Validate CSS
- Test with different content lengths to ensure layout remains stable 