from flask import Flask, request, jsonify
import os
from scripts.check_hybrid_simf import hybrid_check

# Initialize Flask app
app = Flask(__name__)

# Upload folder setup
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    """Basic route to verify backend is running."""
    return jsonify({
        "message": "Music Plagiarism Detector Backend is Running ✅",
        "usage": "POST /analyze with audio (and optional lyrics) files"
    })


@app.route('/analyze', methods=['POST'])
def analyze():
    """Handle audio + lyrics upload and run plagiarism check."""
    try:
        audio_file = request.files.get('audio')
        lyrics_file = request.files.get('lyrics')

        if not audio_file:
            return jsonify({'error': 'No audio file uploaded!'}), 400

        # Save uploaded audio
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
        audio_file.save(audio_path)

        # Save uploaded lyrics (optional)
        lyrics_path = None
        if lyrics_file:
            lyrics_path = os.path.join(app.config['UPLOAD_FOLDER'], lyrics_file.filename)
            lyrics_file.save(lyrics_path)

        # Run hybrid plagiarism check
        result = hybrid_check(audio_path, lyrics_path)

        # Ensure response is serializable
        if isinstance(result, (dict, list)):
            return jsonify(result)
        else:
            return jsonify({'result': str(result)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Hide TensorFlow logs for cleaner output
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    print("🚀 Flask backend is running on http://127.0.0.1:5000")
    app.run(debug=True)
