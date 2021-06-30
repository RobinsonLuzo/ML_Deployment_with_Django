import joblib
import os
from django.http import JsonResponse
from django.shortcuts import render

# Prediction view
def predict(request):
    return render(request, 'predict.html')

# prediction handling - on submission of data by user:
def predict_chances(request):

    # if POST, assign data recieved from client:
    if request.POST.get('action') == 'post':
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width  = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width  = float(request.POST.get('petal_width'))

        # load model from storage:
        model = joblib.load(os.path.dirname(os.getcwd()) + "\\saved_model\\iris_prediction.pkl")

        # Make prediction:
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        classification = result[0]
        
        # return result and submitted data:
        return JsonResponse({'result':  classification, 'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width},
                            safe=False)

