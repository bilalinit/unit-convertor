import streamlit as st
import google.generativeai as genai
import os

# handling gemini api key
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")
except KeyError:
    st.error("Gemini API key not found. Please add it to Streamlit secrets.")
    st.stop()


# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "meters": 1.0,
        "kilometers": 1000.0,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254,
        "nautical miles": 1852.0,
    }
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]


def convert_area(value, from_unit, to_unit):
    area_units = {
        "square meters": 1.0,
        "square kilometers": 1e6,
        "square centimeters": 1e-4,
        "square millimeters": 1e-6,
        "hectares": 10000.0,
        "acres": 4046.86,
        "square miles": 2.59e6,
        "square yards": 0.836127,
        "square feet": 0.092903,
        "square inches": 0.00064516,
    }
    sq_meters = value * area_units[from_unit]
    return sq_meters / area_units[to_unit]


def convert_data_rate(value, from_unit, to_unit):
    data_rate_units = {
        "bits per second": 1.0,
        "kilobits per second": 1000.0,
        "megabits per second": 1e6,
        "gigabits per second": 1e9,
    }
    bps = value * data_rate_units[from_unit]
    return bps / data_rate_units[to_unit]


def convert_digital_storage(value, from_unit, to_unit):
    storage_units = {
        "bytes": 1.0,
        "kilobytes": 1024.0,
        "megabytes": 1024.0**2,
        "gigabytes": 1024.0**3,
        "terabytes": 1024.0**4,
    }
   
    bytes_val = value * storage_units[from_unit]
    return bytes_val / storage_units[to_unit]


def convert_energy(value, from_unit, to_unit):
    energy_units = {
        "joules": 1.0,
        "kilojoules": 1000.0,
        "calories": 4.184,
        "kilocalories": 4184.0,
        "watt-hours": 3600.0,
        "kilowatt-hours": 3.6e6,
    }
    
    joules = value * energy_units[from_unit]
    return joules / energy_units[to_unit]


def convert_frequency(value, from_unit, to_unit):
    frequency_units = {
        "hertz": 1.0,
        "kilohertz": 1000.0,
        "megahertz": 1e6,
        "gigahertz": 1e9,
    }
   
    hertz = value * frequency_units[from_unit]
    return hertz / frequency_units[to_unit]


def convert_fuel_economy(value, from_unit, to_unit):
    fuel_units = {
        "liters per 100 kilometers": 1.0,
        "miles per gallon (US)": 235.215,
        "miles per gallon (UK)": 282.481,
    }
    
    l_per_100km = value * fuel_units[from_unit]
    return l_per_100km / fuel_units[to_unit]


def convert_mass(value, from_unit, to_unit):
    mass_units = {
        "grams": 1.0,
        "kilograms": 1000.0,
        "milligrams": 0.001,
        "micrograms": 1e-6,
        "pounds": 453.592,
        "ounces": 28.3495,
        "stones": 6350.29,
    }
    
    grams = value * mass_units[from_unit]
    return grams / mass_units[to_unit]


def convert_plane_angle(value, from_unit, to_unit):
    angle_units = {
        "degrees": 1.0,
        "radians": 57.2958,
    }

    degrees = value * angle_units[from_unit]
    return degrees / angle_units[to_unit]


def convert_pressure(value, from_unit, to_unit):
    pressure_units = {
        "pascals": 1.0,
        "kilopascals": 1000.0,
        "bars": 1e5,
        "atmospheres": 101325.0,
        "millimeters of mercury": 133.322,
        "pounds per square inch": 6894.76,
    }
  
    pascals = value * pressure_units[from_unit]
    return pascals / pressure_units[to_unit]


def convert_speed(value, from_unit, to_unit):
    speed_units = {
        "meters per second": 1.0,
        "kilometers per hour": 1 / 3.6,  
        "miles per hour": 0.44704,
        "feet per second": 0.3048,
        "knots": 0.514444,
    }
   
    mps = value * speed_units[from_unit]
    return mps / speed_units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9 / 5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5 / 9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9 / 5 + 32
    return value 


