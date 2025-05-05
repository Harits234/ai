import requests
import streamlit as st
from dotenv import load_dotenv
import os

# Memuat file .env untuk mengambil API key secara aman
load_dotenv()

# Mengambil API key DeepSeek dari file .env
DEEPSEEK_API_KEY = os.getenv("sk-6b255993d4a9416e8f72cfd717daf43d")  # API key DeepSeek

# Fungsi untuk mendapatkan sinyal trading dari DeepSeek
def get_trade_signal(symbol):
    url = "https://platform.deepseek.com/api_keys"  # URL API DeepSeek (Contoh, pastikan URL benar)
    
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",  # Header untuk API key
        "Content-Type": "application/json"
    }
    
    payload = {
        "symbol": symbol,
        "timeframe": "5m",  # Sesuaikan dengan timeframe yang Anda pilih
        "signal_type": "trading"  # Tipe sinyal yang Anda butuhkan (bisa jadi 'buy', 'sell', 'hold')
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['forecast']  # Asumsi bahwa response mengembalikan sinyal dalam key 'forecast'
    else:
        return "Error: Unable to fetch data from DeepSeek."

# Menampilkan antarmuka dengan Streamlit
def display_ui():
    st.title("AI Trading Signal System")
    st.header("AI Trading Signal")

    # Pilih simbol trading
    symbol = st.selectbox("Choose a Symbol", ["XAUUSD", "EURUSD", "GBPUSD", "USDJPY"])

    # Tombol untuk mendapatkan sinyal trading dari DeepSeek
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
