import streamlit as st
from streamlit_webrtc import webrtc_streamer , VideoTransformerBase

import cv2
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return img


webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)