# Deploying an ML model using Django:

An example of building, saving and deploying a machine learning model using Django. CSS taken from Bootstrap. Intended for illustrative purposes - most production models have a lot more complexity!

For the Django project itself use the command: "python manage.py runserver" in the "iris" folder to start the application. In here you can enter the numbers to be used as data for a prediction - it should look like so:

<img src="https://raw.githubusercontent.com/RobinsonLuzo/ML_Deployment_with_Django/main/img/django_input.JPG" alt="Django Prompt for user input" width="300"/>


Clicking the "Submit" button should result in a small pop-up window with the predicted result, given the input data.

<img src="https://raw.githubusercontent.com/RobinsonLuzo/ML_Deployment_with_Django/main/img/django_prediction_output.JPG" alt="Django Prediction Results" width="300"/>

## The Model:

The model is developed in a Jupyter Notebook ("Iris_model_training") and saved to disk. The notebook's second cell shows roughly how the input will be taken from the user in Django:

<img src="https://raw.githubusercontent.com/RobinsonLuzo/ML_Deployment_with_Django/main/img/notebook_prompt.JPG" alt="Notebook Prompt for user input" width="300"/>

This yields a prediction of the flower based on the details supplied:

<img src="https://raw.githubusercontent.com/RobinsonLuzo/ML_Deployment_with_Django/main/img/notebook_prediction.JPG" alt="Notebook Prediction for user input" width="300"/>
