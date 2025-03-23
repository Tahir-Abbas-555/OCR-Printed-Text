# Print OCR with TrOCR

This is a **Streamlit** web application that uses **Microsoft TrOCR** to perform Optical Character Recognition (OCR) on printed text images. Users can upload an image or process an example image to extract text using a Transformer-based deep learning model.

## 🚀 Live Demo  
[Check out the live demo here!](https://huggingface.co/spaces/Tahir5/Printed-Text-OCR)  

## ✨ Features  
- 📸 **Upload an Image** (JPG, PNG, JPEG) to extract text.  
- 🔄 **Process an Example Image** with a predefined URL.  
- 📝 **View Extracted Text** directly on the web interface.  

## 🛠 Installation  

To run this project locally, follow these steps:  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/streamlit-trocr.git
cd streamlit-trocr
```

### 2️⃣ Install Dependencies  
Ensure you have Python installed, then install the required dependencies:  
```bash
pip install streamlit transformers pillow torch requests
```

### 3️⃣ Run the Streamlit App  
```bash
streamlit run app.py
```

## 📌 Dependencies  
- **`streamlit`** – for the web interface  
- **`transformers`** – for TrOCR processing  
- **`Pillow`** – for image handling  
- **`torch`** – for deep learning model execution  
- **`requests`** – for fetching images from URLs  

## 🖥 Usage  
1️⃣ Open the web application in your browser.  
2️⃣ Upload an image or click **"Process Example Image"**.  
3️⃣ The extracted text will be displayed on the screen.  

## 🧠 Model Details  
This application uses **Microsoft's TrOCR model (`microsoft/trocr-base-printed`)**, a Vision Encoder-Decoder model trained specifically for OCR tasks.

## 🤝 Contributing  
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## 📜 License  
This project is licensed under the **MIT License**.

---

**👨‍💻 Author:** Tahir Abbas Shaikh  

Let me know if you need any modifications! 🚀
