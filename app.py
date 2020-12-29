from flask import Flask, render_template, request,url_for
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import shutil


app = Flask(__name__)
model = pickle.load(open("model/random_forest_regression_model.pkl", "rb"))


@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")


standard_to = StandardScaler()


@app.route("/predict", methods=["POST"])
def predict():
    pred_next_5_years = []
    p_years = []
    Fuel_Type_Diesel = 0
    if request.method == "POST":
        Year = int(request.form["Year"])
        Pur_year =Year
        Present_Price = float(request.form["Present_Price"])
        Kms_Driven = int(request.form["Kms_Driven"])
        Kms_Driven2 = np.log(Kms_Driven)
        Owner = int(request.form["Owner"])
        Fuel_Type_Petrol = request.form["Fuel_Type_Petrol"]
        if Fuel_Type_Petrol == "Petrol":
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        Year = 2020 - Year
        Seller_Type_Individual = request.form["Seller_Type_Individual"]
        if Seller_Type_Individual == "Individual":
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0
        Transmission_Mannual = request.form["Transmission_Mannual"]
        if Transmission_Mannual == "Mannual":
            Transmission_Mannual = 1
        else:
            Transmission_Mannual = 0
        prediction = model.predict(
            [
                [
                    Present_Price,
                    Kms_Driven2,
                    Owner,
                    Year,
                    Fuel_Type_Diesel,
                    Fuel_Type_Petrol,
                    Seller_Type_Individual,
                    Transmission_Mannual,
                ]
            ]
        )
        output = round(prediction[0], 2)
        yr = 0
        for i in range(Year, Year + 5):
            p = model.predict(
                [
                    [
                        Present_Price,
                        Kms_Driven2,
                        Owner,
                        i,
                        Fuel_Type_Diesel,
                        Fuel_Type_Petrol,
                        Seller_Type_Individual,
                        Transmission_Mannual,
                    ]
                ]
            )
            pred_next_5_years.append(round(p[0],3))
            p_years.append("yr" + str(2020 + yr))
            yr = yr + 1
        print(pred_next_5_years)
        fig = plt.figure()
        plt.plot(p_years, pred_next_5_years)
        plt.title("Next 5 years Prediction")
        plt.xlabel("Years")
        plt.ylabel("Rupees in Lakh")
        txt ="Year: " + str(Pur_year) + ' Present Price: ' + str(Present_Price)
        plt.text(0.05,0.95,txt, transform=fig.transFigure, size=12)
        plt.close()
        
        with PdfPages("static/my_report.pdf") as pdf_pages:
            pdf_pages.savefig(fig, pad_inches=0.6, bbox_inches="tight")

        shutil.copy2('static/my_report.pdf', 'report/my_report.pdf')
        pdf_file =url_for('static',filename ="my_report.pdf")

        merged_list = tuple(zip(p_years, pred_next_5_years))
        if output < 0:
            return render_template(
                "index.html", prediction_texts="Sorry you cannot sell this car"
            )
        else:
            return render_template(
                "index.html",
                prediction_text="You Can Sell The Car at {}".format(output),
                pages=merged_list,
                pdf_file =pdf_file,
            )
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
