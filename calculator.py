import streamlit as st

st.title("My Calculator")

num1 = st.number_input("enter number 1:", value=0.0)
num2 = st.number_input("enter number 2:", value=0.0)

operation = st.selectbox("operation select karo:", ["plus(+)", "Minus (-)", "multiply(x)", "divide (/)"])

result = None

if st.button("Result dekho"):
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

    if result is not None:
        st.success(f"Jawab hai: {result}")
