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

def student_list_view(request):
    context ={}
    context['students'] = Student1.objects.all()
    return render(request,"crud1/student_list.html",context)

#delete from student where id =1
def student_delete_view(request,id):
    context ={}
    #orm -> id --> object fetch --> delete
    student = Student1.objects.get(id=id)
    #request method must be post
    if request.method =="POST":
        student.delete()

    return render(request,"crud1/student_delete.html",context)     
