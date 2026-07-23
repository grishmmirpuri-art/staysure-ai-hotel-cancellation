import joblib
import pandas as pd
import streamlit as st


# Load the trained model and the encoded column names used during training.
@st.cache_resource
def load_model_files():
    trained_model = joblib.load("models/tuned_random_forest_model.pkl")
    trained_columns = joblib.load("models/model_columns.pkl")
    return trained_model, trained_columns


model, model_columns = load_model_files()


# Categories used when the model was trained.
# "Undefined" remains here only so that one-hot encoding matches the training
# structure. It is deliberately excluded from the user-facing dropdown.
HOTEL_CATEGORIES = ["City Hotel", "Resort Hotel"]
DEPOSIT_CATEGORIES = ["No Deposit", "Non Refund", "Refundable"]
MARKET_SEGMENT_CATEGORIES = [
    "Aviation",
    "Complementary",
    "Corporate",
    "Direct",
    "Groups",
    "Offline TA/TO",
    "Online TA",
    "Undefined",
]
CUSTOMER_TYPE_CATEGORIES = [
    "Contract",
    "Group",
    "Transient",
    "Transient-Party",
]


# Descriptions shown directly below selected dropdown options.
DEPOSIT_DESCRIPTIONS = {
    "No Deposit": "No deposit was recorded for the booking.",
    "Non Refund": "A non-refundable deposit arrangement was recorded.",
    "Refundable": "A refundable deposit arrangement was recorded.",
}

MARKET_SEGMENT_DESCRIPTIONS = {
    "Aviation": "Booking associated with an airline or aviation organisation.",
    "Complementary": "A complimentary booking provided without the usual room charge.",
    "Corporate": "Booking made through a company or corporate account.",
    "Direct": "Booking made directly with the hotel.",
    "Groups": "Booking made for an organised group.",
    "Offline TA/TO": "Booking made through an offline travel agency or tour operator.",
    "Online TA": "Booking made through an online travel agency.",
}

CUSTOMER_TYPE_DESCRIPTIONS = {
    "Contract": "Booking made under a contract or negotiated agreement.",
    "Group": "Customer travelling as part of an organised group.",
    "Transient": "An individual booking that is not part of a group or contract.",
    "Transient-Party": "An individual booking linked to other bookings travelling together.",
}


# Streamlit page content.
st.title("StaySure AI – Hotel Booking Cancellation Risk Predictor")

st.write(
    "This app predicts whether a hotel booking is likely to be cancelled "
    "based on the booking details entered by the user."
)

st.caption(
    "Select the category that most closely matches the booking. The app "
    "supports the categories available in the training dataset."
)


# User inputs. Streamlit reruns the page whenever a selection changes,
# allowing each description to update immediately.
hotel_selected = st.selectbox(
    "Hotel type",
    HOTEL_CATEGORIES,
)

lead_time_selected = st.slider(
    "Lead time in days",
    min_value=0,
    max_value=737,
    value=69,
)
st.caption(
    "Number of days between the booking date and the planned arrival date."
)

deposit_type_selected = st.selectbox(
    "Deposit type",
    DEPOSIT_CATEGORIES,
)
st.caption(DEPOSIT_DESCRIPTIONS[deposit_type_selected])

market_segment_selected = st.selectbox(
    "Market segment",
    [
        "Aviation",
        "Complementary",
        "Corporate",
        "Direct",
        "Groups",
        "Offline TA/TO",
        "Online TA",
    ],
)
st.caption(MARKET_SEGMENT_DESCRIPTIONS[market_segment_selected])

customer_type_selected = st.selectbox(
    "Customer type",
    CUSTOMER_TYPE_CATEGORIES,
)
st.caption(CUSTOMER_TYPE_DESCRIPTIONS[customer_type_selected])

st.subheader("Stay Details")

weekend_nights_selected = st.number_input(
    "Number of weekend nights",
    min_value=0,
    max_value=19,
    value=1,
    step=1,
)
st.caption("Number of Saturday and Sunday nights included in the stay.")

