#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vibe Coding 示範專案：AI 文章分享器

這個 Flask 應用程式能夠隨機提供關於 AI Vibe Coding 的文章連結。
"""

import random
from typing import Dict, List, Union, Optional, Tuple

from flask import Flask, jsonify, render_template, url_for, request

# 初始化 Flask 應用
app = Flask(__name__)

# 文章來源列表 (硬編碼)
article_sources: List[str] = [
    "https://medium.com/p/015e28909290",  # Vibe Coding 經驗分享
    "https://docs.cursor.com/context/rules",  # Cursor Rules 文件
    "https://www.deeplearning.ai/the-batch/issue-24-real-magical-code-generation/",  # DeepLearning.AI - 程式碼生成
    "https://medium.com/@johnowens/why-is-cursor-the-best-ai-based-ide-a-love-letter-f44e5fbdd75d",  # Cursor 優勢分析
    "https://martinfowler.com/articles/2023-chatgpt-x-programmer.html"  # Martin Fowler 關於 AI 編程的看法
]


@app.route('/')
def index() -> str:
    """
    渲染主頁面。
    
    Returns:
        str: 渲染後的 HTML 內容
    """
    return render_template('index.html')


@app.route('/get-articles')
def get_articles() -> Tuple[Dict[str, Union[List[str], str]], int]:
    """
    從文章來源中隨機獲取不重複的文章 URL。
    
    - 如果 article_sources 有 3 篇或更多文章，返回 3 篇隨機文章
    - 如果 article_sources 少於 3 篇，返回所有可用的文章
    
    Returns:
        Tuple[Dict, int]: 包含所選文章 URL 的 JSON 回應和 HTTP 狀態碼
    """
    try:
        # 去除重複的 URL (如果有的話)
        unique_urls = list(set(article_sources))
        
        # 判斷可用的 URL 數量，並選擇適當數量的文章
        if len(unique_urls) >= 3:
            selected_articles = random.sample(unique_urls, 3)
        else:
            selected_articles = unique_urls
        
        # 返回 JSON 格式的回應
        return jsonify({"articles": selected_articles}), 200
    
    except Exception as e:
        app.logger.error(f"獲取文章時發生錯誤: {str(e)}")
        return jsonify({"error": "無法檢索文章"}), 500


@app.errorhandler(404)
def page_not_found(e) -> Tuple[str, int]:
    """
    處理 404 錯誤。
    
    Args:
        e: 錯誤對象
        
    Returns:
        Tuple[str, int]: 渲染後的錯誤頁面和狀態碼
    """
    return render_template('index.html', error="找不到頁面"), 404


@app.errorhandler(500)
def internal_server_error(e) -> Tuple[str, int]:
    """
    處理 500 錯誤。
    
    Args:
        e: 錯誤對象
        
    Returns:
        Tuple[str, int]: 渲染後的錯誤頁面和狀態碼
    """
    return render_template('index.html', error="伺服器內部錯誤"), 500


if __name__ == '__main__':
    app.run(debug=True) 