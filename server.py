from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Receives text from the HTML interface and runs emotion detection.
    Returns the emotion scores and dominant emotion in the required format.
    Displays an error message for blank or invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    try:
        response = emotion_detector(text_to_analyze)

        # If dominant_emotion is None, input was blank or API rejected it
        if not response or response['dominant_emotion'] is None:
            return "Invalid text! Please try again!"

        output = (
            "{\n"
            f'    "anger": {response["anger"]},\n'
            f'    "disgust": {response["disgust"]},\n'
            f'    "fear": {response["fear"]},\n'
            f'    "joy": {response["joy"]},\n'
            f'    "sadness": {response["sadness"]},\n'
            f'    "dominant_emotion":"{response["dominant_emotion"]}"\n'
            "}"
        )

        return output

    except Exception as error:
        return f"An error occurred during emotion analysis: {str(error)}"

@app.route("/")
def render_index_page():
    ''' Renders the main application page over the Flask channel.'''
    return render_template('index.html')

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)