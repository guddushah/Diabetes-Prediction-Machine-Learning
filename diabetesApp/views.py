from django.shortcuts import render
from joblib import load

model = load('./savedModels/model.joblib')

def home(request):
    return render(request, 'home.html')

def predictor(request):
    if request.method == 'POST':
         pregnancies=int(request.POST['pregnancies'])
         glucose=int(request.POST['glucose'])
         bloodPressure=int(request.POST['bloodPressure'])
         skinThickness=int(request.POST['skinThickness'])
         insulin=int(request.POST['insulin'])
         bMI=float(request.POST['bMI'])
         diabetesPedigreeFunction=float(request.POST['diabetesPedigreeFunction'])
         age=int(request.POST['age'])

         y_pred = model.predict([[pregnancies,glucose,bloodPressure,skinThickness,insulin,bMI,diabetesPedigreeFunction,age]])
         print(y_pred)

         if y_pred[0] == 0:
             y_pred = "NEGATIVE"
         elif y_pred[0] == 1:
             y_pred = "POSITIVE"

         return render(request,'predict.html', {'result': y_pred})
    return render(request, 'predict.html')