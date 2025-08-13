import streamlit as st

st.title('Unit Converter')

conversion_types = ['Length', 'Weight', 'Temperature']
category = st.selectbox('Conversion type', conversion_types)

if category == 'Length':
    units = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'miles': 1609.34,
        'feet': 0.3048,
    }
    value = st.number_input('Value', value=0.0)
    from_unit = st.selectbox('From', list(units.keys()))
    to_unit = st.selectbox('To', list(units.keys()))
    converted = value * units[from_unit] / units[to_unit]
    st.write(f"{value} {from_unit} = {converted} {to_unit}")

elif category == 'Weight':
    units = {
        'kilograms': 1.0,
        'grams': 0.001,
        'pounds': 0.453592,
        'ounces': 0.0283495,
    }
    value = st.number_input('Value', value=0.0)
    from_unit = st.selectbox('From', list(units.keys()))
    to_unit = st.selectbox('To', list(units.keys()))
    converted = value * units[from_unit] / units[to_unit]
    st.write(f"{value} {from_unit} = {converted} {to_unit}")

elif category == 'Temperature':
    def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
        if from_unit == to_unit:
            return value
        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                return value * 9.0 / 5.0 + 32.0
            if to_unit == 'Kelvin':
                return value + 273.15
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                return (value - 32.0) * 5.0 / 9.0
            if to_unit == 'Kelvin':
                return (value - 32.0) * 5.0 / 9.0 + 273.15
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                return value - 273.15
            if to_unit == 'Fahrenheit':
                return (value - 273.15) * 9.0 / 5.0 + 32.0
        raise ValueError('Unsupported temperature conversion')

    units = ['Celsius', 'Fahrenheit', 'Kelvin']
    value = st.number_input('Value', value=0.0)
    from_unit = st.selectbox('From', units)
    to_unit = st.selectbox('To', units)
    converted = convert_temperature(value, from_unit, to_unit)
    st.write(f"{value} {from_unit} = {converted} {to_unit}")

st.caption('Built with Streamlit')
