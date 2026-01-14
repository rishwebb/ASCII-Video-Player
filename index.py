# Developed by Rishav Biswas

import cv2 # pyright: ignore[reportMissingImports]
import os
import time
import numpy as np

def convert_frame_to_ascii(frame, width=130):
    """
    Convert a frame to ASCII art using a character set based on brightness
    """
    ascii_chars = " .:-=+*#%@"
    
    # Optimized for 15-inch laptop screens to prevent vertical scrolling
    height = int(frame.shape[0] * width / frame.shape[1] / 4.0) 
    if height == 0:
        height = 1
        
    resized_frame = cv2.resize(frame, (width, height))

    if len(resized_frame.shape) > 2:
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    else:
        gray_frame = resized_frame
    
    normalized = gray_frame / 255.0
    ascii_frame = ""
    
    for row in normalized:
        for pixel in row:
            index = int(pixel * (len(ascii_chars) - 1)) 
            ascii_frame += ascii_chars[index]
        ascii_frame += "\n"
    
    return ascii_frame

def play_video_in_terminal(video_path, width=130, fps=30):
    """
    Play a video in the terminal using ASCII characters in an infinite loop
    """
    if not os.path.exists(video_path):
        print(f"Error: Video file '{video_path}' not found.")
        return
    
    cap = cv2.VideoCapture(video_path)

    video_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = 1.0 / video_fps if video_fps > 0 else 1.0 / fps
    
    try:
        while True:
            ret, frame = cap.read()
            
            # If the video ends, reset it to the first frame to loop
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            
            ascii_art = convert_frame_to_ascii(frame, width)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_art)
            
            time.sleep(frame_delay)
            
    except KeyboardInterrupt:
        print("\nVideo playback stopped.")
    
    finally:
        cap.release()

if __name__ == "__main__":
    video_path = input("Enter the path to the video file: ").strip()
    
    try:
        width = int(input("Enter terminal width (default 130): ") or "130")
    except ValueError:
        width = 130

    try:
        fps = int(input("Enter FPS (default: use video FPS): ") or "0")
    except ValueError:
        fps = 0
    
    play_video_in_terminal(video_path, width, fps)