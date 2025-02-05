# QRCodeCanSpeak with ElevenLabs
## Created by Raekunisme

This project reads a QR code from an image, extracts the text from it, and converts it to speech using ElevenLabs API. The following dependencies are used:
- `opencv-python` for image processing.
- `pyzbar` for scanning QR codes.
- `playsound` to play the generated audio.
- `elevenlabs` for text-to-speech conversion.

## Installation & Setup

### Step 1: Install Dependencies
Install the required libraries by running the following command:
```bash
pip install opencv-python pyzbar playsound elevenlabs
```

### Step 2: Import Your QR Code Image
Make sure you have a QR code image ready that contains the text you want to be converted to speech.

### Step 3: Update QR Code Image Path in main.py
Open the main.py file and replace the image_path variable with the path to your QR code image. It should look something like this:
```bash
if __name__ == "__main__":
    image_path = "QR.png"  # change with Your QRCode Image Path
    qr_text = scan_qr_from_image(image_path)
    
    if qr_text:
        text_to_speech_stream(qr_text)
```

### Step 4: Create a .env File for API Keys
Create a .env file in the root directory of your project and add your ElevenLabs API key and Voice ID like so:
```bash
ELEVENLABS_API_KEY="YOUR_ELEVENLABS_API_KEY"
VOICE_ID="YOUR_VOICE_ID"
```

### Step 5: Run the Program
Now, you're ready to run the program! Execute the following command in your terminal or command prompt:
```bash
python main.py
```

This will scan the QR code in your image, extract the text, and use ElevenLabs to convert it to speech, which will then be played automatically.
