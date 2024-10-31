from gtts import gTTS
import os
import playsound

def text_to_speech(text, lang='en', slow=False):
    
    tts = gTTS(text=text, lang=lang, slow=slow)
    filename = 'output.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def main():
    print("Welcome to the Text-to-Speech Converter!")
    text = input("Please enter the text you want to convert to speech: ")


    print("\nChoose the voice selection:")
    print("1. English (US)")
    print("2. English (UK)")
    lang_options = {
        '1': 'en',
        '2': 'en-uk',
    }
    lang_choice = input("Enter the number of your choice: ")
    lang = lang_options.get(lang_choice, 'en') 

    print("\nChoose speech rate:")
    print("1. Normal")
    print("2. Slow")
    slow_choice = input("Enter the number of your choice: ")
    slow = slow_choice == '2'  

    text_to_speech(text, lang, slow)

if __name__ == "__main__":
    main()
