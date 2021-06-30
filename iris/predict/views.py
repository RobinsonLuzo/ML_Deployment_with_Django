from django.shortcuts import render

# Prediction view
def predict(request):
    return render(request, 'predict.html')