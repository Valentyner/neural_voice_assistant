import torch
import whisper

def speech_to_text(audio_path, device, language="Ukrainian"):

    model = whisper.load_model("base").to(device)
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio).to(device)

    options = whisper.DecodingOptions(language="Ukrainian")

    model.eval()

    with torch.no_grad():
        result = whisper.decode(model, mel, options)

    with open("transcription.txt", "w") as f:
        f.write(result.text)
