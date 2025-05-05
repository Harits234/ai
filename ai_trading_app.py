
import streamlit as st
import openai

# Inisialisasi OpenAI API dengan kunci API Anda
openai.api_key = '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'

# Fungsi untuk mendapatkan sinyal trading dari ChatGPT
def get_trade_signal(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Pilih model GPT yang sesuai
        prompt=prompt,
        max_tokens=100,
        temperature=0.7  # Nilai 0.7 memberikan tingkat variasi yang lebih tinggi dalam respons
    )
    message = response.choices[0].text.strip()
    return message

# Fungsi untuk memproses sinyal trading
def process_signal(symbol):
    prompt = f"Please analyze the market for {symbol} and suggest whether to Buy, Sell, or Hold based on the current market conditions."
    signal = get_trade_signal(prompt)
    return signal

# Tampilan UI dengan Streamlit
def display_ui():
    st.title("AI Trading Signal System")
    st.header("AI Trading Signal")

    # Pilih simbol trading
    symbol = st.selectbox("Choose a Symbol", ["XAUUSD", "EURUSD", "GBPUSD", "USDJPY"])

    # Tombol untuk mendapatkan sinyal trading dari ChatGPT
    if st.button('Get AI Trading Signal'):
        signal = process_signal(symbol)
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
