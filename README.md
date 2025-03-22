# Handwritten OCR with TrOCR

This is a Streamlit web application that uses the Microsoft TrOCR model to perform Optical Character Recognition (OCR) on printed or handwritten images. Users can upload an image or process an example image to extract text using a Transformer-based deep learning model.

## Features
- Upload an image (JPG, PNG, JPEG) to extract text.
- Process a sample image from a predefined URL.
- View extracted text directly on the web interface.

## Installation
To run this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/streamlit-trocr.git
cd streamlit-trocr
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required dependencies:
```bash
pip install streamlit transformers pillow torch requests
```

### 3. Run the Streamlit App
```bash
streamlit run app.py
```

## Dependencies
- `streamlit` for the web interface
- `transformers` for TrOCR processing
- `Pillow` for image handling
- `torch` for model execution
- `requests` for fetching images from URLs

## Usage
1. Open the web application in your browser.
2. Upload an image or click the "Process Example Image" button.
3. The extracted text will be displayed on the screen.

## Model Details
This application uses **Microsoft's TrOCR model (`microsoft/trocr-base-printed`)**, which is a Vision Encoder-Decoder model trained for OCR tasks.

## Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

---
**Author:** Tahir Abbas Shaikh

