from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the model
model = joblib.load("E:/Airline Fare App/model/final_xgb_model_10.pkl")

app = Flask(__name__)

# Home page with input form
@app.route("/")
def home():
    return render_template("form.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            # Extract input values from form
            features = [
                float(request.form["MktMilesFlown"]),
                float(request.form["LCC_Comp"]),
                float(request.form["Carrier_freq"]),
                float(request.form["Carrier"]),
                float(request.form["NonStopMiles"]),
                float(request.form["Pax"]),
                float(request.form["MktCoupons"]),
                float(request.form["Market_HHI"]),
                float(request.form["Market_share"]),
                float(request.form["ODPairID_freq"])
            ]

            input_data = np.array([features])
            prediction = model.predict(input_data)[0]

            return render_template("result.html", prediction=round(prediction, 2))

        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)