"""
server.py
This module contains the Flask application for detecting emotions
from a given text input. It provides an endpoint to receive text
and return the detected emotions as a JSON response.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Route to analyze the emotion from the provided statement.

    Returns:
        JSON response containing the analysis results and a message.
    """
    statement = request.json.get('statement', '')
    result = emotion_detector(statement)

    # Check for invalid input
    if result['dominant_emotion'] is None:
        return jsonify(message="Invalid text! Please try again."), 400

    # Prepare response message
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify(result=result, message=response_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
