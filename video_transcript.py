import tkinter as tk
from tkinter import filedialog
import whisper

# Step 1: Open a file picker dialog to select the video file
root = tk.Tk()
root.withdraw()  # Hide the root window
video_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")])

# Step 2: Load the Whisper model
model = whisper.load_model("base")

# Step 3: Transcribe the selected video file
if video_path:
    print(f"Transcribing: {video_path}")
    result = model.transcribe(video_path)

    # Step 4: Print and save the transcript to a file
    transcript = result["text"]
    print("Transcript:")
    print(transcript)

    with open("transcript.txt", "w") as f:
        f.write(transcript)
    print("Transcript saved to transcript.txt")
else:
    print("No file selected.")
