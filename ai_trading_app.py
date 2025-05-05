
import streamlit as st
import openai
import MetaTrader5 as mt5

# Initialize OpenAI API
openai.api_key = 'your-openai-api-key'

# Function to get trade signal from ChatGPT
def get_trade_signal(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use appropriate engine
        prompt=prompt,
        max_tokens=100
    )
    message = response.choices[0].text.strip()
    return message

# Initialize MetaTrader5 connection
def initialize_mt5():
    if not mt5.initialize():
        print("MetaTrader 5 initialization failed")
        mt5.shutdown()
    else:
        print("MetaTrader 5 initialized successfully")

# Function to open trade in MT5
def open_trade(symbol, order_type, volume, price, sl, tp):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 234000,
        "comment": "Streamlit AI Trading",
        "type_filling": mt5.ORDER_FILLING_IOC,
        "type_time": mt5.ORDER_TIME_GTC
    }
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Error executing trade: {result.retcode}")
    else:
        print("Trade executed successfully")

# Streamlit user interface
def display_ui():
    st.title("AI Trading Super Canggih")
    st.header("AI Trading Signal")
    
    symbol = st.selectbox("Choose Symbol", ["XAUUSD", "EURUSD", "GBPUSD"])
    
    if st.button('Get AI Trading Signal'):
        prompt = f"Analyze the market for {symbol} and suggest a buy or sell signal."
        signal = get_trade_signal(prompt)
        st.write("AI Suggestion:", signal)
        
        if "BUY" in signal:
            price = SymbolInfoDouble(symbol, SYMBOL_ASK)
            sl = price - 10 * _Point  # Stop Loss
            tp = price + 20 * _Point  # Take Profit
            open_trade(symbol, mt5.ORDER_TYPE_BUY, 0.1, price, sl, tp)
        elif "SELL" in signal:
            price = SymbolInfoDouble(symbol, SYMBOL_BID)
            sl = price + 10 * _Point  # Stop Loss
            tp = price - 20 * _Point  # Take Profit
            open_trade(symbol, mt5.ORDER_TYPE_SELL, 0.1, price, sl, tp)
    
    st.header("Market Overview")
    st.write("Real-time market data can be displayed here using MT5 API.")
    
    st.sidebar.header("Settings")
    st.sidebar.write("Adjust trading parameters here.")

if __name__ == "__main__":
    display_ui()
    