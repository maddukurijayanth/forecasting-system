from flask import Flask, render_template, request

import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("models/xgboost_multistate.pkl")

encoder = joblib.load("models/state_encoder.pkl")

states = list(encoder.classes_)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        state = request.form["state"]

        sales = float(request.form["sales"])

        state_encoded = encoder.transform([state])[0]

        features = np.array([[

            state_encoded,
            sales,
            sales,
            sales,
            sales,
            1000000,
            1,
            1,
            1

        ]])

        pred = model.predict(features)

        prediction = f"Predicted Future Sales: {pred[0]:,.2f}"

    return render_template(
        "index.html",
        prediction=prediction,
        states=states
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)