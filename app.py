import streamlit as st
import torch
from synthesizer.inference import Synthesizer

# Load the synthesizer model
synthesizer = Synthesizer('pretrained/synthesizer.pt')

# Streamlit app interface
st.title("Voice Cloning App")
text = st.text_area("Enter text here", height=150)

if st.button("Synthesize"):
    if text:
        with st.spinner("Synthesizing..."):
            # Perform synthesis
            embedding = torch.load('your_voice_embedding.pt')
            audio = synthesizer.synthesize_spectrograms([text], [embedding])[0]
            audio = audio.tobytes()
            
            # Save the audio to a file
            with open("output.wav", "wb") as f:
                f.write(audio)
            
            # Play the audio file
            st.audio("output.wav", format="audio/wav")
    else:
        st.warning("Please enter some text to synthesize.")
