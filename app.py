#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vibe Coding Demo Project: AI Article Sharer

This Flask application randomly provides article links about AI Vibe Coding.
"""

import random
from typing import Dict, List, Union, Optional, Tuple

from flask import Flask, jsonify, render_template, url_for, request

# Initialize Flask application
app = Flask(__name__)

# AI article source list
articles = [
    "https://medium.com/towards-data-science/chatgpt-explained-a-complete-guide-to-understanding-the-ai-language-model-0e5855512157",
    "https://towardsdatascience.com/all-you-need-to-know-about-llms-from-embedding-to-prompt-engineering-and-rag-09e9c69e8811",
    "https://www.marktechpost.com/2023/08/26/mit-and-ibm-introduce-dynalang-an-open-source-benchmark-designed-to-test-the-ability-of-llms-to-dynamically-switch-between-multiple-human-languages/",
    "https://arstechnica.com/information-technology/2023/09/openai-reveals-gpts-customizable-chatgpt-mini-apps-open-to-anyone-to-create/",
    "https://www.forbes.com/sites/bernardmarr/2023/09/11/the-amazing-ways-google-bard-uses-generative-ai/",
    "https://www.vox.com/future-perfect/23891756/ai-chatgpt-bing-bard-anthropic-claude-ethics-safety-existential-risk-value-alignment",
    "https://www.theverge.com/2023/8/22/23840529/meta-ai-assistant-chatbot-threads-messenger-facebook-instagram-whatsapp",
    "https://time.com/6324525/ai-agi-anthropic-claude/",
    "https://www.nytimes.com/2023/05/16/technology/ai-pioneer-godfather.html",
    "https://www.theguardian.com/technology/2023/apr/14/claude-ai-chatbot-anthropic-chatgpt-rival",
    "https://www.theatlantic.com/technology/archive/2023/09/anthropic-claude-2-ai-assistant/675156/",
    "https://www.wired.com/story/ai-chatbots-hallucinations-problem/",
    "https://podcasts.apple.com/us/podcast/cosmos-and-ai-a-conversation-with-sean-carroll/id1101223134?i=1000629118607",
    "https://openai.com/blog/new-models-and-developer-products-announced-at-devday",
    "https://writings.stephenwolfram.com/2023/06/claude-meets-wolfram/",
    "https://hbr.org/2023/10/the-competitive-map-of-ai-is-being-redrawn-daily",
    "https://www.quantamagazine.org/the-unpredictable-abilities-emerging-from-large-ai-models-20230316/"
]


@app.route('/')
def index() -> str:
    """
    Render the main page.
    
    Returns:
        str: Rendered HTML content
    """
    try:
        return render_template('index.html')
    except Exception as e:
        # Return error page with error message
        return render_template('index.html', error=f"Error loading page: {str(e)}")


@app.route('/get-articles')
def get_articles() -> Tuple[Dict[str, Union[List[str], str]], int]:
    """
    Randomly get non-duplicate article URLs from the article source.
    
    - If article_sources has 3 or more articles, return 3 random articles
    - If article_sources has fewer than 3 articles, return all available articles
    
    Returns:
        Tuple[Dict, int]: JSON response containing selected article URLs and HTTP status code
    """
    try:
        # Select three random articles from the list
        if len(articles) >= 3:
            selected_articles = random.sample(articles, 3)
        else:
            selected_articles = articles.copy()
        
        # Return response in JSON format
        return jsonify({
            "success": True,
            "articles": selected_articles
        }), 200
    
    except Exception as e:
        app.logger.error(f"Error occurred while getting articles: {str(e)}")
        return jsonify({
            "success": False,
            "error": f"Error getting articles: {str(e)}"
        }), 500


@app.errorhandler(404)
def page_not_found(e) -> Tuple[str, int]:
    """
    Handle 404 errors.
    
    Parameters:
        e: Error object
        
    Returns:
        Tuple[str, int]: Rendered error page and status code
    """
    return render_template('index.html', error="Page not found"), 404


@app.errorhandler(500)
def internal_server_error(e) -> Tuple[str, int]:
    """
    Handle 500 errors.
    
    Parameters:
        e: Error object
        
    Returns:
        Tuple[str, int]: Rendered error page and status code
    """
    return render_template('index.html', error="Internal server error"), 500


if __name__ == '__main__':
    app.run(debug=True) 