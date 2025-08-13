import streamlit as st

st.title("Conversion App")

conversion_type = st.selectbox(
    "Select conversion",
    [
        "Kilometers to Miles",
        "Miles to Kilometers",
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius",
        "Kilograms to Pounds",
        "Pounds to Kilograms",
    ],
)

value = st.number_input("Enter value", value=0.0, step=0.1)

if st.button("Convert"):
    if conversion_type == "Kilometers to Miles":
        result = value * 0.621371
        st.write(f"{value} km = {result:.2f} miles")
    elif conversion_type == "Miles to Kilometers":
        result = value / 0.621371
        st.write(f"{value} miles = {result:.2f} km")
    elif conversion_type == "Celsius to Fahrenheit":
        result = (value * 9 / 5) + 32
        st.write(f"{value} °C = {result:.2f} °F")
    elif conversion_type == "Fahrenheit to Celsius":
        result = (value - 32) * 5 / 9
        st.write(f"{value} °F = {result:.2f} °C")
    elif conversion_type == "Kilograms to Pounds":
        result = value * 2.20462
        st.write(f"{value} kg = {result:.2f} lbs")
    elif conversion_type == "Pounds to Kilograms":
        result = value / 2.20462
        st.write(f"{value} lbs = {result:.2f} kg")
