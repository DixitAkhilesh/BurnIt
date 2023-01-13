import imp
from re import template
from unicodedata import name
from django.shortcuts import render, HttpResponse
from matplotlib.pyplot import cla
from home.models import User, Dish, DailyCalorieCount
from home.models import User, Workout, DailyCalorieCount, DailyCaloriesBurnt
from json import dumps
from datetime import datetime
from django.views.generic import TemplateView

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request , 'signup.html')

def login(request):
    return render(request , 'login.html')

def main(request):
    name = ""

    if request.method == "POST" and request.POST.get('feature') == "login":
        mobile = request.POST.get('mob-num')
        password = request.POST.get('pwd')
        result = User.objects.raw("Select * from home_user where mobile=%s and password=%s", (mobile, password))[0];
        if(result and mobile == result.mobile and password == result.password):
            request.session['userName'] = result.name;
            request.session['mobile'] = result.mobile;
            request.session['gender'] = result.gender;
        name = result.name
        

    if request.method == "POST" and request.POST.get('feature') == "signup":
        name = request.POST.get('name');
        mobile = request.POST.get('mobile');
        age = request.POST.get('age');
        gender = request.POST.get('gender');
        password = request.POST.get('password');
        user = User(name=name, mobile=mobile, age=age, gender=gender, password=password)
        user.save()
        request.session['userName'] = name;
        request.session['mobile'] = mobile;
        request.session['gender'] = gender;


    if request.method == "POST" and request.POST.get('feature') == "calorieCount":
        name = request.session['userName']

        calorieCount = request.POST.get('calorieCount')
        date = datetime.now().strftime("%m/%d/%Y")
        dailyCalorieCount = DailyCalorieCount(name=name, calorieCount=calorieCount, date=date);
        dailyCalorieCount.save()

    if request.method == "POST" and request.POST.get('feature') == "burntCalories":
        name = request.session['userName']

        burntCalories = request.POST.get('burntCalories')
        date = datetime.now().strftime("%m/%d/%Y")
        dailyCaloriesBurnt = DailyCaloriesBurnt(name=name, burntCalories=burntCalories, date=date);
        dailyCaloriesBurnt.save()

    requiredIntake = 0
    if(request.session['gender'] == "Male"):
        requiredIntake = 2500
    if(request.session['gender'] == "Female"):
        requiredIntake = 2000
    date = datetime.now().strftime("%m/%d/%Y")
    calorieCountResult = DailyCalorieCount.objects.raw("Select id, sum(calorieCount) as totalCalorieIntake from home_dailycaloriecount where name = %s and date = %s", (name, date))[0];
    burntCalorieResult = DailyCaloriesBurnt.objects.raw("Select id, sum(burntCalories) as totalCaloriesBurnt from home_dailycaloriesburnt where name = %s and date = %s", (name, date))[0];
    # print(calorieCountResult.totalCalorieIntake, burntCalorieResult.totalCaloriesBurnt)
    return render(request , 'main.html', {'calorieIntake': calorieCountResult.totalCalorieIntake, 'caloriesBurnt': burntCalorieResult.totalCaloriesBurnt, 'requiredIntake': requiredIntake})

def add(request):
    result = Dish.objects.raw("Select * from home_dish");
    return render(request , 'add.html', {'Dishes': result})

def workout(request):
    result1 = Workout.objects.raw("Select * from home_workout");
    #We can also use Workout.objects.all()
    return render(request , 'workout.html', {'Workout': result1})

def user(request):
    return render(request , 'user.html')

def chart(request):
    return render(request , 'chart.html')

