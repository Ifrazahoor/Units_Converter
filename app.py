import streamlit as st

# Function to convert length units
def convert_length(value, from_unit, to_unit):
    # Conversion factors (relative to meters)
    units_in_meters = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'micrometers': 1e-6,
        'nanometers': 1e-9
    }
    
    # Convert the input value to meters first
    value_in_meters = value * units_in_meters[from_unit]
    
    # Convert from meters to the target unit
    converted_value = value_in_meters / units_in_meters[to_unit]
    
    return converted_value

# Streamlit App

# Customizing page title and layout
st.set_page_config(page_title="Ultimate Unit Converter", page_icon="🔄", layout="wide")

# Title with a custom heading
st.title("Ultimate Unit Converter 🔄")
st.markdown("Convert various length units seamlessly and accurately. Choose your units and see the result instantly.")

# Sidebar for user inputs
st.sidebar.header('Enter Conversion Details')
st.sidebar.markdown("Select the units and input the value for conversion.")

# Adding placeholders to inputs for better UX
value = st.sidebar.number_input('Enter the value to convert', min_value=0.0, help="Enter a positive number.")
from_unit = st.sidebar.selectbox('Convert from', ['meters', 'kilometers', 'centimeters', 'millimeters', 'micrometers', 'nanometers'], help="Select the unit you want to convert from.")
to_unit = st.sidebar.selectbox('Convert to', ['meters', 'kilometers', 'centimeters', 'millimeters', 'micrometers', 'nanometers'], help="Select the unit you want to convert to.")

# Conversion button and result display
if st.sidebar.button('Convert'):
    # Error handling for invalid value
    if value <= 0:
        st.sidebar.warning("Please enter a positive number!")
    else:
        # Call the conversion function
        result = convert_length(value, from_unit, to_unit)
        st.success(f"**Conversion Result:** {value} {from_unit} = {result:.4f} {to_unit}")
        
        # Display result with a simple explanation
        st.write(f"### How It Works:")
        st.write(f"1. The value `{value}` {from_unit} is converted to meters first.")
        st.write(f"2. Then, it's converted to `{to_unit}`.")
        st.write(f"3. The final result is displayed above.")

        # Add some extra visual appeal
        st.markdown("---")
        st.write("Enjoy converting your units effortlessly!")
        
        # Optional: Display a success icon or image to make the result feel like a 'success'
        st.image("https://img.icons8.com/emoji/48/000000/check-mark-emoji.png", width=50)

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ by [Ifra Zahoor]")
