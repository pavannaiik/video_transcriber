import tkinter as tk
from tkinter import filedialog
import whisper

# Step 1: Open a file picker dialog to select the video file
root = tk.Tk()
root.withdraw()  # Hide the root window
video_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")])

# Step 2: Load the Whisper model
model = whisper.load_model("base")

# Step 3: Transcribe the selected video file with timestamps
if video_path:
    print(f"Transcribing: {video_path}")
    result = model.transcribe(video_path, verbose=False)

    # Step 4: Group transcript by 2-minute intervals
    segments = result["segments"]
    transcript_by_intervals = {}
    current_interval = 0

    for segment in segments:
        start_time = int(segment["start"])  # in seconds
        end_time = int(segment["end"])      # in seconds
        text = segment["text"]

        # Calculate the current 2-minute interval
        interval = (start_time // 120) * 2

        # Group text by the interval
        if interval not in transcript_by_intervals:
            transcript_by_intervals[interval] = ""
        transcript_by_intervals[interval] += text + " "

    # Step 5: Save the transcript to a file
    with open("transcript_with_timestamps.txt", "w") as f:
        for interval, text in sorted(transcript_by_intervals.items()):
            start_minute = interval
            end_minute = interval + 2
            f.write(f"{start_minute:02d}:00 to {end_minute:02d}:00\n{text.strip()}\n\n")

    print("Transcript saved to transcript_with_timestamps.txt")
else:
    print("No file selected.")
