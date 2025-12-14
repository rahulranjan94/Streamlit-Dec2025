import streamlit as st
import pandas as pd


cars_df = pd.read_csv("cars24-car-price.csv")
st.title("Car Price Analysis")
st.header("Dataset Overview")
st.dataframe(cars_df.head())

# save
# with open('model.pkl','wb') as f:
#    pickle.dump(clf,f)

# load
import pickle

with open("car_pred_model", "rb") as file:
    model = pickle.load(file)

print("model loaded successfully")

st.header("Car Price Prediction")
st.write("Enter the details of the car to predict its price")

col1, col2 = st.columns(2)
with col1:
    fuel_type = st.selectbox("Select the fuel type", ["Diesel","Petrol","CNG","LPR","Electric"])
    engine = st.slider("Set the Engine Power",500,5000,step=100)

with col2:
    transmission_type = st.selectbox("Select the transmission type", ["Manual","Automatic"])
    seats= st.selectbox("Enter the number of seats", [4,5,7,9,11])

## Encoding categorical features
## Use the same encoding scheme applied during model training

encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

if st.button("Predict Price"):
    st.write("Predicting.....")

    # Convert the selected fuel type (categorical value) into its numerical encoded form
    # using the same encoding dictionary that was applied during model training
    encoded_fuel_type = encode_dict["fuel_type"][fuel_type]

    # Convert the selected transmission type (categorical value) into its numerical encoded form
    # to ensure consistency with the trained machine learning model
    encoded_transmission_type = encode_dict["transmission_type"][transmission_type]

    # Create the input data in the exact order and format expected by the trained model
    # All values are placed inside a nested list because the model expects a 2D array
    input_data = [[
        2012.0,                     # Year of manufacture of the car
        2,                          # Number of previous owners
        120000,                     # Total distance driven (in kilometers)
        encoded_fuel_type,          # Encoded value of the fuel type
        encoded_transmission_type,  # Encoded value of the transmission type
        19.7,                       # Mileage of the car (km/l)
        engine,                     # Engine capacity (in CC)
        46.3,                       # Maximum power of the car (in bhp)
        seats                       # Number of seats in the car
    ]]

    # Use the trained machine learning model to predict the car price
    # The result is returned as an array, even for a single prediction
    price = model.predict(input_data)

    # Display the predicted price on the Streamlit web interface
    # The price is formatted to two decimal places and shown in Lakhs
    st.header(f"Predicted Price: Rs {price[0]:.2f} Lakhs")
