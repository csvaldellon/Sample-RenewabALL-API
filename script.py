from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    predLuzon, predVisayas, predMindanao = 0, 0, 0
    if request.method == "POST":
        userDate = request.form.get("date")
        predLuzon, predVisayas, predMindanao = get_predict(userDate)
    return render_template("index.html", predLuzon=predLuzon, predVisayas=predVisayas, predMindanao=predMindanao)


# @app.route("/predict", methods=["GET", "POST"])
def get_predict(userDate):
    model = pd.read_csv("Peak_Demand_Predictions.csv")
    # print(model)

    luzonValue = round(model["Luzon"][model["Date"] == userDate].values[0])
    visayasValue = round(model["Visayas"][model["Date"] == userDate].values[0])
    mindanaoValue = round(model["Mindanao"][model["Date"] == userDate].values[0])

    return luzonValue, visayasValue, mindanaoValue


if __name__ == "__main__":
    app.run(debug=True)
