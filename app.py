
from flask import Flask,render_template,request
import pickle 

import numpy as np 

# from transformer import dependent_Transformer,propertyArea_Transformer
from dataTransformer import dependent_Transformer,propertyArea_Transformer

app = Flask(__name__)
model = pickle.load(open('./models/model.pkl','rb'))


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/prediction",methods=['GET','POST'])
def predict():
    if request.method == "POST":
        try:
            GENDER = request.form['gender']
            MARRIED = request.form['married']
            DEPENDENTS = request.form['dependents']
            EDUCATION = request.form['education']
            SELF_EMPLOYED = request.form['selfemployed']
            PROPERTY_AREA = request.form['propertyarea']
            CREDIT_HISTORY = request.form['credithistory']
            APPLICANT_INCOME = float(request.form['appliincome'])
            COAPPLICANT_INCOME = float(request.form['coappliincome'])
            LOAN_AMOUNT = float(request.form['loanAmount'])
            LOAN_AMOUNT_TERM = float(request.form['loanterm'])

            dep1, dep2, dep3 = dependent_Transformer(DEPENDENTS)
            semiurban, urban = propertyArea_Transformer(PROPERTY_AREA)

            APPLICANT_INCOME_LOG = np.log(APPLICANT_INCOME)
            TOTAL_INCOME_LOG = np.log(APPLICANT_INCOME + COAPPLICANT_INCOME)
            LOAN_AMOUNT_LOG = np.log(LOAN_AMOUNT)
            LOAN_AMOUNT_TERM_LOG = np.log(LOAN_AMOUNT_TERM)

            prediction = model.predict([[CREDIT_HISTORY, APPLICANT_INCOME_LOG, LOAN_AMOUNT_LOG, LOAN_AMOUNT_TERM_LOG, TOTAL_INCOME_LOG, GENDER, MARRIED, dep1, dep2, dep3, EDUCATION, SELF_EMPLOYED, semiurban, urban]])

            if prediction == "N":
                prediction_text = "No"
            else:
                prediction_text = "Yes"

         

            return render_template("prediction.html", prediction_text=prediction_text)
    

        
        except Exception as e:
            # Handle exceptions and provide feedback to the user
            # error_message = str(e)
            # return json.dumps({"error_message": "Error"})
            return render_template("prediction.html", error_message="Some Server Issues !Try Again")
        
    else:

      return render_template("prediction.html")


app.run(debug=True)
