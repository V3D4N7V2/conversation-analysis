# main.py (python example)

import json
import os
# from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

# load_dotenv()



import hashlib

def calculate_hash(file_path, algorithm='sha256'):
    """
    Calculate the hash of a file using a specified algorithm.

    Parameters:
        file_path (str): Path to the file.
        algorithm (str): Hash algorithm. Default is 'sha256'.

    Returns:
        str: Hexadecimal representation of the calculated hash.
    """
    hash_algorithm = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_algorithm.update(chunk)
    return hash_algorithm.hexdigest()


def deepgram_audio_response(audio_file="1322-paul-accident.mp3"):
    # save audio file transcription by hashes to save time of same file used later.
    audio_hash = calculate_hash(audio_file)
    print(f"Audio hash: {audio_hash}")

    # check if hash in previous results json file, if exists then return the saved result.
    try:
        with open("results.json", "r+") as f:
            results = json.load(f)
            if audio_hash in results:
                with open(results[audio_hash], "r+") as result_file:
                    response = json.load(result_file)
                    return response
    except FileNotFoundError:
        with open("results.json", "w") as f:
            f.write("{}")

    API_KEY = "101d75bc5288d2ed6b12497af817e2bfe4bdc264"
    # API_KEY = os.getenv("DG_API_KEY")
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)

        with open(audio_file, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        # STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            diarize=True,
            summarize="v2",
            detect_topics=True,
            # detect_sentiments=True,

        )

        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v(
            "1").transcribe_file(payload, options)

        # STEP 4: Print the response
        print(response.to_json(indent=4))

        # save the response to a file
        
        response_location = f"deepgram_responses/{audio_hash}.json"
        
        os.makedirs("deepgram_responses", exist_ok=True)

        with open("results.json", "r+") as f:
            results = json.load(f)
            results[audio_hash] = response_location
            f.seek(0)
            json.dump(results, f)

        with open(response_location, "w") as result_file:
            json.dump(response.to_dict(), result_file)

        return response

    except Exception as e:
        print(f"Exception: {e}")


def transcribe_file(audio_file="1322-paul-accident.mp3"):
    try:
        print(f"Transcribing {audio_file}")
        response = deepgram_audio_response(audio_file)
        print(response)
        transcribed_text = response["results"]["channels"][0]["alternatives"][0]["paragraphs"]["transcript"]
        print(transcribed_text)
        return transcribed_text
    except Exception as e:
        print(f"Exception: {e}")
        return str(e)
