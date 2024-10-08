# YouTube Video Summarizer

YouTube Video Summarizer is a project that allows users to input YouTube video links and receive concise summaries of the video content. The application leverages the Google Gemini Pro API to analyze the video transcripts and provide accurate summaries.

## Features

- Input YouTube video links
- Generate concise summaries of video content
- Easy-to-use interface
- Adjustable summary length (short, medium, long)

## Getting Started

Follow these instructions to set up and run the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.8+
- Pip (Python package manager)
- Google Gemini Pro API key

### Installation

1. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Google Gemini Pro API key:**

   Create a `.env` file in the root directory of the project and add your Google Gemini Pro API key:

   ```plaintext
   GOOGLE_GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. **Run the application:**

   ```bash
   python app.py
   ```

2. **Open your web browser and go to** `http://localhost:5000`

3. **Input the YouTube video link and select the summary length, then generate the summary!**


## Acknowledgments

- Google Gemini Pro API
- YouTube Transcript API

