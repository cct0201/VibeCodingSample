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



# 核心邏輯 (Act Mode 執行步驟)

1.  **(後端)** `app.py`:
    *   建立 Flask app instance。
    *   定義一個文章來源列表 (List of URLs)。為了簡化 demo，我們先硬編碼一些相關的文章 URL。
        *   例如:
            ```python
            article_sources = [
                "https://medium.com/p/015e28909290", # 您的文章
                "https://example.com/article-link-1", # 替換成真實的範例 URL
                "https://example.com/article-link-2", # 替換成真實的範例 URL
                "https://example.com/article-link-3", # 替換成真實的範例 URL
                "https://example.com/article-link-4"  # 替換成真實的範例 URL
            ]
            ```
    *   建立根路由 `/`，渲染 `templates/index.html`。
    *   建立 API 路由 `/get-articles` (使用 `GET` 方法，由前端觸發)：
        *   從 `article_sources` 列表中隨機選取 3 個 **不重複** 的 URL。
        *   使用 `random.sample()` 來處理隨機選取與不重複。
        *   處理來源列表數量不足 3 個的邊界情況 (如果 `len(article_sources) < 3`，則回傳所有)。
        *   使用 `jsonify()` 回傳 JSON 格式的結果，例如：`{"articles": ["url1", "url2", "url3"]}`。
        *   加入基本的錯誤處理 (例如 `try...except`)。
2.  **(前端)** `templates/index.html`:
    *   包含一個按鈕 (例如 `<button id="getArticlesBtn">取得文章</button>`)。
    *   包含一個用於顯示文章連結的區域 (例如 `<ul id="articleList"></ul>`)。
    *   撰寫 JavaScript：
        *   獲取按鈕和列表元素。
        *   為按鈕加上 `click` 事件監聽器。
        *   點擊後，清空現有列表內容。
        *   使用 `fetch('/get-articles')` 呼叫後端 API。
        *   處理 API 回應：
            *   檢查回應是否成功 (`response.ok`)。
            *   解析 JSON (`response.json()`)。
            *   成功：遍歷 `data.articles` 陣列，為每個 URL 建立 `<li><a href="...">...</a></li>` 並附加到列表中。
            *   失敗：在列表區域或 console 中顯示錯誤訊息。
3.  **(規則)** `.cursor/rules/`:
    *   稍後建立這些 `.mdc` 檔案並填入內容。
4.  **(依賴)** `requirements.txt`:
    *   建立檔案並包含 `Flask`。
5.  **(測試與迭代)** (可選，但建議加入 demo):
    *   針對後端 API 撰寫基本單元測試。
    *   根據測試結果或新的想法，回到 Plan Mode 或直接在 Act Mode 中進行重構與調整。

# 預期交付

一個能運行的 Flask 網站，符合專案目標描述的功能。




# Technical Plan – AI Article Site

## Architecture Overview
- Flask server with two endpoints:
  - `/` renders the HTML template
  - `/get-articles` returns JSON data

## Project Structure

```
.
├── app.py                       # Flask application entry point
├── templates/                   # Template directory
│   └── index.html               # HTML frontend template
├── static/                      # Static assets
│   ├── css/                     # CSS stylesheets
│   └── js/                      # JavaScript files
├── requirements.txt             # Python dependency list
├── plan.md                      # Technical design (How)
├── docs/                        # Documentation directory
│   └── prd_ai_article_site.md   # Product requirement document (What)
├── tasks/                       # Tasks directory
│   └── ai_article_site_tasks.md # Task list in Markdown table format
└── .cursor/                     # Cursor configuration
    └── rules/                   # Cursor rules
        ├── generate_tasks_from_prd.mdc  # Auto-rule to generate task list from PRD
        ├── python_linting.mdc           # Python linting rules
        ├── flask_best_practice.mdc      # Flask best practices
        └── business_logic.mdc           # Business logic rules
```

## Data Flow
- Client sends GET request to `/get-articles`
- Server randomly selects 3 URLs from a static list
- Server responds with a JSON object

## Logic Detail
- Use `random.sample()` to ensure non-repeating selection
- If less than 3 URLs, return all
- Use `jsonify()` for response

## Function/Module Plan
- `app.py`: flask app, endpoint definitions, logic for selection
- `index.html`: contains button + JS call to `/get-articles`

## Edge Cases
- Empty source list → return `{"articles": []}`
- Source list < 3 → no crash, return what exists

## Improvements (future)
- Move source list to config file or admin panel
- Add tagging or categories to articles
