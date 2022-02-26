from _site2.forms import LoginForm

#for the login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect

def login_page (request): #primera vista
    message = None
    if request.method =='POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            user =  authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    message = "Login succesful , redirecting..."
                    return render(request,'index_areas.html') #HttpResponse(documento)
                else:
                    message = "Tu usuario esta inactivo"
            else:
                message = "Nombre de usuario y/o password incorrectos"
        #form = AuthenticationForm (data = request.POST)
        #user = form.get_user()
        print(message)
    else:
        print('POST not recived')
        form = LoginForm()
    return render(request,'index.html')
