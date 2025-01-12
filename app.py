from flask import Flask, render_template, request, send_file
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re
from transformers import pipeline
import io
import time

app = Flask(__name__)

def extract_video_id(url):
    regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    return None

def generate_summary(text, length_option):
    # Configure summary length based on selection
    max_length = {
        'short': 150,
        'medium': 250,
        'long': 400
    }.get(length_option, 250)
    
    min_length = max_length // 2

    # Initialize the summarization pipeline
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Split text into chunks if it's too long
    max_chunk_length = 1024
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    
    # Summarize each chunk and combine
    summaries = []
    for chunk in chunks:
        if len(chunk) > 100:  # Only summarize chunks with sufficient content
            summary = summarizer(chunk, max_length=max_length//len(chunks), 
                               min_length=min_length//len(chunks), 
                               do_sample=False)[0]['summary_text']
            summaries.append(summary)
    
    return " ".join(summaries)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = None
    summary = None
    if request.method == "POST":
        video_url = request.form.get("video_url")
        length_option = request.form.get("summary_length", "medium")
        video_id = extract_video_id(video_url)
        
        if not video_id:
            transcript = "Video ID could not be extracted."
        else:
            try:
                # Simulate processing time for loading bar
                time.sleep(2)
                
                transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
                formatter = TextFormatter()
                transcript = formatter.format_transcript(transcript_data)
                
                # Generate summary if transcript is obtained
                if transcript:
                    summary = generate_summary(transcript, length_option)
                
            except Exception as e:
                transcript = f"An error occurred: {e}"

    return render_template("index.html", transcript=transcript, summary=summary)

@app.route("/download_summary")
def download_summary():
    summary = request.args.get('summary', '')
    buffer = io.StringIO()
    buffer.write(summary)
    buffer.seek(0)
    
    return send_file(
        io.BytesIO(buffer.getvalue().encode()),
        mimetype='text/plain',
        as_attachment=True,
        download_name='summary.txt'
    )

@app.route("/download_transcript")
def download_transcript():
    transcript = request.args.get('transcript', '')
    buffer = io.StringIO()
    buffer.write(transcript)
    buffer.seek(0)
    
    return send_file(
        io.BytesIO(buffer.getvalue().encode()),
        mimetype='text/plain',
        as_attachment=True,
        download_name='transcript.txt'
    )

if __name__ == "__main__":
    app.run(debug=True)