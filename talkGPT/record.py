import pyaudio
import wave
import numpy as np
from datetime import datetime
from .transcribe import transcribe
from .chat import ask
from .voice import generate_voice, respond
from .env import conversations, byebye

def start():
    threshold = 0.1
    thresholdmin = 0.02
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    blank = 1
    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
        channels = CHANNELS,
        rate = RATE,
        input = True,
        frames_per_buffer = chunk
    )

    sound=[]
    while True:
        data = stream.read(chunk, exception_on_overflow = False)
        x = np.frombuffer(data, dtype="int16") / 32768.0
        if x.max() > threshold:
            rec = 0
            now_text = datetime.today().strftime("%Y%m%d%H%M%S")
            filename = './talkGPT/wav/asking/{}.wav'.format(now_text)
            sound=[]
            sound.append(data)
            # 0.5秒音がない場合、切る
            while rec < int(blank * RATE / chunk) / 2:
                data = stream.read(chunk, exception_on_overflow = False)
            
                sound.append(data)
                x = np.frombuffer(data, dtype="int16") / 32768.0
                if x.max() < thresholdmin:
                    rec += 1
                else:
                    rec = 0
            
            data = b''.join(sound)
        
            out = wave.open(filename,'w')
            out.setnchannels(CHANNELS)
            out.setsampwidth(2)
            out.setframerate(RATE)
            out.writeframes(data)
            out.close()

            # transcribe
            text = transcribe(filename)

            if text == byebye:
                print(conversations)
                break
            
            if text != "":
                conversations.append({"role": "user", "content": text})

                # ask to GPT
                answer = ask(conversations)
                print(answer)

                # update conversation log
                conversations.append({"role": "assistant", "content": answer})

                # generate voice
                voice_filepath = './talkGPT/wav/respond/{}.wav'.format(now_text)
                generate_voice(answer, voice_filepath)
                respond(voice_filepath)

    stream.close()
    p.terminate()
