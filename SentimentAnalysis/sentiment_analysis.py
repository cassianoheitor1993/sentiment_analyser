import requests

def sentiment_analyzer(text_to_analyze):
    """Analyzes sentiment of the given text using an external API.

    Args:
        text_to_analyze (str): The text to be analyzed for sentiment.

    Returns:
        dict: A dictionary containing the sentiment label and score.
    """
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Create the payload with the text to be analyzed
    payload = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    try:
        # Make a POST request to the API with the payload and headers
        response = requests.post(url, json=payload, headers=headers)
        
        # Check if the response status code is 200
        if response.status_code == 200:
            formatted_response = response.json()  # Automatically parse JSON
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']
        # If the response status code is not 200, set label and score to None
        else:
            label = None
            score = None

    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., network issues)
        print(f"An error occurred: {e}")
        label = None
        score = None

    # Return the label and score in a dictionary
    return {'label': label, 'score': score}
