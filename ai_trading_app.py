import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Memuat file .env untuk mengambil API key secara aman
load_dotenv()

# API key Anda
openai.api_key = "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"  # API key yang Anda berikan

# Fungsi untuk mendapatkan sinyal trading dari GPT-3
def get_trade_signal(symbol):
    prompt = f"Analyze the market for {symbol} and suggest whether to Buy, Sell, or Hold based on current market conditions."
    
    # Memanggil OpenAI API untuk menghasilkan sinyal trading
    response = openai.Completion.create(
        model="text-davinci-003",  # Pilih model GPT terbaru
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
