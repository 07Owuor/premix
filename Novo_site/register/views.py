from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import register
from .models import Register

def index(request):
    return render(request, 'register/register.html')

def add_user (request):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            title = request.POST.get('title', ' ')
            fname = request.POST.get('fname', ' ')
            lname = request.POST.get('lname', ' ')
            email = request.POST.get('email', ' ')
            diet = request.POST.get('diet', ' ')
            medNo = request.POST.get('medNo', ' ')
            practAd = request.POST.get('practAd', ' ')

            #image = request.POST.get('image', ' ')

            Register_obj = Register(title=title, fname=fname, lname=lname, email=email, diet=diet, medNo=medNo, practAd=practAd)
            Register_obj.save()

            return HttpResponseRedirect(reversed('register:add_user'))
    else:
        form = register()

    return render(request,'register/register.html', {
        'form':form
    })
