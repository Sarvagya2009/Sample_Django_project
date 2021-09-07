from django.apps import AppConfig
import os
import xgboost as xgb
from django.conf import settings



class ApiConfig(AppConfig):
    name = 'API'
    MODEL_FILE = os.path.join(settings.MODELS, "model1.json")
    model_load = xgb.XGBClassifier()
    model_load.load_model(MODEL_FILE)