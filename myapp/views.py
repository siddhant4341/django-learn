from django.shortcuts import render,redirect
from . models import *
# Create your views here.
#1-------------
def InsertPageView(request):
    return render(request,"app/insert.html")

#creating form action for insert.html form

def InsertData(request):
    #data comes from html page to view 
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

   #creating model of object class
    newuser = Teacher.objects.create(Firstname=fname, Lastname=lname ,Email=email ,Contact=contact)

    #After Insert render on show.html
    return redirect('showpage')

#2----------------
def ShowPage(request):
    #query for getting data from database
    all_data = Teacher.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

#3------------------
#Edit page view
def Editpage(request,pk):
    get_data = Teacher.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

# update data view
def UpdateData(request,pk):
    udata = Teacher.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    
    udata.save()
    return redirect('showpage')
#4------------------
def DeleteData(request,pk):
    ddata = Teacher.objects.get(id=pk)
    ddata.delete()
    return redirect('showpage')

#5------------------
#for registration page 

def RegisterPage(request):
    return render(request,"app/register.html")

#view for user registration
def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password =request.POST['password']
        cpassword =request.POST['cpassword']

        #first validate that user already exists...
        user = User.objects.filter(Email = email)
        if user:
            message = "Email already exists"
            return render(request,'app/register.html',{'msg':message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message = "user register Successfully.."
                return render(request,"app/login.html",{'msg':message})
            else:
                message = "password and confirm password does not match !! "
                return render(request,"app/register.html",{'msg':message})

#6--------------------
#Login View
def LoginPage(request):
    return render(request,"app/login.html")

#Login User view
def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        #checking emailID With Database..
        user = User.objects.get(Email = email)
        if user:
            if user.Password == password:
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                return render(request,"app/home.html")
            else:
                message = "password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "user does not exist"
            return render(request,"app/register.html",{'msg':message})
        
#7----------------------
#view for ImageUploading

def IndexPage(request):
    return render(request,"app/index.html")

def UploadImage(request):
    if request.method == "POST":
        imagename = request.POST['imgname']
        pics = request.FILES['image']

        newimg  = ImageData.objects.create(Imagename = imagename, Image = pics)
        return render(request,"app/shows.html")

        
