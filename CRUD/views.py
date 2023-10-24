from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Students


def index(request):
    data = Students.objects.all()
    context = {"data":data}
    return render(request,'index.html',context)

def handlesignup(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        myuser =authenticate(username=username,password=password)


        if myuser is not None:
            login(request,myuser)
            return redirect('/')

        else:
            return redirect('/login')

    return render(request,'login.html')



def insertdata(request):
    if request.method =='POST':
        name =request.POST.get('name')
        email =request.POST.get('email')
        age =request.POST.get('age')
        gender =request.POST.get('gender')
        # print(name,email,age,gender)
        query = Students(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect('/')

    return render(request,'index.html')



def updatedata(request):
    if request.method =='POST':
        name =request.POST.get('name')
        age =request.POST.get('age')
        email =request.POST.get('email')
        gender =request.POST.get('gender')

        edit = Students.objects.get(id=id)
        edit.name =name
        edit.email =email
        edit.age =age
        edit.gender =gender
        edit.save()
        return redirect('/')
    d = Students.objects.get(id=id)
    context = {'d': d}
    return render(request,'edit.html',context)



def deletdata(request):
    d = Students.objects.get(id=id)
    d.delete()
    return redirect('/')
def handlelogout(request):
    logout(request)
    return redirect('/signup')







