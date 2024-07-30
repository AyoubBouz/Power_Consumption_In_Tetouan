from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from powerconsumptiontetouan.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app
app.debug = True

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            # Temperature,Humidity,WindSpeed,GeneralDiffuseFlows,DiffuseFlows
            temperature =float(request.form['temperature'])
            humidity =float(request.form['humidity'])
            windSpeed =float(request.form['windSpeed'])
            generalDiffuseFlows =float(request.form['generalDiffuseFlows'])
            diffuseFlows =float(request.form['diffuseFlows'])
            dateTime =request.form['dateTime']
            dateTime_pd = pd.to_datetime(dateTime)
            month = dateTime_pd.month
            day = dateTime_pd.day
            hour = dateTime_pd.hour
         
            data = [temperature,humidity,windSpeed,generalDiffuseFlows,diffuseFlows,month,day,hour]
            data = np.array(data).reshape(1, 8)
            # print(data,flush=True)
            obj = PredictionPipeline()
            predict = obj.predict(data)


            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)