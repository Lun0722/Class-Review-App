import streamlit as st
from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip
import os
import math

st.set_page_config(page_title="AI 課後複習 App", layout="centered")
st.title("📚 AI 課後複習 App Demo")

st.header("教師上傳文章 / 單字")
article = st.text_area("請輸入文章或單字", height=150)

def estimate_duration(text):
    words = len(text.split())
    return max(5, math.ceil(words / 2.5))

if st.button("生成影片與語音"):
    if not article.strip():
        st.warning("請先輸入文章或單字")
    else:
        audio_file = "lesson_audio.mp3"
        tts = gTTS(text=article, lang="en")
        tts.save(audio_file)
        duration = estimate_duration(article)

        clip = TextClip(
            article, fontsize=40, color="white", size=(1280, 720), method="caption"
        ).set_duration(duration)

        audio_clip = AudioFileClip(audio_file)
        video = clip.set_audio(audio_clip)

        video_file = "lesson_video.mp4"
        video.write_videofile(video_file, fps=24, verbose=False, logger=None)

        st.success("影片與語音生成完成！🎉")
        st.header("學生端播放區")
        st.video(video_file)
        st.audio(audio_file)

def cleanup():
    for f in ["lesson_audio.mp3", "lesson_video.mp4"]:
        if os.path.exists(f):
            os.remove(f)
    st.success("暫存檔案已清理 ✅")

st.button("清理暫存檔案", on_click=cleanup)
