import joblib
import streamlit as st
import pandas as pd


# Load trained model and encoded column names
model = joblib.load("models/tuned_random_forest_model.pkl")
model_columns = joblib.load("models/model_columns.pkl")


# Streamlit app title
st.title("StaySure AI - Hotel Booking Cancellation Prediction")

st.write(
    "This app predicts whether a hotel booking is likely to be cancelled "
    "based on booking details entered by the user."
)


# User inputs
hotel_selected = st.selectbox(
    "Select hotel type",
    ["City Hotel", "Resort Hotel"]
)

lead_time_selected = st.slider(
    "Lead time in days",
    min_value=0,
    max_value=737,
    value=69
)

deposit_type_selected = st.selectbox(
    "Select deposit type",
    ["No Deposit", "Non Refund", "Refundable"]
)

market_segment_selected = st.selectbox(
    "Select market segment",
    [
        "Aviation",
        "Complementary",
        "Corporate",
        "Direct",
        "Groups",
        "Offline TA/TO",
        "Online TA",
        "Undefined"
    ]
)

customer_type_selected = st.selectbox(
    "Select customer type",
    ["Contract", "Group", "Transient", "Transient-Party"]
)

st.subheader("Stay Details")

weekend_nights_selected = st.number_input(
    "Number of weekend nights",
    min_value=0,
    max_value=19,
    value=1
)

week_nights_selected = st.number_input(
    "Number of week nights",
    min_value=0,
    max_value=50,
    value=2
)

st.subheader("Guest Details")

adults_selected = st.number_input(
    "Number of adults",
    min_value=0,
    max_value=55,
    value=2
)

children_selected = st.number_input(
    "Number of children",
    min_value=0,
    max_value=10,
    value=0
)

babies_selected = st.number_input(
    "Number of babies",
    min_value=0,
    max_value=10,
    value=0
)

has_special_request_selected = st.selectbox(
    "Does the booking have any special request?",
    ["No", "Yes"]
)


# Predict button
if st.button("Predict Cancellation"):

    # Feature engineering
    total_nights = weekend_nights_selected + week_nights_selected
    total_guests = adults_selected + children_selected + babies_selected

    if children_selected + babies_selected > 0:
        has_children = 1
    else:
        has_children = 0

    if has_special_request_selected == "Yes":
        has_special_request = 1
    else:
        has_special_request = 0

    # Simple input validation
    if total_guests == 0:
        st.error("Please enter at least one guest for the booking.")

    else:
        # Create input data using the same selected features as the model
        input_data = {
            "hotel": hotel_selected,
            "lead_time": lead_time_selected,
            "deposit_type": deposit_type_selected,
            "market_segment": market_segment_selected,
            "customer_type": customer_type_selected,
            "total_nights": total_nights,
            "total_guests": total_guests,
            "has_children": has_children,
            "has_special_request": has_special_request
        }

        # Convert input data to DataFrame
        df_input = pd.DataFrame([input_data])

        # Encode categorical columns using the same method as model training
        df_input_encoded = pd.get_dummies(
            df_input,
            columns=["hotel", "deposit_type", "market_segment", "customer_type"],
            drop_first=True
        )

        # Match Streamlit input columns to training columns
        df_input_encoded = df_input_encoded.reindex(
            columns=model_columns,
            fill_value=0
        )

        # Predict cancellation
        prediction = model.predict(df_input_encoded)[0]

        if prediction == 1:
            st.warning("Prediction: This booking is likely to be cancelled.")
        else:
            st.success("Prediction: This booking is likely not to be cancelled.")

        st.write("Input summary:")
        st.write(df_input)