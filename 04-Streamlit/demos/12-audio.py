"""Audio playback, recording, and uploading without extra media files."""  # This names the three audio actions in the lesson.

import io  # BytesIO lets Python build an in-memory file.
import math  # Math supplies pi and sine for a simple tone.
import struct  # Struct turns numbers into raw audio bytes.
import wave  # Wave writes a standard WAV sound file.

import streamlit as st  # Streamlit supplies audio playback and input widgets.

st.set_page_config(page_title="Audio Demo", page_icon="🎵")  # This chooses the browser-tab name and emoji.
st.title("🎵 Audio")  # This creates the visible lesson title.


@st.cache_data  # The same tone bytes can be reused on every widget rerun.
def make_tone(frequency, duration=0.4, sample_rate=8000):  # Parameters control pitch, seconds, and samples per second.
    buffer = io.BytesIO()  # This empty memory buffer will pretend to be a file.
    with wave.open(buffer, "wb") as wav_file:  # Opening in write-binary mode prepares a WAV container.
        wav_file.setnchannels(1)  # One channel means mono audio.
        wav_file.setsampwidth(2)  # Two bytes per sample means 16-bit sound.
        wav_file.setframerate(sample_rate)  # The sample rate tells the player how quickly to read samples.
        for sample_number in range(int(duration * sample_rate)):  # This loop creates every tiny slice of the tone.
            value = int(12000 * math.sin(2 * math.pi * frequency * sample_number / sample_rate))  # A sine wave makes a smooth beep.
            wav_file.writeframes(struct.pack("<h", value))  # '<h' stores one little-endian signed 16-bit number.
    return buffer.getvalue()  # This returns the finished WAV file as bytes.


frequency = st.slider("Tone frequency (Hz)", min_value=220, max_value=880, value=440, step=10, help="Higher hertz values sound higher.")  # This widget changes the pitch.
st.audio(make_tone(frequency), format="audio/wav", loop=False)  # The audio player receives generated WAV bytes.

recorded = st.audio_input("Record a short message")  # This component asks permission to use the microphone.
if recorded is not None:  # This branch runs after the visitor records something.
    st.audio(recorded)  # The recording object can be played without conversion.
    st.success(f"Recording size: {len(recorded.getvalue()):,} bytes")  # This demonstrates how to inspect uploaded audio bytes.

uploaded = st.file_uploader("Or upload an audio file", type=["wav", "mp3", "ogg"])  # The type list limits the file picker to common audio formats.
if uploaded is not None:  # This branch runs only when a file has been selected.
    st.audio(uploaded)  # Streamlit infers playback information from the uploaded file.

st.caption("`st.audio` plays sound; `st.audio_input` records; `st.file_uploader` accepts an existing file.")  # This one-line summary separates the three jobs.
