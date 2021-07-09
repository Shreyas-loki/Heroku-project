import numpy as np
from flask import Flask, request, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('university.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    """
    For rendering results on HTML GUI
    """
    x_test = [float(x) for x in request.form.values()]
    final_features = [np.array(x_test)]
    prediction = model.predict(final_features)
        
    output = prediction[0]
    if(output == False):
        return render_template('index.html', Prediction_text="You don't have a chance")
    else:
        return render_template('index.html', Prediction_text="You have a chance")


if __name__ == "__main__":
    app.run(debug=True)
    