
# **Youtube Video and Website Content Summarizer**  
Summarize YouTube videos and websites effortlessly using **LangChain**, **Groq**, and **OpenAI Whisper** for audio fallback. This app is built with **Streamlit** and provides accurate, concise summaries of online content.  

---

## **✨ Features**
-  Summarize **YouTube videos** (captions or audio transcription fallback)  
-  Summarize **web pages** using **Unstructured URL Loader**  
-  **Groq LLaMA-3.3** for fast and high-quality text summarization  
-  **OpenAI Whisper** for audio transcription when captions are unavailable  
-  Clean and interactive **Streamlit UI**  

---

## **🛠️ Tech Stack**
- **Python 3.13.0**
- **Streamlit** (User Interface)
- **LangChain** (Prompt chaining & summarization)
- **Groq LLM (LLaMA-3.3-70B-Versatile)**
- **OpenAI Whisper** (Audio transcription)
- **YouTube Transcript API** (Transcripts of Youtube Videos)
- **yt-dlp** (Audio extraction)
- **Unstructured URL Loader** (Web content loading)
- **dotenv** (Environment variables)

---

## **💡 How It Works**
1. **Input a URL** → YouTube video or a website.  
2. **Content Fetching**:
   - For **YouTube**:
     - Try **captions** via `youtube_transcript_api`
     - If no captions → Download audio & transcribe using **Whisper**
   - For **Websites**:
     - Extract text using **UnstructuredURLLoader**
3. **Summarization**:
   - Use **LangChain Summarize Chain** with **Groq LLaMA-3.3**  
4. **Output**: A **clear and concise summary** displayed on Streamlit.

---

## **📦 Requirements**
Add these to `requirements.txt`:
```
streamlit
langchain
langchain-groq
langchain-community
python-dotenv
youtube-transcript-api
yt-dlp
openai
validators
unstructured
```

---

## **🚀 Future Enhancements**
- Add **multi-language support**
- Generate **bullet point summaries**
- Enable **PDF summarization**
- Add **question-answering** on summarized content


