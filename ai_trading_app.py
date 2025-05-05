import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Memuat file .env untuk mengambil API key secara aman
load_dotenv()

# Mengambil API key dari file .env (gunakan API key terbaru Anda)
openai.api_key = "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"

# Fungsi untuk mendapatkan sinyal trading
def get_trade_signal(symbol):
    prompt = f"Analyze the market for {symbol} and suggest whether to Buy, Sell, or Hold based on current market conditions."
    
    # Memanggil OpenAI API untuk menghasilkan sinyal trading
    response = openai.Completion.create(
        model="text-davinci-003",  # Gunakan model GPT terbaru yang didukung oleh OpenAI
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    
    return response.choices[0].text.strip()

# Menampilkan antarmuka dengan Streamlit
def display_ui():
    st.title("AI Trading Signal System")
    st.header("AI Trading Signal")

    # Pilih simbol trading
    symbol = st.selectbox("Choose a Symbol", ["XAUUSD", "EURUSD", "GBPUSD", "USDJPY"])

    # Tombol untuk mendapatkan sinyal trading dari GPT
    if st.button('Get AI Trading Signal'):
        signal = get_trade_signal(symbol)
        st.write(f"**AI Suggestion for {symbol}:** {signal}")

        # Menampilkan saran dari AI, jika ada
        if "BUY" in signal:
            st.write("AI suggests opening a **BUY** order.")
        elif "SELL" in signal:
            st.write("AI suggests opening a **SELL** order.")
        else:
            st.write("AI suggests **HOLD** the current position.")

    st.sidebar.header("Settings")
    st.sidebar.write("Adjust trading parameters here.")

# Menjalankan aplikasi Streamlit
if __name__ == "__main__":
    display_ui()
