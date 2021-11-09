from  models import Prophet
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/",methods=['GET'])
def run():
    model = Prophet.FBProphetModel().model
    future = model.make_future_dataframe(periods=1095, freq='D')
    forecast = model.predict(future)
    return jsonify(forecast.to_json(orient='table'))


if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0', debug=True)