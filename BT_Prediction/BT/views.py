from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import published_articles
import keras
from PIL import Image
import requests
import json
import numpy as np
import os
from django.core.files.storage import FileSystemStorage

media = 'media'
model = keras.models.load_model('bestmodel(UK).h5')




def makepredictions(path):
       img = Image.open(path)
       img_d = img.resize((224,224))
       img_d = np.array(img_d, dtype=np.float64)
       img_d = np.array(img_d)
       img_d = img_d.reshape(1,224,224,3)

       predictions = model.predict(img_d)
       a = np.where(predictions > 0.5, 1,0)

       if a==0:
              a = "Positive"

       else:
              a = "Negative"

       return a

def index(request):
       if request.method == 'POST' and request.FILES['upload']:
              upload = request.FILES['upload']
              fss = FileSystemStorage()
              file = fss.save(upload.name , upload)
              file_url = fss.url(file)
              predictions = makepredictions(os.path.join(media , file))
              return render(request , 'index.html', {'pred': predictions , 'file_url':file_url})                 
       else:
              return render(request , 'index.html')

def home(request):
       return render(request , 'home.html')

def bt(request):
       return render(request , 'bt.html')

def mt(request):
       return render(request , 'mt.html')

def stat(request):
       return render(request , 'stat.html')

def publish(request):

       published = published_articles.objects.all()
       return render(request , 'publish.html', {'published':published})

def signup(request):
       
       username = None
       email = None
       password = None
       Conpass = None

       if request.method == 'POST':
              username = request.POST['Username']
              email = request.POST['Email']
              password = request.POST['Password']
              Conpass = request.POST['Conpass']

              if password==Conpass:
                     if User.objects.filter(email=email).exists():
                            messages.info(request , '**Email already exists')
                            return redirect('/')
                     else:
                            user = User.objects.create_user(username = username , password = password , email = email)
                            user.save()
                            messages.info(request , 'Account Created ! Login to Continue')
                            return redirect('/')
              else:
                     messages.info(request, 'Passwords are not same')
                     return redirect('/') 
       else:
              return render(request,'signup.html')           

def login_form(request):

       if request.method=='POST':

                 username = request.POST['username']
                 password = request.POST['password']
                 user = authenticate(request, username=username, password=password)
                 
                 if user is not None:
                      login(request, user)
                      return redirect('home')
  
                 else:
                      messages.info(request , 'Invalid Credentials')
                      return redirect('login_form')

       else:
              return render(request,'login.html')

def logout_form(request):
       logout(request)
       return redirect('home')

def live_well(request):
       return render(request , 'live_well.html')

def five_steps(request):
       return render(request,'five_steps.html')

def eat_well(request):
       return render(request,'eat_well.html')

def add_support(request):
       return render(request,'add_support.html')


from django.core.mail import send_mail

def contact(request):

       if request.method == 'POST':
              subject = request.POST['subject']
              from_email = request.POST['email']
              message = request.POST['message']
              to = 'saadankamal.lohani@gmail.com'

              send_mail
              (
                     subject,
                     message,
                     from_email,
                     [to]
              )      


       return render(request , 'contact.html')



def calculator(request):
       
       if request.method == 'POST':
              query = request.POST['query']
              api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
              api_request = requests.get(api_url + query, headers={'X-Api-Key': 'cOwDKXlhLOUA6RUGYZEG9Q==nwfPkYPpxQDrBZKv'})

              try:
                     api = json.loads(api_request.content)
                     print(api_request.content)
              except Exception as e:
                     api = "There is an error"
                     print(e)
              
              return render(request, 'calculator.html', {'api':api})
       
       else:
             return render(request, 'calculator.html', {'query':'Enter Valid Query'}) 