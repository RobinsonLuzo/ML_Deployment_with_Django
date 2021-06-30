# Deploying an ML model using Django:

An example of building, saving and deploying a machine learning model using Django. CSS taken from Bootstrap. Intended for illustrative purposes - most production models have a lot more complexity!

For the Django project itself use the command: "python manage.py runserver" in the "iris" folder to start the application. In here you can enter the numbers to be used as data for a prediction - it should look like so:

![Django input](https://raw.githubusercontent.com/RobinsonLuzo/ML_Deployment_with_Django/main/img/django_input.JPG "Django Prompt for user input")

Clicking the "Submit" button should result in a small pop-up window with the predicted result, given the input data.

![Django prediction result](https://raw.githubusercontent.com/RobinsonLuzo/ML_Deployment_with_Django/main/img/django_prediction_output.JPG "Django Prediction Results")


## The Model:

The model is developed in a Jupyter Notebook ("Iris_model_training") and saved to disk. The notebook's second cell shows roughly how the input will be taken from the user in Django:

![Notebook prompt](https://raw.githubusercontent.com/RobinsonLuzo/ML_Deployment_with_Django/main/img/notebook_prompt.JPG "Notebook Prompt for user input")

This yields a prediction of the flower based on the details supplied:

![Notebook prediction](https://raw.githubusercontent.com/RobinsonLuzo/ML_Deployment_with_Django/main/img/notebook_prediction.JPG "Notebook Prediction for user input")