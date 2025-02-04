## text_to_speech.py
import os
from playsound import playsound
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def text_to_speech_stream(text: str):
    response = client.text_to_speech.convert(
        voice_id = os.getenv("VOICE_ID"), # voice_id
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5", # use the turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Temporary Save and Play Audio
    temp_audio_file = "temp_audio.mp3"
    with open(temp_audio_file, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    
    playsound(temp_audio_file)
    os.remove(temp_audio_file)

