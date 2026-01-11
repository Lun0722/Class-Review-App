import streamlit as st
from gtts import gTTS
import os
import base64

st.set_page_config(page_title="EIE Institute Class Review", layout="centered")
st.title("📚 EIE Institute Class Review")

# ----------------------------
# Mobile-safe audio player
# ----------------------------
def mobile_audio_player(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()

    audio_html = f"""
    <audio controls style="width:100%">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# ----------------------------
# Input
# ----------------------------
text = st.text_area("Enter your article or vocabulary here", height=150)

if st.button("Generate Audio"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        audio_file = "lesson_audio.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(audio_file)

        st.success("Audio generated successfully 🎉")

        # ▶ Online Play (Base64)
        st.subheader("▶️ Play Online")
        mobile_audio_player(audio_file)

        # ⬇ True file download
        st.subheader("⬇ Download")
        with open(audio_file, "rb") as f:
            st.download_button(
                label="Download MP3",
                data=f.read(),   # important: raw bytes
                file_name="EIE_Lesson.mp3",
                mime="audio/mpeg"
            )

# ----------------------------
# Cleanup
# ----------------------------
if st.button("Clear Audio"):
    if os.path.exists("lesson_audio.mp3"):
        os.remove("lesson_audio.mp3")
        st.success("Audio file cleared.")
