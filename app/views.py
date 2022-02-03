from django.shortcuts import render

# Create your views here.
def nav(request):
    return render(request,'navbar.html')
def team(request):
    return render(request,'Trainer_Team.html')
def current(request):
    return render(request,'Trainer_Current_Team.html')
def task(request):
    return render(request,'Trainer_Current_task.html')
def ass(request):
    return render(request,'Trainer_Current_Assignd.html')
def Trainees(request):
    return render(request,'Trainer_Current_Trainees.html')
def Empdetails(request):
    return render(request,'Trainer_Current_Empdetails.html')

def Attendance(request):
    return render(request,'Trainer_Current_Attendance.html')
def task1(request):
    return render(request,'Trainer_Current_task1.html')
def List(request):
    return render(request,'Trainer_Current_AttendanceList.html')
def tdetails(request):
    return render(request,'Trainer_Current_Taskdetails.html')