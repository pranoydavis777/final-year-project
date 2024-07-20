from django.shortcuts import render

# Create your views here.
#Importing Libraries required for the code 
from django.shortcuts import render
from .models import Monument
import numpy as np
import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Create your views here.

#Creating variables 
indexhtml='index.html'
abouthtml='about.html'
uploadhtml='upload.html'
resulthtml='result.html'

#Rendering Pages
def home(request):
    return render(request,indexhtml)

def about(request):
    return render(request,abouthtml)



#Loading the Model
#Saving the image file uploaded 
#Using the saved file to predict 
#Assigining the message to predictions
def upload(request):

    pathss=os.listdir("app/dataset/test")
    classes=[]
    
    for i in pathss:
        classes.append(i)
    



    if request.method=='POST':
        m1 = int(request.POST['alg'])
        file=request.FILES['data']
        img=Monument(image=file)
        img.save()

        if m1==1:
            path="app/static/saved/"+ img.filename()
            path1="/static/saved/"+ img.filename()
            models=load_model("app/models/CNN_1.h5")
            

        elif m1==2:
            path="app/static/saved/"+ img.filename()
            path1="/static/saved/"+ img.filename()
            models=load_model("app/models/mobilenet.h5")
     
        x=image.load_img(path,target_size=(224,224))
        x=image.img_to_array(x)
        x=np.expand_dims(x,axis=0)
        x/=255
        results=models.predict(x)
        b=np.argmax(results)
        prediction=classes[b]
      


            

        
        return render(request,resulthtml,{'result':prediction,'path':path1})


    return render(request,uploadhtml)



