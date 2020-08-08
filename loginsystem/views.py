from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail

keyvalue = 0
# Create your views here.
def registerasnewuser(request):

    registerform = register()
    return render(request, 'loginsystem/registerform.html', {'registerform': registerform})

def registersave(request):

    global keyvalue

    if request.method == 'POST':
        registerform = register(request.POST)
        # print("2")
        keyvalue = 0
        if registerform.is_valid():

            if len(request.POST["password"]) < 8:

                keyvalue = 0
                return render(request, 'loginsystem/registerform.html', {'registerform': registerform, 'error': 'Password should be minimum of 8 characters', 'keyvalue': keyvalue})

            if request.POST["password"] != request.POST["password_again"]:

                keyvalue = 0
                return render(request, 'loginsystem/registerform.html', {'registerform': registerform, 'error': 'Passwords Dont Match', 'keyvalue': keyvalue})

            request.session['username'] = request.POST['username']
            request.session['emailID'] = request.POST['emailID']
            send_mail('MAXSHOP Registration Confirmation ', 'Thank you' + " " + registerform.cleaned_data['username'] + ' for registering with MAXSHOP, we hope we will fullfill your demands and interest. Please take a glance at amazing journey of maxshop. You can now purchase from our site https://www.myntra.com/', 'devansh@damco.com', [registerform.cleaned_data['emailID']], fail_silently=False)
            user = newuser(username = registerform.cleaned_data['username'], emailID = registerform.cleaned_data['emailID'], password = registerform.cleaned_data['password'])
            user.save()
            # print("HI")
            return redirect('shopme')
        
        else:
            return render(request, 'loginsystem/registerform.html', {'registerform': registerform})

def loginuser(request):
    global keyvalue
    keyvalue = 0
    user = newuser.objects.all()
    print(user)
    loginform = login()
    return render(request, 'loginsystem/loginform.html', {'loginform': loginform, 'keyvalue': keyvalue})

def loginuserget(request):

    

    if request.method == "POST":
        # print("2")
        loginform = login(request.POST)

        # username = request.POST["username"]
        # password = request.POST["password"]


        if loginform.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            data = newuser.objects.filter(username = username, password = password)
            if data:
                request.session['username'] = username
                global session
                session = request.session

                global keyvalue
                keyvalue = 0
                return redirect('shopme')

            if username not in newuser.objects.values_list('username', flat = True):
                return render(request, 'loginsystem/loginform.html', {'error1': "Username Does Not Exists", 'loginform': loginform})
            
            if password not in newuser.objects.values_list('password', flat = True):
                return render(request, 'loginsystem/loginform.html', {'error2': "Password Does Not Exists", 'loginform': loginform})
            
            user = newuser.objects.filter().values('username', 'password')

            for u in user:
                if username in u['username']:
                    if password not in u['password']:
                        return render(request, 'loginsystem/loginform.html', {'error3': 'Username password mismatch', 'loginform': loginform})

                    else:
                        return redirect('shopme')
            # print(username)
            return render(request, 'loginsystem/loginform.html', {'username': username})

def password_reset_email(request):

    password_reset_email_form = passwordemailform()
    return render(request, 'loginsystem/password_reset_email.html', {'password_reset_email_form': password_reset_email_form})

def password_reset_email_verification(request):

    if request.method == "POST":

        password_reset_email_form = passwordemailform(request.POST)
        if password_reset_email_form.is_valid():

            user = newuser.objects.values_list('emailID', flat=True)
            print(user)
            email = password_reset_email_form.cleaned_data['emailID']
            request.session['e'] = email
            if email in user:
                # print("EMAIL HERE")
                send_mail('Password Reset Link', 'Dear User we have recieved password reset request from this email id. Please click on the following link to reset your password ' + '127.0.0.1:8000/loginsystempassword_reset_view', 'myline.dicksjohn@gmail.com', [email], fail_silently=False)
                return render(request, 'loginsystem/password_reset_email.html', {'password_reset_email_form': password_reset_email_form, 'prompt': 'Check Your Email We have Sent You The Link For Resetting The Password'})

            else:

                return render(request, 'loginsystem/password_reset_email.html', {'password_reset_email_form': password_reset_email_form, 'error': 'This email id is not registered'})

    return render(request, 'loginsystem/password_reset_email.html')

def password_reset_view(request):

    password_reset_form = password_reset()
    return render(request, 'loginsystem/password_reset_form.html', {'password_reset_form': password_reset_form})

def password_reset_done(request):

    if request.method == "POST":

        password_reset_form = password_reset(request.POST)
        if password_reset_form.is_valid():

            if request.POST["password"] != request.POST["password_again"]:

                return render(request, 'loginsystem/password_reset_form.html', {'error': 'Passwords Donot Match'})

            if request.POST["username"] not in newuser.objects.values_list('username', flat=True):

                return render(request, 'loginsystem/password_reset_form.html', {'error': 'Username does not exist'})

            u = newuser.objects.filter().values('emailID', 'username')
            for a in u:

                if request.session['e'] in a['emailID']:
                    print("here there i am yours")
                    if request.POST['username'] not in a['username']:

                        return render(request, 'loginsystem/password_reset_form.html', {'error': 'Username does not matches with your email id', 'password_reset_form': password_reset_form})

            user = newuser.objects.filter(username=request.POST["username"]).update(password=password_reset_form.cleaned_data["password"])
            return redirect('login')

def logout(request):
    del request.session['username']
    request.session.modified=True
    global keyvalue
    keyvalue=0
    return redirect('login')