import os
import tempfile
import validators
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp
from openai import OpenAI
from langchain.schema import Document

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize LLM
model_name = "llama-3.3-70b-versatile"
llm = ChatGroq(api_key=groq_api_key, model=model_name)

# Initialize OpenAI client for Whisper
openai_client = OpenAI(api_key=openai_api_key)

# Streamlit UI
st.set_page_config("LangChain Summarizer", layout="centered")
st.title("Summarizer")
st.subheader("Summarize YouTube videos and websites using LangChain (with Whisper fallback)")

# Get URL input
url = st.text_input("Enter a YouTube video or website URL:")

if st.button("Summarize"):
    if not url.strip():
        st.error("Please enter a valid URL.")
    elif not validators.url(url):
        st.error("Invalid URL format.")
    else:
        try:
            with st.spinner("Fetching content..."):
                if "youtube.com" in url or "youtu.be" in url:
                    video_id = url.split("v=")[-1] if "v=" in url else url.split("/")[-1]
                    text_content = None

                    # Try captions first
                    try:
                        st.info("Trying to fetch captions...")
                        transcript = YouTubeTranscriptApi.get_transcript(video_id)
                        text_content = " ".join([t['text'] for t in transcript])
                        st.success("Captions fetched successfully!")
                    except Exception:
                        st.warning("No captions available. Falling back to audio transcription...")

                        # Download audio using yt_dlp
                        with tempfile.TemporaryDirectory() as tmpdir:
                            audio_path = os.path.join(tmpdir, "audio.mp3")
                            ydl_opts = {
                                'format': 'bestaudio/best',
                                'outtmpl': audio_path
                            }
                            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                                ydl.download([url])

                            # Transcribe audio using Whisper
                            with open(audio_path, "rb") as audio_file:
                                transcript = openai_client.audio.transcriptions.create(
                                    model="whisper-1",
                                    file=audio_file
                                )
                            text_content = transcript.text
                            st.success("Audio transcribed successfully!")

                else:
                    # Handle website content
                    loader = UnstructuredURLLoader(urls=[url], ssl_verify=False)
                    docs = loader.load()
                    text_content = " ".join(doc.page_content for doc in docs)
                    st.success("Website content fetched successfully!")

            # Summarization step
            if text_content and len(text_content.strip()) > 50:
                st.info("Summarizing content...")
                docs = [Document(page_content=text_content, metadata={})]

                prompt_template = """
                Generate a concise and clear summary of the following text:
                {text}
                """
                prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                summary = chain.run({"input_documents": docs, "text": text_content})

                st.success("Summary generated successfully!")
                st.write(summary)
            else:
                st.error("Could not extract enough content for summarization. Please try another URL.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.write("Please check your API keys, model names, and try again.")
