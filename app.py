# Importing required modules from Flask
from flask import Flask, render_template, request, jsonify

# Import the predict_trash function which will handle model prediction (we will create this in utils.py)
from utils import predict_trash
import os  # Used to save and delete files

# Initialize the Flask application
app = Flask(__name__)

# ----------------------------
# HOME PAGE ROUTE
# ----------------------------
@app.route('/')
def index():
    # When a user visits the root URL '/', render the index.html template
    return render_template('index.html')


# ----------------------------
# PREDICTION ROUTE (POST)
# ----------------------------
@app.route('/predict', methods=['POST'])
def predict():
    # Step 1: Check whether the uploaded file is included in the request or not
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400  # If not found, return an error response

    file = request.files['file']  # Get the uploaded file from the request

    # Step 2: Check if the user has actually selected a file (filename is not empty)
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400  # If filename is empty, return an error

    # Step 3: Save the uploaded file temporarily in the 'static' folder
    image_path = os.path.join('static', 'uploaded_image.jpg')
    file.save(image_path)

    # Step 4: Pass the saved image path to the model for prediction (function defined in utils.py)
    result = predict_trash(image_path)

    # Step 5: Delete the uploaded image after prediction is completed to save space
    os.remove(image_path)

    # Step 6: Return the prediction result as a JSON response to the frontend
    return jsonify(result)

# ----------------------------
# APP RUNNER
# ----------------------------
if __name__ == '__main__':
    # Run the Flask app locally; debug=True helps in displaying detailed error logs in the console
    app.run(debug=True)

