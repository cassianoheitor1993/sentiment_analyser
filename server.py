"""
This module implements a Flask web application for sentiment analysis
using a specified API for text processing.
"""

from flask import Flask, render_template, request  # Removed unused jsonify
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route('/sentimentAnalyzer', methods=['GET'])
def sent_analyzer():
    """Analyze the sentiment of the text provided in the request."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    if label is None:
        return "Invalid input! Try again."
    return (
        f"The given text has been identified as {label.split('_')[1]} "
        f"with a score of {score}."
    )  # Using f-string and breaking into multiple lines for readability

@app.route("/")
def render_index_page():
    """Render the index HTML page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
