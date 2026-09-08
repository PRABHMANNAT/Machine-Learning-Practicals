"""Image, video, and camera components in one small media playground."""  # This file-level note names the three examples.

from pathlib import Path  # Path builds a reliable route to the local image asset.

import streamlit as st  # Streamlit displays media and creates the camera widget.

st.set_page_config(page_title="Images and Video", page_icon="🎬")  # This configures the browser tab.
st.title("🎬 Images & video")  # This shows the lesson heading.

asset_path = Path(__file__).resolve().parents[1] / "assets" / "streamlit_learning.svg"  # This finds the SVG no matter which working directory launches the app.
image_tab, video_tab, camera_tab = st.tabs(["Image", "Video", "Camera"])  # Tabs keep three media components organized.

with image_tab:  # The following indented elements live in the Image tab.
    st.image(str(asset_path), caption="A local SVG learning map", width="stretch")  # `caption` adds a label and `width` fills the tab.
with video_tab:  # The following indented elements live in the Video tab.
    video_url = "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"  # This public sample URL avoids storing a large movie in the repository.
    st.video(video_url, start_time=0, loop=False, autoplay=False, muted=True)  # These parameters control where playback starts and how it behaves.
    st.caption("The browser fetches this sample video, so this tab needs internet access.")  # This sets an honest expectation for offline learners.
with camera_tab:  # The following indented elements live in the Camera tab.
    photo = st.camera_input("Take a practice photo", help="Your browser will ask before using the camera.")  # This asks the browser for a still image only after permission.
    if photo is not None:  # This branch runs only after a picture has been captured.
        st.image(photo, caption="Your captured image", width=350)  # The uploaded image-like object can be shown directly.
        st.success(f"Captured {len(photo.getvalue()):,} bytes.")  # This reports the file size to demonstrate reading uploaded bytes.

st.info("Useful parameters: `caption`, `width`, `start_time`, `loop`, `autoplay`, and `muted`.")  # This revises the main media options in one place.
