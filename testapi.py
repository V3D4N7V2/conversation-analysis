import requests

# test Function
def test_function(file_path, server_api_url='http://127.0.0.1:5000/transcribe'):
    try:
        files = {'audio': open(file_path, 'rb')}
        response = requests.post(server_api_url, files=files)
        if response.status_code == 200:
            return response.json()['transcript']
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return str(e)

# Example usage:
file_path = '1322-paul-accident.mp3'
transcript = test_function(file_path)
print("Output:", transcript)
