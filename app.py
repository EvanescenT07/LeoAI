# from flask import Flask, render_template, request, jsonify
import win32com.client
import speech_recognition as sr
from openai import OpenAI
# from dotenv import load_dotenv
import webbrowser
import datetime
import os

# app = Flask(__name__)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
SAVE_FILE = True
# load_dotenv()
# API_KEY = os.getenv('API_KEY')
API_KEY = open("API_KEY", "r").read()

def say(text):
    speaker.Speak(text)

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1.2
        audio = r.listen(source)
        try:
            print("Recognizing....")
            user_input = r.recognize_google(audio, language='en-us')
            print(f"User said : {user_input}")
            return user_input
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand. Please try again."
        except sr.RequestError as e:
            return f"Sorry, there was an error with the speech recognition service: {e}"

def ask_ai(user_input):
    client = OpenAI(
        api_key=API_KEY
        )  
    text = f"Prompt: {user_input} \n******************\n\n"
    messages = [{"role": "user", "content": user_input}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500,
    )
    ai_response = response.choices[0].message.content

    if not os.path.exists("OpenAI"):
        os.makedirs("OpenAI")
    if SAVE_FILE:
        filename = f"OpenAI/{'_'.join(user_input.split())}.txt"
        with open(filename, "w") as file:
            file.write(text + response.choices[0].message.content)

    say(ai_response)
    return ai_response

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/process_voice_input', methods=['POST'])
# def process_voice_input():
#     user_input = request.json.get('user_input')
#     output = ask_ai(user_input)
#     return jsonify({'output': output})

# @app.route('/start_listening', methods=['POST'])  # New route for starting speech recognition
# def start_listening():
#     say("I'm listening. Please give a command.")
#     user_input = Command()  # Call the speech recognition function
#     output = ask_ai(user_input)
#     return jsonify({'output': output})

if __name__ == '__main__':
    say("Hi.... I'm Leo A.I. I'm your personal assistant. How can I help you?")
#     app.run(debug=True)
    while True:
        print("Listening.....")
        list = Command()

        # Open Websites integrated with Google Chrome
        websites = [[
            "Youtube", "https://www.youtube.com/"
        ], [
            "google", "https://www.google.co.id/"
        ], [
            "Instagram", "https://www.instagram.com/"
        ], [
            "Github", "https://github.com/"
        ], [
            "my weapon", "https://chat.openai.com/"
        ]
        ]
        for web in websites:
            if f"Open {web[0]}".lower() in list.lower():
                say(f"Opening {web[0]}...")
                webbrowser.open(web[1])

        # Playing Music in local storage using VLC Media Player
        if "play music" in list:
            music_file = r"D:\Documents\President University\Final Project\Artificial Intelligence\assets\audio\Karena_Kamu_Cuma_Satu.mp3"
            print("Playing Music...")
            say("Playing Music...")
            os.system(f'start vlc "{music_file}"')
        # Stop Music
        elif "stop music" in list:
            say("Music Stopped")
            os.system("taskkill /f /im vlc.exe")

        # Tell the current time
        elif "what time is it" in list:
            time = datetime.datetime.now().strftime("%I:%M %p")
            # print(time)
            print(f"it is {time}")
            say(f"it is {time}")

        # Open Windows Application
        elif "play my game" in list:
            say("Opening Valorant...")
            os.system(r'start "" "C:\Game\Riot Games\Riot Client\RiotClientElectron\Riot Client.exe"')

        elif "open Spotify".lower() in list.lower():
            say("Opening Spotify...")
            os.system(r'start "" "C:\Users\zulfi\AppData\Roaming\Spotify\Spotify.exe"')

        elif "open Visual Studio Code".lower() in list.lower():
            say("Opening Visual Studio Code...")
            os.system(r'start "" "C:\Application\Microsoft VS Code\code.exe"')

        # Greeting
        elif any(keyword in list.lower() for keyword in ["hello", "hi", "hey"]):
            say("Hello, How can I help you?")

        # Exit the program
        elif any(keyword in list.lower() for keyword in ["exit", "goodbye", "quit"]):
            say("Goodbye, Have a nice day!")
            exit()

        elif "thank you".lower() in list.lower():
            say("You're welcome, it's my pleasure to help you.")

        # If the word count is sufficient, ask the A.I.
        elif len(list) > 10:
            ask_ai(list)

        # If the word count is insufficient, ask the user to repeat their question.
        elif len(list) < 9:
            say("Sorry, I didn't catch that. Can you say again?")