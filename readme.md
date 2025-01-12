# YouTube Transcript & Summary Generator

This application allows users to generate transcripts and summaries for YouTube videos by providing a video URL. It leverages the `YouTubeTranscriptApi` for fetching transcripts and a transformer model for summarization. Users can also download the transcript and summary as text files.

---

## Features
- Extracts transcripts from YouTube videos.
- Summarizes transcripts into short, medium, or long summaries using a BART transformer model.
- Allows users to download transcripts and summaries.
- Provides a responsive and user-friendly web interface.

---

## Requirements

- Python 3.7+
- Flask
- transformers
- youtube-transcript-api

---

## Installation and Setup

### 1. Clone the Repository
```bash
$ git clone <repository-url>
$ cd <repository-folder>
```

### 2. Create and Activate a Virtual Environment
```bash
$ python -m venv venv
$ source venv/bin/activate    # On macOS/Linux
$ venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```bash
$ pip install -r requirements.txt
```

### 4. Run the Application
```bash
$ python app.py
```
Access the application in your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## File Structure
- `app.py`: The main application file.
- `templates/index.html`: The HTML template for the web interface.
- `static`: Folder for static files (e.g., CSS, JavaScript, images).
- `.gitignore`: To exclude unnecessary files (e.g., `venv`, `__pycache__`, etc.) from version control.

---

## Adding `.gitignore`
Ensure your `.gitignore` includes:
```
venv/
__pycache__/
*.pyc
.DS_Store
```

---

## Commands to Push to GitHub

### 1. Initialize Git Repository
```bash
$ git init
$ git add .
$ git commit -m "Initial commit"
```

### 2. Add Remote Repository
```bash
$ git remote add origin <repository-url>
$ git branch -M main
$ git push -u origin main
```

---

## Creating a GitHub Pages Link

1. Go to the GitHub repository.
2. Navigate to `Settings` > `Pages`.
3. Under the "Source" section, select the branch (`main`) and folder (`/ (root)` or `/docs` if applicable).
4. Save and GitHub Pages will provide a link to access the application.

---

## Notes
- Make sure to include your `requirements.txt` for easy setup.
- If deploying publicly, consider securing your application and handling rate limits from APIs.
