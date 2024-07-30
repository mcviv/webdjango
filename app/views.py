from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django_daraja.mpesa.core import MpesaClient

from app.models import students
from app.serializers import studentserializer


# Create your views here.
def index(request):
    data = students.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context)

def save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        form = students(name=name, email=email, age=age, gender=gender, location=location)
        form.save()
        return redirect("/")
    return render(request, 'index.html')

def editstudent(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        location = request.POST.get('location')

        editForm = students.objects.get(id=id)
        editForm.name = name
        editForm.email = email
        editForm.age = age
        editForm.gender = gender
        editForm.location = location
        editForm.save()
        return redirect("/")
    student = students.objects.get(id=id)
    context = {'student': student}
    return render(request, 'edit.html', context)


def deletestudent(request, id):
    student = students.objects.get(id=id)
    student.delete()
    return redirect("/")

def student_list(request):
    student = students.objects.all()
    serializer = studentserializer(student, many=True)
    return JsonResponse(serializer.data, safe=False)


def mpesaapi(request):
    cl = MpesaClient()
    phone_number = '0706314626'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
    data = request.body
    return HttpResponse('STK PUSH has been sent successfully')