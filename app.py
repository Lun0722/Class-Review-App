import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="EIE Institute Class Review", layout="centered")
st.title("📚 EIE Institute Class Review")

text = st.text_area("Enter your article or vocabulary here", height=150)

if st.button("Generate Audio"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        audio_file = "lesson_audio.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(audio_file)

        st.success("Audio generated successfully 🎉")

        # 播放
        st.audio(audio_file, format="audio/mp3")

        # 真正的下載按鈕
        with open(audio_file, "rb") as file:
            st.download_button(
                label="⬇️ Download MP3",
                data=file,
                file_name="lesson_audio.mp3",
                mime="audio/mpeg"
            )

# 清除檔案
if st.button("Clear Audio"):
    if os.path.exists("lesson_audio.mp3"):
        os.remove("lesson_audio.mp3")
        st.success("Audio file cleared.")
