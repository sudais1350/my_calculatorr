import streamlit as st



st.set_page_config(page_title="My Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
num1 = st.number_input("enter number 1:", value=0)



num2 = st.number_input("enter number 2:", value=0)



operation = st.selectbox("enter operation?", ["plus (+)", "Minus (-)", "multiply (x)", "divide(/)"])


if st.button("result "):
    result = 0
    if operation == "plus(+)":
        result = num1 + num2
    elif operation == "Minus (-)":
        result = num1 - num2
    elif operation == "multiply(x)":
        result = num1 * num2
    elif operation == "divide (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("0 se divide nahi ho sakta!")
            result = None
    
    if result is not None:
        st.success(f"Jawab hai: {result}")
        



