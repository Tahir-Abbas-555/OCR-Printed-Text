import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

def load_model():
    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-printed')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-printed')
    return processor, model

def process_image(image, processor, model):
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text

st.title("Print OCR with TrOCR")

# Load model and processor
processor, model = load_model()

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    with st.spinner("Extracting text..."):
        extracted_text = process_image(image, processor, model)
    
    st.subheader("Extracted Text:")
    st.write(extracted_text)

# Example URL processing
st.write("Or try with an example image:")
default_url = "https://fki.tic.heia-fr.ch/static/img/a01-122-02-00.jpg"
if st.button("Process Example Image"):
    image = Image.open(requests.get(default_url, stream=True).raw).convert("RGB")
    st.image(image, caption="Example Image", use_column_width=True)
    with st.spinner("Extracting text..."):
        extracted_text = process_image(image, processor, model)
    st.subheader("Extracted Text:")
    st.write(extracted_text)
