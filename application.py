'''import pickle
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler
# 1. Import the Flask class

from flask import Flask,request,jsonify,render_template

# 2. Create an instance of the Flask class
application = Flask(__name__)
app = application  # for compatibility with some hosting services
#import redge regressor and standard scaler pickle file
ridge_model=pickle.load(open("models/ridge.pkl","rb"))
standard_scaler=pickle.load(open("models/scaler.pkl","rb"))

# 3. Define a route and the view function to handle requests to that route
@app.route('/')
def index():
    """This function runs when someone visits the root URL ('/')."""
    return render_template('index.html')
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        Temperature=float(request.form.get("Temperature"))
        RH=float(request.form.get("RH"))
        Ws=float(request.form.get("Ws"))
        Rain=float(request.form.get("Rain"))
        FFMC=float(request.form.get("FFMC"))
        DMC=float(request.form.get("DMC"))
        ISI=float(request.form.get("ISI"))
        Classes=float(request.form.get("Classes"))
        Region=request.form.get("Region") 

        new_data_scaled=standard_scaler.transform([[emperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')


# 4. Run the application
if __name__ == '__main__':
    # debug=True enables auto-reloading and an in-browser debugger
    app.run(host="0.0.0.0",debug=True)'''
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, jsonify, render_template

# --- DIAGNOSTIC PRINT 1 ---
# This will prove we are running the correct file.
print("--- Starting the application.py file! ---")

# Create an instance of the Flask class
application = Flask(__name__)
app = application  # for compatibility with some hosting services

# import ridge regressor and standard scaler pickle file
ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
standard_scaler = pickle.load(open("models/scaler.pkl", "rb"))

# Define a route and the view function to handle requests to that route
@app.route('/')
def index():
    """This function runs when someone visits the root URL ('/')."""
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = float(request.form.get("Classes"))
        Region = float(request.form.get("Region"))

        # NOTE: I have also fixed the 'emperature' typo from before
        new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_data_scaled)
        return render_template('home.html', results=result[0])
    else:
        return render_template('home.html')
    


# Run the application
if __name__ == '__main__':
    # --- DIAGNOSTIC PRINT 2 ---
    # This will print all known URLs before starting the server.
    with app.app_context():
        print("--- All Registered Routes ---")
        print(app.url_map)
        print("---------------------------")
    
    app.run(host="0.0.0.0", debug=True)