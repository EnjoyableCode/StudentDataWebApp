from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from phchallenge_site import models
from datetime import datetime, timedelta, date
import time


def is_admin(user):
    if user.groups.filter(name='Admin'):
        return True
    return False


def sign_in(request):
    try:
        url=request.GET['next']

    except:
        url = "/"

    return render(request, 'signin.html', {
        'url': url,
        })


def log_in(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        try:
            url = request.GET['next']
        except:
            url = "/"
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(url)
            else:
                return render(request, 'signin', {
                    'failure': 2,
                    'url': url,
                    })
        else:
            return render(request, 'registration/signin.html', {
                'failure': 1,
                'url': url,
                })
    except:
        return HttpResponseRedirect('/signin/')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/signin/')



@login_required(redirect_field_name='/')
def add_data(request):

    return render(request, 'index.html')



@login_required(redirect_field_name='/')
def view_data(request):

    if request.method == 'POST':
        is_athlete = False
        url = request.POST['url']
        name = request.POST['name']
        if 'is_athlete' in request.POST:
            is_athlete =  True
        joke = request.POST['joke']

        new_student = models.Student.objects.create(
            name=name,
            homepage_url=url,
            is_athlete=is_athlete,
            favorite_joke=joke
            )
    
        new_student.save()
    students = models.Student.objects.all()
    return render(request, 'report.html', {
            'students': students,
        })



@login_required(redirect_field_name='/')
def edit_data(request):

    if request.method == 'POST':
        student_id = request.POST['student_id']

    students = models.Student.objects.filter(id=student_id)
    return render(request, 'editdata.html', {
            'students': students,
        })

@login_required(redirect_field_name='/')
def save_data(request):

    if request.method == 'POST':
        student_id = request.POST['student_id']

        if 'delete' in request.POST:
            new_student = models.Student.objects.get(id=student_id)
            new_student.delete()

        else:
            name = request.POST['name']
            url = request.POST['url']
            is_athlete = False
            if 'is_athlete' in request.POST:
                is_athlete = True
            joke = request.POST['joke']

            new_student = models.Student.objects.get(id=student_id)
            new_student.name = name
            new_student.homepage_url = url
            new_student.is_athlete = is_athlete
            new_student.favorite_joke = joke
            new_student.save()

    students = models.Student.objects.all()
    return render(request, 'report.html', {
            'students': students,
        })
    