week_nights_selected = st.number_input(
    "Number of week nights",
    min_value=0,
    max_value=50,
    value=2,
    step=1,
)
st.caption("Number of Monday to Friday nights included in the stay.")

st.subheader("Guest Details")

adults_selected = st.number_input(
    "Number of adults",
    min_value=1,
    max_value=55,
    value=2,
    step=1,
)

children_selected = st.number_input(
    "Number of children",
    min_value=0,
    max_value=10,
    value=0,
    step=1,
)

babies_selected = st.number_input(
    "Number of babies",
    min_value=0,
    max_value=10,
    value=0,
    step=1,
)

has_special_request_selected = st.selectbox(
    "Special requests",
    ["No", "Yes"],
)
st.caption(
    "Select Yes if the booking includes at least one special request from the guest."
)

submitted = st.button("Predict Cancellation")


if submitted:
    # Recreate the engineered features used during model training.
    total_nights = weekend_nights_selected + week_nights_selected
    total_guests = adults_selected + children_selected + babies_selected
    has_children = int(children_selected + babies_selected > 0)
    has_special_request = int(has_special_request_selected == "Yes")

    # Validate the booking before making a prediction.
    validation_errors = []

    if total_nights <= 0:
        validation_errors.append(
            "Please enter at least one weekend night or week night for the stay."
        )

    if total_guests <= 0:
        validation_errors.append("Please enter at least one guest for the booking.")

    if validation_errors:
        for error_message in validation_errors:
            st.error(error_message)
    else:
        input_data = {
            "hotel": hotel_selected,
            "lead_time": lead_time_selected,
            "deposit_type": deposit_type_selected,
            "market_segment": market_segment_selected,
            "customer_type": customer_type_selected,
            "total_nights": total_nights,
            "total_guests": total_guests,
            "has_children": has_children,
            "has_special_request": has_special_request,
        }

        df_input = pd.DataFrame([input_data])

        # Give pandas the full training categories before one-hot encoding.
        # This prevents a single-row input from losing its selected category
        # when drop_first=True is used.
        df_input["hotel"] = pd.Categorical(
            df_input["hotel"], categories=HOTEL_CATEGORIES
        )
        df_input["deposit_type"] = pd.Categorical(
            df_input["deposit_type"], categories=DEPOSIT_CATEGORIES
        )
        df_input["market_segment"] = pd.Categorical(
            df_input["market_segment"], categories=MARKET_SEGMENT_CATEGORIES
        )
        df_input["customer_type"] = pd.Categorical(
            df_input["customer_type"], categories=CUSTOMER_TYPE_CATEGORIES
        )

        df_input_encoded = pd.get_dummies(
            df_input,
            columns=["hotel", "deposit_type", "market_segment", "customer_type"],
            drop_first=True,
        )

        # Match the exact feature order used during model training.
        df_input_encoded = df_input_encoded.reindex(
            columns=model_columns,
            fill_value=0,
        )

        prediction = model.predict(df_input_encoded)[0]
        probabilities = model.predict_proba(df_input_encoded)[0]

        # Probability that the booking will be cancelled (class = 1).
        class_labels = list(model.classes_)
        cancelled_class_index = class_labels.index(1)
        cancellation_probability = probabilities[cancelled_class_index]

        st.subheader("Prediction Result")

        if prediction == 1:
            st.warning("⚠ High Cancellation Risk")
            st.write("The model predicts that this booking is likely to be cancelled.")
        else:
            st.success("✅ Low Cancellation Risk")
            st.write("The model predicts that this booking is unlikely to be cancelled.")

        st.metric(
            "Cancellation Probability",
            f"{cancellation_probability:.1%}",
        )


with st.expander("About this model"):
    st.write("**Model:** Tuned Random Forest Classifier")
    st.write(
        "**Purpose:** Predict whether a hotel booking is likely to be cancelled."
    )
    st.write("**Prediction target:** Booking cancelled or not cancelled")
    st.write(
        "The prediction is an estimate produced from patterns in the training "
        "dataset and should support, rather than replace, business judgement."
    )