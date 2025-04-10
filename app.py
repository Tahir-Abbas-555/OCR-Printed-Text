from datetime import datetime
import io
import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

def load_model():
    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-printed')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-printed')
    return processor, model

def recognize_text(image, processor, model):
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text

# Sidebar info with custom profile section
st.sidebar.title("ℹ️ About")
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <style>
        .custom-sidebar {
            display: flex;
            flex-direction: column;
            align-items: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            width: 650px;
            padding: 10px;
        }
        .profile-container {
            display: flex;
            flex-direction: row;
            align-items: flex-start;
            width: 100%;
        }
        .profile-image {
            width: 200px;
            height: auto;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
            margin-right: 15px;
        }
        .profile-details {
            font-size: 14px;
            width: 100%;
        }
        .profile-details h3 {
            margin: 0 0 10px;
            font-size: 18px;
            color: #333;
        }
        .profile-details p {
            margin: 10px 0;
            display: flex;
            align-items: center;
        }
        .profile-details a {
            text-decoration: none;
            color: #1a73e8;
        }
        .profile-details a:hover {
            text-decoration: underline;
        }
        .icon-img {
            width: 18px;
            height: 18px;
            margin-right: 6px;
        }
    </style>

    <div class="custom-sidebar">
        <div class="profile-container">
            <img class="profile-image" src="https://res.cloudinary.com/dwhfxqolu/image/upload/v1744014185/pnhnaejyt3udwalrmnhz.jpg" alt="Profile Image">
            <div class="profile-details">
                <h3>👨‍💻 Developed by:<br> Tahir Abbas Shaikh</h3>
                <p>
                    <img class="icon-img" src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Gmail">
                    <strong>Email:</strong> <a href="mailto:tahirabbasshaikh555@gmail.com">tahirabbasshaikh555@gmail.com</a>
                </p>
                <p>📍 <strong>Location:</strong> Sukkur, Sindh, Pakistan</p>
                <p>
                    <img class="icon-img" src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png" alt="GitHub">
                    <strong>GitHub:</strong> <a href="https://github.com/Tahir-Abbas-555" target="_blank">Tahir-Abbas-555</a>
                </p>
                <p>
                    <img class="icon-img" src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="HuggingFace">
                    <strong>HuggingFace:</strong> <a href="https://huggingface.co/Tahir5" target="_blank">Tahir5</a>
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

def display_header():
    st.markdown(
        """
        <style>
            .title {
                font-size: 2.5em;
                font-weight: 700;
                color: #4a90e2;
                text-align: center;
                margin-bottom: 20px;
            }
            .caption {
                text-align: center;
                font-style: italic;
                color: #666;
            }
            .stButton>button {
                width: 100%;
                padding: 0.75rem;
                border-radius: 0.5rem;
                font-weight: 600;
            }
        </style>
        <div class="title">📝 Print OCR with TrOCR</div>
        """,
        unsafe_allow_html=True
    )

def main():
    display_header()

    processor, model = load_model()

    tab1, tab2 = st.tabs(["📤 Upload Image", "🌐 Enter Image URL"])

    image = None

    with tab1:
        uploaded_file = st.file_uploader("Upload a Printed Text image", type=["png", "jpg", "jpeg"])
        if uploaded_file:
            try:
                image = Image.open(uploaded_file).convert("RGB")
            except Exception as e:
                st.error(f"Error loading uploaded file: {e}")
    
    with tab2:
        image_url = st.text_input("Paste image URL here")
        if image_url:
            try:
                response = requests.get(image_url, stream=True, timeout=5)
                response.raise_for_status()
                image = Image.open(response.raw).convert("RGB")
            except Exception as e:
                st.error(f"Error loading image from URL: {e}")

    if image is not None:
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image(image, caption="🖼️ Input Image", use_column_width=True)

        with col2:
            if st.button("🔍 Recognize Pricted Text"):
                with st.spinner("Processing... Please wait."):
                    try:
                        text = recognize_text(image, processor, model)
                        st.success("✅ Text Recognized Successfully!")
                        st.text_area("📜 Recognized Text", value=text, height=200)

                        buffer = io.StringIO()
                        buffer.write(text)
                        st.download_button(
                            label="📥 Download Recognized Text",
                            data=buffer.getvalue(),
                            file_name=f"recognized_text_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                            mime="text/plain"
                        )
                    except Exception as e:
                        st.error(f"Recognition failed: {e}")
    else:
        st.info("Please upload an image or paste a URL to begin.")

if __name__ == "__main__":
    main()
