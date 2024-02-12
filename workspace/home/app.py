from flask import Flask, send_from_directory, request, jsonify
from classifier import classifier  # Import your image classification function
import os

app = Flask(__name__)

# Define the directory where the frontend files are stored
STATIC_DIR = 'frontend'

# Route to serve the homepage (index.html)
@app.route('/')
def index():
    return send_from_directory(STATIC_DIR, 'index.html')

# Route to serve static files (CSS, JavaScript, images)
@app.route('/<path:filename>')
def serve_static(filename):
    # Check if the requested file exists in the static directory
    if os.path.exists(os.path.join(STATIC_DIR, filename)):
        return send_from_directory(STATIC_DIR, filename)
    else:
        return jsonify({'error': 'File not found'}), 404

# Route to classify the image and return the result
@app.route('/classify', methods=['POST'])
def classify():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    
    # Process the image using your image classification function
    # The classifier function takes the image file and the model name as input
    # Replace 'vgg' with the appropriate model name if necessary
    classification_result = classifier(image_file, 'vgg')  # Pass model name directly
    
    # Return the classification result with the key 'classification'
    result = {'classification': classification_result}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
