## main.py
import cv2
from pyzbar.pyzbar import decode
from text_to_speech_stream import text_to_speech_stream

def scan_qr_from_image(image_path):
    image = cv2.imread(image_path)
    detected_qr = decode(image)
    
    for qr in detected_qr:
        qr_data = qr.data.decode('utf-8')
        print(f"QR Code Founded! Result: {qr_data}")
        return qr_data
    
    print("QR Code Can't detected.")
    return None

if __name__ == "__main__":
    image_path = "QR.png"  # change with QRCode Image Path
    qr_text = scan_qr_from_image(image_path)
    
    if qr_text:
        text_to_speech_stream(qr_text)
