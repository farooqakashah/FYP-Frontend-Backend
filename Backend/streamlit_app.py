import os
import io
import time
import threading
import queue

import numpy as np
import soundfile as sf
import streamlit as st

import config
import stt
import translate
import tts


st.set_page_config(
    page_title="AI Agriculture Assistant |  اے آئی زرعی معاون",
    page_icon="",
    layout="wide",
)

# Custom CSS for greenish theme and text display
st.markdown("""
    <style>
    /* Main background - greenish theme */
    .stApp {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 50%, #a5d6a7 100%);
    }
    
    /* Main content area */
    .main .block-container {
        background-color: #f1f8e9;
        padding: 2rem;
        border-radius: 10px;
    }
    
    /* Urdu text styling - simple white box with black text */
    .urdu-text {
        font-family: 'Noto Nastaliq Urdu', 'Jameel Noori Nastaleeq', 'Al Qalam Taj Nastaleeq', 'Nafees Web Naskh', Arial, sans-serif;
        font-size: 24px !important;
        line-height: 1.8;
        direction: rtl;
        text-align: right;
        padding: 20px;
        background: #ffffff;
        color: #000000;
        border-radius: 8px;
        border: 1px solid #c8e6c9;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    
    /* LTR text styling - simple white box with black text */
    .ltr-text {
        font-family: Arial, sans-serif;
        font-size: 24px !important;
        line-height: 1.8;
        direction: ltr;
        text-align: left;
        padding: 20px;
        background: #ffffff;
        color: #000000;
        border-radius: 8px;
        border: 1px solid #c8e6c9;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        font-family: 'Noto Nastaliq Urdu', 'Jameel Noori Nastaleeq', 'Al Qalam Taj Nastaleeq', 'Nafees Web Naskh', Arial, sans-serif !important;
        font-size: 22px !important;
        line-height: 1.8 !important;
        direction: rtl !important;
        text-align: right !important;
        padding: 15px !important;
        background: #ffffff !important;
        color: #000000 !important;
    }
    
    /* Section headers */
    h3, h4 {
        color: #2e7d32;
        margin-top: 20px;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        transition: all 0.3s;
        background-color: #4caf50;
        color: white;
    }
    
    .stButton > button:hover {
        background-color: #45a049;
    }
    
    /* Recording status indicator */
    .recording-status {
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        font-weight: bold;
        text-align: center;
    }
    
    .recording-active {
        background-color: #ff4444;
        color: white;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    /* Info boxes */
    .stInfo {
        background-color: #e8f5e9;
        border-left: 4px solid #4caf50;
    }
    
    /* Success messages */
    .stSuccess {
        background-color: #c8e6c9;
    }
    </style>
""", unsafe_allow_html=True)


# Recording functions removed due to system audio dependency


