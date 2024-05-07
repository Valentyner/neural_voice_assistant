from flask import Flask, request, send_file, render_template
import tempfile
from text2speech import text2speech
from speech2text import speech2text

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process-audio", methods=["POST"])
def process_audio():
    audio_data = request.files["audio"].read()

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
        temp_audio.write(audio_data)
        temp_audio.flush()

    text = speech2text((temp_audio.name))
    generated_speech = text2speech(text)

    return send_file(generated_speech, mimetype="audio/mpeg")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
