import os

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

# Path to the audio file


API_KEY = "2eb3bb5301dc61e51e3b5d9d6722eaf9dc443625"


def speech2text(audio_file):
    try:
        deepgram = DeepgramClient(API_KEY)

        with open(audio_file, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            language="uk"
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]
        return transcript

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    print(speech2text("audio_2024-05-07_09-13-26.ogg"))

