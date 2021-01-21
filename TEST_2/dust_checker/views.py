from django.shortcuts import render
from .api import check_air
from .api import tags


def index(request):
    res = check_air("pm10", "daegu")
    pm10 = int(res[0])
    res = check_air("pm25", "daegu")
    pm25 = int(res[0])
    if(pm10 <= 30): pm10grade = "좋음"
    elif(pm10 <= 80): pm10grade = "보통"
    elif(pm10 <= 150): pm10grade = "나쁨"
    else: pm10grade = "매우나쁨"
    if(pm25 <= 15): pm25grade = "좋음"
    elif(pm25 <= 35): pm25grade = "보통"
    elif(pm25 <= 75): pm25grade = "나쁨"
    else: pm25grade = "매우나쁨"
    context = {'pm10grade': pm10grade, 'pm25grade': pm25grade,'pm10value' : pm10,'pm25value' : pm25}
    return render(request, 'dust_checker/main.html', context)

def detail(request, itemCode):
    res = check_air(itemCode, "all")
    resDic = dict(zip(tags, res))
    context = {'dust': resDic}
    return render(request, 'dust_checker/detail.html', context)

def robot(request):

    return render(request, 'robot.html')

def server(request):
    return render(request, 'getserver.php')