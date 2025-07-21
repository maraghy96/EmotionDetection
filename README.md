# Emotion Detection Web App

## Overview

**Emotion Detection** is a Natural Language Processing (NLP) project that analyzes and classifies emotions in text using Python. The application is built with Flask, providing a simple web interface for users to input text and receive an emotion analysis powered by Watson NLP API. The project also demonstrates modern software engineering best practices, including unit testing, robust error handling, and static code analysis.

---

## Features

- **NLP-Based Emotion Analysis:**  
  Detects key emotions (anger, disgust, fear, joy, sadness) in text using a pretrained language model.

- **Python & Flask Web Application:**  
  Interactive web interface served via Flask for real-time emotion analysis.

- **Unit Testing:**  
  Core logic is covered by automated unit tests using Python’s `unittest` module.

- **Robust Error Handling:**  
  User-friendly error messages and comprehensive exception management in both backend and web layers.

- **Static Code Analysis:**  
  Codebase is maintained according to Python best practices, passing PyLint static analysis checks.

---

## Getting Started

### Prerequisites

- Python 3.7+
- pip
- (Optional) `virtualenv` for isolated development

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/maraghy96/EmotionDetection.git
    cd EmotionDetection
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask server:**
    ```bash
    python server.py
    ```
    The application will be available at [http://localhost:5000](http://localhost:5000).

---

## Usage

- Open your web browser and go to [http://localhost:5000](http://localhost:5000)
- Enter text to analyze its emotional content.
- The application will display the scores for each emotion and indicate the dominant emotion.

---

## Testing

Unit tests are provided in `test_emotion_detection.py`.  
To run all tests:

```bash
python -m unittest test_emotion_detection.py
