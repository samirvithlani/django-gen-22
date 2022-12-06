from django.shortcuts import render
from . forms import StudentForm
from . models import Student1

# Create your views here.
def student_create_view(request):
    context ={}
    
    form = StudentForm(request.POST or None)
    #validate the form
    if form.is_valid():
        form.save()
    
    context['form']=form
    return render(request,"crud1/student_create.html",context)
