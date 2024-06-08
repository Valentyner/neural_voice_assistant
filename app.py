from flask import Flask, request, send_file, render_template, jsonify
import tempfile
from text2speech import text2speech
from speech2text import speech2text
from groq_service import execute
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process-text", methods=["POST"])
@cross_origin()
def process_text():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text data provided"}), 400

    text_data = data["text"]
    generated_answer = execute(f"Будь ласка дай відповідь на запит Українською мовою {text_data}")

    return jsonify({"answer": generated_answer})


@app.route("/process-audio", methods=["POST"])
@cross_origin()
def process_audio():
    audio_data = request.files["audio"].read()

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
        temp_audio.write(audio_data)
        temp_audio.flush()

    text = speech2text(temp_audio.name)
    generated_answer = execute(f"Будь ласка дай відповідь на запит Українською мовою {text}")
    print(generated_answer)
    generated_speech = text2speech(generated_answer)

    return send_file(generated_speech, mimetype="audio/mpeg")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
