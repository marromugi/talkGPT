import whisper

def transcribe(wav_path):
    model = whisper.load_model("small")
    print(wav_path)
    result = model.transcribe(
        wav_path, verbose=True, 
        language='ja', 
        fp16=False
    )
    return result["text"] if result["text"] != None else ""


