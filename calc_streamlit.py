import streamlit as st
from PIL import Image

logo_img = Image.open("calc_image.jpg")
st.set_page_config(page_title="Calculator",page_icon=logo_img, layout="centered")


#text
st.title("Simple Calculator")
st.header("Perform basic arithmetic operations")

#uset input widjet
num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")
operation = st.selectbox("Select Operation", ["+","-","*","/","%"])

if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            result = "Error: Division by zero"
    
    st.success(f"Result: {result}") 




