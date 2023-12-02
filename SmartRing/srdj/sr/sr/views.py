from django.http import HttpResponse
from django.shortcuts import render

# header file for ML 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def index(request):
    return render(request,'index.html')

def mlpage(request):
    return render(request,'mlpage.html')

def form_submission(request):
    if request.method == 'GET':
        oxygen_saturation = request.GET.get('oxygen_saturation', '')
        heart_rate = request.GET.get('heart_rate', '')
        
        # Do something with the collected values (e.g., process and display)
        
        # ml code 

        # Load dataset
        df = pd.read_csv('C:/Users/HASNAT/Desktop/SmartRing/accident_data.csv');

        # Define features 
        X = df[['Oxygen saturation (%)', 'Heart rate (bpm)']]

        # Define target
        y = df['Activity']

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        smart_ring_values = [
             oxygen_saturation,
            heart_rate,
    
            ]


        input_data = [smart_ring_values]
        prediction = model.predict(input_data)
        context = {
            'oxygen_saturation': oxygen_saturation,
            'heart_rate': heart_rate,
            'result':prediction[0],
        }
        
        return render(request, 'form_submission.html', context)