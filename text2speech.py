import os

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)

filename = "output2.wav"


def text2speech(text):
    try:
        SPEAK_OPTIONS = {"text": text}
        deepgram = DeepgramClient(api_key="2eb3bb5301dc61e51e3b5d9d6722eaf9dc443625")

        options = SpeakOptions(
            model="aura-asteria-en",
            encoding="linear16",
            container="wav"
        )

        response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        return filename

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    text2speech("This is a text to speech test")
