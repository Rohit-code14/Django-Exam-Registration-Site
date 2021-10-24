from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def baseRedirect(request):
    return redirect('accounts/register')

@login_required(login_url='accounts/login')
def dashboard(request):
    exam = Exam.objects.order_by('-date_created')
    stu = Student.objects.all()
    # for ex in exam:
    #     ex.is_selected = False
    # exam.save()
    data = {
        'exam':exam,
        'stu': stu
    }
    return render(request,'dashboard.html',data)


@login_required(login_url='accounts/login')
def registerExam(request):
    exam = Exam.objects.all()
    if request.method == 'POST':
        stu = Student.objects.order_by('name').get(name = request.POST['username'])
        for ex in exam:
            if request.POST.get(ex.examCode,False):
                regExam = RegisteredExam(student = stu,exam = ex)
                regExam.save()
        return redirect('displaySelected')
    return render(request,'four04.html')



@login_required(login_url='accounts/login')
def displaySelected(request):
    regExam = RegisteredExam.objects.all().distinct()
    data = {
        'regExam':regExam
    }
    return render(request,'display.html',data)




