# %%
from openai import OpenAI
from deepgramstt import transcribe_file

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-yh3JsZ0grs4u3gFVHKxUU89RnlY2gduycX6CyWLTPeayIilT",
    base_url="https://api.chatanywhere.tech/v1"
    # base_url="https://api.chatanywhere.cn/v1"
)

# completion = client.chat.completions.create(
    
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     ]
# )

# print(completion.choices[0].message)


# %%

dummyTranscription = """
[Speaker_1]: Hello, Dave. How are you? 
[Speaker_2]: Hi, Joseph. I'm good. Yesterday went for a run. What about you? 
[Speaker_1]: I'm fine. Today I will read a book. I like reading. 
[Speaker_2]: That's nice. I like running.
[Speaker_1]: I dislike running.
[Speaker_2]: I understand. I dislike reading.
[Speaker_1]: I'm in a good mood today.
[Speaker_2]: I'm in a bad mood today.
[Speaker_1]: I'm feeling sad.
[Speaker_2]: I am the best runner in the world.
[Speaker_1]: I am the worst reader in the world.
[Speaker_2]: I am happy.
[Speaker_1]: I am sad.
[Speaker_2]: Nice to talk to you, bye.
[Speaker_1]: Bye.
"""

def sentiment_analysis(transcription=dummyTranscription):
    response = client.chat.completions.create(
        # model="gpt-4",
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": """
                As an AI with expertise in language and emotion analysis, your task is to analyze the sentiment of the following text. Please consider the overall tone of the discussion, the emotion conveyed by the language used, and the context in which words and phrases are used. Indicate whether the sentiment is generally positive, negative, or neutral, and provide brief explanations for your analysis where possible.

                
                You will also extract Information such as likes, dislikes, hobbies, mood, empathy, confidence, psychological insights and other personal information from the conversation.
                You will give your conclusions in the following format for each type of information extracted:
                <Speaker> : <Info Type> -> <Conclusion>, <Explanation>
                For example:
                Joseph : Likes -> Reading, Joseph mentioned that he likes reading.
                Jimmy : Mood -> Happy, Jimmy sounded cheerful and positive throughout the conversation.
                Larry : psychological insights ->  Bored , Changes Conversation topic frequently, Larry seems to be bored.
                Bartholomew : Empathy -> Empathetic, Bartholomew showed empathy towards the speaker by offering support and understanding.
                Sheldon Cooper: Confidence -> Confident, Sheldon Cooper spoke with confidence and certainty.
                Jar Jar Binks : Mood -> Anxious, Jar Jar Binks sounded anxious and nervous throughout the conversation.
                Darth Vader: psychological insights -> Shy, Darth Vader sounded shy throughout the conversation with a low tone of voice.
                """
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response.choices[0].message.content

# print(sentiment_analysis(dummyTranscription))

# %%

# transcription = transcribe_file("1322-paul-accident.mp3")

# %%
# print(transcription)

# %%
# print(sentiment_analysis(transcription))


def get_sentiment_analysis(audio_file):
    transcription = transcribe_file(audio_file)
    return sentiment_analysis(transcription)