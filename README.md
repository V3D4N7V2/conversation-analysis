# conversation-analysis

## How to run the code:
1. Deepgram SDK requires python 3.10 or higher, this code is written with python 3.12 in mind. If you don't have python 3.12.0 installed, some things might break.
2. Clone the repository and cd into it: 
    `git clone https://github.com/V3D4N7V2/conversation-analysis.git`
    `cd conversation-analysis`

3. Install the requirements: `pip install -r requirements.txt`

4. Run the code: `python server.py`
5. Open the browser and go to `http://127.0.0.1:5000/` (can vary as flask might use a different port.But, it will be displayed in the terminal)
6. Upload the file and click on the submit button to get the results.
7. testapi.py is a script which uploads 1322-paul-accident.mp3 audio file to the /transcribe endpoint and prints the response. You can run it using `python testapi.py`

## ~~Whats left~~ Challanges/Issues faced:
1. ~~API on Cloud Service Provider.~~
2. PS. I don't have a credit card, so ended up hosting the code at `http://vedantghuge.pythonanywhere.com/` (webui)
3.  and the API at `http://vedantghuge.pythonanywhere.com/transcribe` (API)
4.  Local Server works totally fine though.
5. The service dosen't work well with longer audios, and the transcriptions fail (my guess is some upload speed/size limit. as I got this error `Exception: [Errno 90] Message too long`)
6. `1322-paul-accident60sec.mp3` seemed to work fine.
7. Also, The webserver is using gemini pro, wanted to try using it.