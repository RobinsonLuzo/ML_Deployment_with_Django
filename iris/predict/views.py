import joblib
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

        model = joblib.load(r"C:\Users\BenDa\Desktop\Projects\ML_Deployment_with_Django\saved_model\iris_prediction.pkl")

        # Make prediction
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        classification = result[0]

        return JsonResponse({'result': classification, 'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width},
                            safe=False)