def convert_time(value, from_unit, to_unit):
    time_units = {
        "seconds": 1.0,
        "minutes": 60.0,
        "hours": 3600.0,
        "days": 86400.0,
        "weeks": 604800.0,
    }
   
    seconds = value * time_units[from_unit]
    return seconds / time_units[to_unit]


def convert_volume(value, from_unit, to_unit):
    volume_units = {
        "cubic meters": 1.0,
        "cubic kilometers": 1e9,
        "cubic centimeters": 1e-6,
        "cubic millimeters": 1e-9,
        "liters": 0.001,
        "milliliters": 1e-6,
        "gallons (US)": 0.00378541,
        "gallons (UK)": 0.00454609,
        "fluid ounces (US)": 2.95735e-5,
        "fluid ounces (UK)": 2.84131e-5,
    }
    
    cubic_meters = value * volume_units[from_unit]
    return cubic_meters / volume_units[to_unit]


def verify_with_gemini(value, from_unit, to_unit, result):
    """
    Verifies the unit conversion result using the Gemini API.
    """
    prompt = f"""
    I have a unit conversion:
    Value: {value}
    From Unit: {from_unit}
    To Unit: {to_unit}
    Calculated Result: {result}

    Is this conversion accurate?  Respond with only "Accurate" or "Inaccurate".
    Explain your reasoning in one sentence.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error during Gemini API call: {e}"



st.title("Unit Converter with Gemini Verification")
st.sidebar.header("Conversion Options")

#  category
category = st.sidebar.selectbox(
    "Select a category",
    [
        "Length",
        "Area",
        "Data Transfer Rate",
        "Digital Storage",
        "Energy",
        "Frequency",
        "Fuel Economy",
        "Mass",
        "Plane Angle",
        "Pressure",
        "Speed",
        "Temperature",
        "Time",
        "Volume",
    ],
)


value = st.number_input("Enter the value to convert", value=0.0)

#  category condition
if category == "Length":
    from_unit = st.selectbox(
        "From Unit",
        [
            "meters",
            "kilometers",
            "centimeters",
            "millimeters",
            "miles",
            "yards",
            "feet",
            "inches",
            "nautical miles",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "meters",
            "kilometers",
            "centimeters",
            "millimeters",
            "miles",
            "yards",
            "feet",
            "inches",
            "nautical miles",
        ],
    )
    result = convert_length(value, from_unit, to_unit)
elif category == "Area":
    from_unit = st.selectbox(
        "From Unit",
        [
            "square meters",
            "square kilometers",
            "square centimeters",
            "square millimeters",
            "hectares",
            "acres",
            "square miles",
            "square yards",
            "square feet",
            "square inches",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "square meters",
            "square kilometers",
            "square centimeters",
            "square millimeters",
            "hectares",
            "acres",
            "square miles",
            "square yards",
            "square feet",
            "square inches",
        ],
    )
    result = convert_area(value, from_unit, to_unit)
elif category == "Data Transfer Rate":
    from_unit = st.selectbox(
        "From Unit",
        [
            "bits per second",
            "kilobits per second",
            "megabits per second",
            "gigabits per second",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "bits per second",
            "kilobits per second",
            "megabits per second",
            "gigabits per second",
        ],
    )
    result = convert_data_rate(value, from_unit, to_unit)
elif category == "Digital Storage":
    from_unit = st.selectbox(
        "From Unit", ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]
    )
    to_unit = st.selectbox(
        "To Unit", ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]
    )
    result = convert_digital_storage(value, from_unit, to_unit)
elif category == "Energy":
    from_unit = st.selectbox(
        "From Unit",
        [
            "joules",
            "kilojoules",
            "calories",
            "kilocalories",
            "watt-hours",
            "kilowatt-hours",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "joules",
            "kilojoules",
            "calories",
            "kilocalories",
            "watt-hours",
            "kilowatt-hours",
        ],
    )
    result = convert_energy(value, from_unit, to_unit)
elif category == "Frequency":
    from_unit = st.selectbox(
        "From Unit", ["hertz", "kilohertz", "megahertz", "gigahertz"]
    )
    to_unit = st.selectbox(
        "To Unit", ["hertz", "kilohertz", "megahertz", "gigahertz"]
    )
    result = convert_frequency(value, from_unit, to_unit)
elif category == "Fuel Economy":
    from_unit = st.selectbox(
        "From Unit",
        ["liters per 100 kilometers", "miles per gallon (US)", "miles per gallon (UK)"],
    )
    to_unit = st.selectbox(
        "To Unit",
        ["liters per 100 kilometers", "miles per gallon (US)", "miles per gallon (UK)"],
    )
    result = convert_fuel_economy(value, from_unit, to_unit)
elif category == "Mass":
    from_unit = st.selectbox(
        "From Unit",
        ["grams", "kilograms", "milligrams", "micrograms", "pounds", "ounces", "stones"],
    )
    to_unit = st.selectbox(
        "To Unit",
        ["grams", "kilograms", "milligrams", "micrograms", "pounds", "ounces", "stones"],
    )
    result = convert_mass(value, from_unit, to_unit)
elif category == "Plane Angle":
    from_unit = st.selectbox("From Unit", ["degrees", "radians"])
    to_unit = st.selectbox("To Unit", ["degrees", "radians"])
    result = convert_plane_angle(value, from_unit, to_unit)
elif category == "Pressure":
    from_unit = st.selectbox(
        "From Unit",
        [
            "pascals",
            "kilopascals",
            "bars",
            "atmospheres",
            "millimeters of mercury",
            "pounds per square inch",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "pascals",
            "kilopascals",
            "bars",
            "atmospheres",
            "millimeters of mercury",
            "pounds per square inch",
        ],
    )
    result = convert_pressure(value, from_unit, to_unit)
elif category == "Speed":
    from_unit = st.selectbox(
        "From Unit",
        [
            "meters per second",
            "kilometers per hour",
            "miles per hour",
            "feet per second",
            "knots",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "meters per second",
            "kilometers per hour",
            "miles per hour",
            "feet per second",
            "knots",
        ],
    )
    result = convert_speed(value, from_unit, to_unit)
elif category == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    result = convert_temperature(value, from_unit, to_unit)
elif category == "Time":
    from_unit = st.selectbox(
        "From Unit", ["seconds", "minutes", "hours", "days", "weeks"]
    )
    to_unit = st.selectbox(
        "To Unit", ["seconds", "minutes", "hours", "days", "weeks"]
    )
    result = convert_time(value, from_unit, to_unit)
elif category == "Volume":
    from_unit = st.selectbox(
        "From Unit",
        [
            "cubic meters",
            "cubic kilometers",
            "cubic centimeters",
            "cubic millimeters",
            "liters",
            "milliliters",
            "gallons (US)",
            "gallons (UK)",
            "fluid ounces (US)",
            "fluid ounces (UK)",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "cubic meters",
            "cubic kilometers",
            "cubic centimeters",
            "cubic millimeters",
            "liters",
            "milliliters",
            "gallons (US)",
            "gallons (UK)",
            "fluid ounces (US)",
            "fluid ounces (UK)",
        ],
    )
    result = convert_volume(value, from_unit, to_unit)
else:
    result = None  


if result is not None:
    st.write(f"Converted value: {result} {to_unit}")

    # Gemini Verification
    if st.button("Verify with Gemini"):
        with st.spinner("Verifying with Gemini..."):
            gemini_response = verify_with_gemini(
                value, from_unit, to_unit, result
            )
            st.write("Gemini Verification:")
            st.write(gemini_response)
else:
    st.warning("Please select a category to perform the conversion.")
