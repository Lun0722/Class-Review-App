import streamlit as st
from gtts import gTTS
import os

# Set Streamlit page config
st.set_page_config(page_title="EIE Institute Class Review", layout="centered")
st.title("📚 EIE Institute Class Review")

# -------- Text input --------
text = st.text_area("Enter your article or vocabulary here", height=150)

# -------- Generate audio --------
if st.button("Generate Audio"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        audio_file = "lesson_audio.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(audio_file)

        st.success("Audio has been generated successfully! 🎉")
        st.audio(audio_file, format="audio/mp3")

# -------- Clean up --------
if st.button("Clear Audio File"):
    if os.path.exists("lesson_audio.mp3"):
        os.remove("lesson_audio.mp3")
        st.success("Audio file has been cleared ✅")
    else:
        st.info("No audio file to clear.")
