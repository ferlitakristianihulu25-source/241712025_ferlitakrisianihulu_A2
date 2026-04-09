import streamlit as st
import torch
from PIL import Image
from torchvision import transforms

# Judul Website
st.title("🐾 Animal Classifier AI - Ferlita")

# Fungsi Load Model (Sesuaikan dengan arsitektur modelmu)
@st.cache_resource
def load_model():
    model = ModelAnda() # Ganti dengan nama kelas modelmu
    model.load_state_dict(torch.load('animal_model.pth', map_location='cpu'))
    model.eval()
    return model

# Input Gambar
uploaded_file = st.file_uploader("Upload gambar hewan (Kucing, Anjing, atau Hewan Liar)", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar yang diunggah', use_column_width=True)
    
    # Prediksi (Sederhana)
    st.write("Sedang menganalisis...")
    # (Di sini nanti tambahkan logika transform dan model(image))
    st.success("Hasil Prediksi: Kucing! (Contoh)")