# Sample_Django_project

A XGBoost classifier model has been used to create an API with the help of Django REST framework. The API accepts data in JSON format (examples in api_examples.txt) using a POST request.
The model predicts whether a person is likely to be covid 19 positive given symptoms. 

The features for the JSON query include:
1. YES or NO whether cough symptoms are there or not
2. YES or NO whether fever symptoms are there or not
3. YES or NO whether sore throat is a symptom or not 
4. YES or NO whether the person has difficulty breathing or not
5. YES or NO whether the person is experiencing headache
6. If the person is a senior citizen or not
7. If the person is male or female (could be expanded to people with other biological attributes but restricted due to absence of data)
8. If YES, the person has contact with a confirmed positive, if NO, the person has come from abroad in past 2 weeks, if Other, none of the 2.