def main() -> None:
    st.title("AI Agriculture Assistant | اے آئی زرعی معاون")
    st.markdown(
        "Local **Whisper** (STT) + **Gemini 2.5 Flash** (translation) + **Google TTS** (TTS)."
    )

    # Sidebar configuration
    st.sidebar.header("Settings")
    language_options = ["urdu", "english", "punjabi", "sindhi", "pashto"]
    default_index = language_options.index(config.TARGET_LANGUAGE) if config.TARGET_LANGUAGE in language_options else 0
    target_lang = st.sidebar.selectbox("Target language", language_options, index=default_index)

    tab_upload, = st.tabs(["Upload Audio File"])

    # Microphone tab removed (system audio not supported in this environment)

    with tab_upload:
        st.subheader("Upload Audio File")
        uploaded_file = st.file_uploader("Upload audio file (WAV recommended)", type=["wav", "mp3", "m4a"])

        if uploaded_file is not None:
            # Save uploaded audio to temp path
            temp_path = config.TEMP_INPUT_WAV_PATH
            # Read file-like into bytes then write out
            raw = uploaded_file.read()
            with open(temp_path, "wb") as f:
                f.write(raw)

            st.markdown("#### Input Audio")
            st.audio(raw)
            
            # Initialize processing state for upload tab
            if 'upload_processing_step' not in st.session_state:
                st.session_state.upload_processing_step = None
            
            # Process audio step by step
            if st.button(" Process Uploaded Audio", type="primary"):
                # Clear previous results when starting new processing
                st.session_state.upload_processing_step = None
                if 'upload_transcribed_text' in st.session_state:
                    del st.session_state.upload_transcribed_text
                if 'upload_translated_text' in st.session_state:
                    del st.session_state.upload_translated_text
                if 'upload_translated_text_display' in st.session_state:
                    del st.session_state.upload_translated_text_display
                if 'upload_translated_text_audio' in st.session_state:
                    del st.session_state.upload_translated_text_audio
                if 'upload_output_audio_path' in st.session_state:
                    del st.session_state.upload_output_audio_path
                st.session_state.upload_processing_step = 'transcribing'
                st.rerun()
            
            # Step 1: Transcribing
            if st.session_state.upload_processing_step == 'transcribing':
                with st.spinner(" Transcribing audio..."):
                    text, detected_lang_code = stt.speech_to_text(temp_path)
                    detected_lang_name = stt.map_whisper_lang_to_name(detected_lang_code)
                    
                    # Store in session state for upload tab
                    st.session_state.upload_detected_lang = detected_lang_name
                    st.session_state.upload_detected_lang_code = detected_lang_code
                    st.session_state.upload_transcribed_text = text
                    st.session_state.upload_processing_step = 'translating'
                    st.rerun()
            
            # Step 2: Translation (only if transcription is done)
            if st.session_state.upload_processing_step == 'translating' and 'upload_transcribed_text' in st.session_state:
                with st.spinner(" Translating text..."):
                    # Two-step pipeline handles Sindhi/Punjabi/Pashto internally.
                    # Output is always correct Arabic script — use same text for display and TTS.
                    translated = translate.translate_text(st.session_state.upload_transcribed_text, target_lang=target_lang)
                    st.session_state.upload_translated_text_display = translated
                    st.session_state.upload_translated_text_audio = translated
                    st.session_state.upload_processing_step = 'synthesizing'
                    st.rerun()
            
            # Step 3: TTS (only if translation is done)
            if (
                st.session_state.upload_processing_step == 'synthesizing'
                and 'upload_translated_text_audio' in st.session_state
                and st.session_state.upload_translated_text_audio
            ):
                with st.spinner(" Synthesizing speech..."):
                    out_path = tts.text_to_speech(st.session_state.upload_translated_text_audio, lang=target_lang, output_path=config.OUTPUT_WAV_PATH)
                    st.session_state.upload_output_audio_path = out_path
                    st.session_state.upload_processing_step = 'complete'
                    st.rerun()
            
            # Display results incrementally if available
            if 'upload_transcribed_text' in st.session_state and st.session_state.upload_transcribed_text:
                st.markdown("---")
                st.markdown("###  Results")
                
                # Step 1: Show transcribed text
                st.markdown("####  Step 1: Transcribed Text")
                st.write(f"**Detected Language:** {st.session_state.upload_detected_lang} (`{st.session_state.upload_detected_lang_code}`)")
                
                transcribed_display = st.session_state.upload_transcribed_text
                st.markdown(
                    f'<div class="urdu-text" dir="rtl">{transcribed_display}</div>',
                    unsafe_allow_html=True
                )
                
                # Step 2: Show translated text (if available)
                if 'upload_translated_text_display' in st.session_state and st.session_state.upload_translated_text_display:
                    st.markdown("####  Step 2: Translated Text")
                    translated_display = st.session_state.upload_translated_text_display
                    # RTL box for all Arabic-script languages; LTR only for English
                    if target_lang in ("urdu", "punjabi", "sindhi", "pashto"):
                        st.markdown(
                            f'<div class="urdu-text" dir="rtl">{translated_display}</div>',
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            f'<div class="ltr-text" dir="ltr">{translated_display}</div>',
                            unsafe_allow_html=True
                        )
                    
                    # Step 3: Show output audio (if available)
                    if 'upload_output_audio_path' in st.session_state and os.path.exists(st.session_state.upload_output_audio_path):
                        st.markdown("####  Step 3: Output Audio")
                        with open(st.session_state.upload_output_audio_path, "rb") as f:
                            out_bytes = f.read()
                        st.audio(out_bytes, format="audio/wav")


if __name__ == "__main__":
    main()


