from django.shortcuts import render
import numpy as np
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class CovidPrediction(APIView):
    def post(self, request):
        data = request.data
        cough= data['cough'] #YES or NO whether cough symptoms are there or not
        fever= data['fever'] #YES or NO whether fever symptoms are there or not
        throat= data['throat'] #YES or NO whether sore throat is a symptom or not 
        breathe= data['breathe'] #YES or NO whether the person has difficulty breathing or not
        headache= data['headache'] #YES or NO whether the person is expeiriencing headache
        above60= data['above60'] #If the person is a senior citizen or not
        sex= data['sex'] #If the person is male or female (could be expanded to people with other biological attributes but restricted due to absence of data)
        situation= data['situation'] #If YES, the person has contact with a confirmed positive, if NO, the person has come from abroad in past 2 weeks, if Other, none of the 2.
        mp = {'YES':1, 'NO':0, 'OTHER':2, 'MALE':1, 'FEMALE':0}
        result = np.array([
                            mp[cough],
                            mp[fever],
                            mp[throat],
                            mp[breathe],
                            mp[headache],
                            mp[above60],
                            mp[sex],
                            mp[situation],])
        
        model= ApiConfig.model_load
        predictions= model.predict(result.reshape((1, 8)))
        if predictions[0] ==1:
            covid= "Most likely positive"
        else:
            covid= "Most likely negative"
        response_dict = {"Covid prediction": covid}
        return Response(response_dict, status=200)