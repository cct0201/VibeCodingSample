# Vibe Coding 示範專案：AI 文章分享器

這是一個用於展示「Vibe Coding」開發流程的示範專案。專案實現了一個簡單的 Flask 網站，讓使用者點擊按鈕後，隨機獲取三篇關於 AI 與 Vibe Coding 的文章連結。

## 專案背景

本專案源自我在 [從「寫程式」到「與 AI 共舞」──我在公司推動 Vibe Coding 的經驗分享](https://medium.com/p/015e28909290) 一文中分享的經驗。該文探討了如何將 AI 助手 (如 Cursor) 從個人效率工具提升為團隊知識共享與協作的一部分。

## Vibe Coding 的四個層次

示範專案展示了文章中提到的 Vibe Coding 四個層次：

1. **Level 1 (Generate)**: 使用 AI 生成基本程式碼和結構
2. **Level 2 (Enhance)**: 讓 AI 協助重構與優化程式碼
3. **Level 3 (Systematize)**: 通過 Project Rules 系統化團隊知識與規範
4. **Level 4 (Automate)**: 整合到工作流程 (本示範專案不涵蓋)

## 專案設計重點

這個專案特意設計成小型且簡單，但同時包含了實際開發中的各種考量：

- **Plan Mode**: 通過 `plan.md` 進行詳細規劃，說明專案目標與實作步驟
- **規則落地**: 使用 `.cursor/rules/` 中的 Project Rules 系統化團隊規範：
  - 業務邏輯規則 (`business_logic.mdc`)
  - Python 程式碼風格規則 (`python_linting.mdc`)
  - Flask 最佳實踐 (`flask_best_practice.mdc`)
- **Act Mode**: 根據計畫和規則，實作具體功能

## 專案結構

```
.
├── app.py              # 主要 Flask 應用程式
├── templates/
│   └── index.html      # 前端頁面模板
├── static/             # (可選) 存放 CSS/JS 檔案
├── .cursor/rules/      # Cursor Project Rules 目錄
│   ├── business_logic.mdc
│   ├── python_linting.mdc
│   └── flask_best_practice.mdc
├── requirements.txt    # Python 依賴列表
├── plan.md             # 開發計畫
└── README.md           # 本說明檔
```

## 如何運行

1. 安裝依賴：
   ```
   pip install -r requirements.txt
   ```

2. 運行 Flask 應用：
   ```
   flask run
   ```

3. 在瀏覽器中訪問：
   ```
   http://localhost:5000
   ```

## 如何使用這個示範

本專案作為展示 Vibe Coding 的教學範例，您可以關注以下幾點：

1. 閱讀 `plan.md` 了解專案規劃思路
2. 查看 `.cursor/rules/` 目錄，理解如何將團隊知識系統化
3. 研究 `app.py` 和 `templates/index.html` 如何遵循這些規則
4. 嘗試自己修改或擴充功能，感受 AI 如何根據已有規則協助開發

## 擴展建議

若要將這個示範項目擴展為更完整的應用，您可以考慮：

1. 整合搜尋 API，動態獲取文章而不是使用硬編碼列表
2. 添加文章預覽功能
3. 實現使用者收藏功能
4. 加入分類篩選功能

## 關於 Vibe Coding

Vibe Coding 不僅是使用 AI 輔助編程，而是一種將 AI 視為團隊成員的開發理念，重點在於：

1. 從**個人效率**到**團隊知識**的轉變
2. 將隱性知識通過規則系統化
3. 讓 AI 理解並遵循團隊的業務邏輯與技術標準

---

*本專案僅作為示範與教學用途。* 