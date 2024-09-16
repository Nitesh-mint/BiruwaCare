from dotenv import load_dotenv
import os

from django.shortcuts import render, redirect

#for the model
import tensorflow as tf
import streamlit as st
import numpy as np
from PIL import Image
import io

from .forms import ImageUploadForm
from .models import ImagePrediction, DiseaseInfo


load_dotenv()
def home(request):
    return render(request,'home.html')

def predict(img):
    try:
        model = tf.keras.models.load_model("/Users/niteshmint/Downloads/archive/trained_plant_disease_model.keras")
        image = tf.keras.preprocessing.image.load_img(img,target_size=(128,128))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr]) #convert single image to batch
        predictions = model.predict(input_arr)
        result_index=  np.argmax(predictions) #return index of max element
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                        'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                        'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                        'Corn_(maize)___Common_rust', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                        'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                        'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                        'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                        'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                        'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                        'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                        'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                        'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                        'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                        'Tomato___healthy']
        output = class_name[result_index]
        return output     
    except Exception as e:
        return None


def upload_image(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_prediction = form.save(commit=False)
            image_prediction.user = request.user
            uploaded_image = request.FILES['image']
            img_bytes = io.BytesIO(uploaded_image.read())
            prediction = predict(img_bytes)
            if prediction is None:
                return redirect('upload_image')
            else:
                cleaned_prediction = prediction.replace("___", " ")
                image_prediction.prediction = "".join(cleaned_prediction)
                prediction_disease = image_prediction.prediction.split(" ")[1]
                prediction_disease = prediction_disease.replace("_", " ")
                try:
                    disease = DiseaseInfo.objects.filter(name__iexact=prediction_disease)
                    image_prediction.disease = disease[0]
                except:
                    pass
                image_prediction.save()
                return redirect('result',pk=image_prediction.pk)
    else:
        form = ImageUploadForm()
    return render(request, 'mainapp/input_image.html', {'form':form})


def result(request, pk):
    image_prediction = ImagePrediction.objects.get(pk=pk)
    prediction_family = image_prediction.prediction.split(" ")[0]
    prediction_disease = image_prediction.prediction.split(" ")[1]
    print(prediction_disease)
    if prediction_disease == "healthy":
        infection_false = "healthy"
        infection_true = False
    else:
        infection_true = "Infected"
        infection_false = False
    context = {
        'prediction_family': prediction_family,
        'prediction_disease': prediction_disease,
        'image_prediction':image_prediction,
        'infection_false':infection_false,
        'infection_true':infection_true,
    }
    return render(request, 'mainapp/result.html', context=context)