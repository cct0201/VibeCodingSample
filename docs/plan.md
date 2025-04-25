## System Design

### Architecture Overview
- A lightweight Flask backend serving HTML and JSON endpoints
- Frontend: HTML template rendered server-side
- JavaScript handles AJAX call to `/get-articles`

### Interfaces
- `/`: Render index
- `/get-articles`: Return 3 random links

### Data Models
- No persistent model; article sources are hard-coded list

### Constraints
- Source list may be less than 3
- URLs must not repeat



# Core Logic (Act Mode Implementation Steps)

1.  **(Backend)** `app.py`:
    *   Create a Flask app instance.
    *   Define a list of article sources (List of URLs). To simplify the demo, we'll hardcode some relevant article URLs.
        *   For example:
            ```python
            article_sources = [
                "https://medium.com/p/015e28909290", # Your article
                "https://example.com/article-link-1", # Replace with real example URL
                "https://example.com/article-link-2", # Replace with real example URL
                "https://example.com/article-link-3", # Replace with real example URL
                "https://example.com/article-link-4"  # Replace with real example URL
            ]
            ```
    *   Create the root route `/`, which renders `templates/index.html`.
    *   Create an API route `/get-articles` (using the `GET` method, triggered by the frontend):
        *   Randomly select 3 **non-duplicate** URLs from the `article_sources` list.
        *   Use `random.sample()` to handle random selection and non-duplication.
        *   Handle the edge case where there are fewer than 3 sources (if `len(article_sources) < 3`, return all of them).
        *   Use `jsonify()` to return the results in JSON format, for example: `{"articles": ["url1", "url2", "url3"]}`.
        *   Add basic error handling (like `try...except`).
2.  **(Frontend)** `templates/index.html`:
    *   Include a button (e.g., `<button id="getArticlesBtn">Get Articles</button>`).
    *   Include an area for displaying article links (e.g., `<ul id="articleList"></ul>`).
    *   Write JavaScript:
        *   Get the button and list elements.
        *   Add a `click` event listener to the button.
        *   On click, clear existing list content.
        *   Use `fetch('/get-articles')` to call the backend API.
        *   Handle the API response:
            *   Check if the response is successful (`response.ok`).
            *   Parse the JSON (`response.json()`).
            *   Success: Iterate through the `data.articles` array, create `<li><a href="...">...</a></li>` for each URL and append to the list.
            *   Failure: Display an error message in the list area or console.
3.  **(Rules)** `.cursor/rules/`:
    *   Later create these `.mdc` files and fill them with content.
4.  **(Dependencies)** `requirements.txt`:
    *   Create a file and include `Flask`.
5.  **(Testing and Iteration)** (optional, but recommended for the demo):
    *   Write basic unit tests for the backend API.
    *   Based on test results or new ideas, return to Plan Mode or directly refactor and adjust in Act Mode.

# Expected Deliverable

A functioning Flask website that meets the functionality described in the project objectives.




# Technical Plan – AI Article Site

## Architecture Overview
- Flask server with two endpoints:
  - `/` renders the HTML template
  - `/get-articles` returns JSON data

## Project Structure

```