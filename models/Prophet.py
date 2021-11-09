from prophet import Prophet
import joblib
import glob, os


class FBProphetModel:
    model = None
    def __init__(self):
        if self.model is None:
            self.model = joblib.load("/home/user/models/model.pkl")
