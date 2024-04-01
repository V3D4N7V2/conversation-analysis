from io import BytesIO
import os
from flask import Flask, request, jsonify, render_template
# import speech_recognition as sr

from sentimentAnalysis import get_sentiment_analysis


app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe_and_sa_audio():
    try:
        audio_file = request.files['audio']
        print("audio_file: ", audio_file)
        if audio_file:
            temp_file_path = 'tmp/' + audio_file.filename
            os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
            audio_file.save(temp_file_path)
            print("audio_file exists, get_sentiment_analysis... ")
            transcriptSA = get_sentiment_analysis(temp_file_path)
            print("get_sentiment_analysis done")
            os.remove(temp_file_path)
            return jsonify({'transcript': transcriptSA})
        else:
            return jsonify({'error': 'No audio file provided'}), 400
    except Exception as e:
        return jsonify({'transcript': str(e)}), 500
    

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
