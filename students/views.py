from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import StudentCreateForm
from .forms import StudentFilterForm
from .models import Student


def get_students(request):
    students = Student.objects.all()
    students_filter = StudentFilterForm(data=request.GET, queryset=students)

    return render(
        request,
        'students/list.html',
        {'students_filter': students_filter}
    )


def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    else:
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/create.html',
        context={'form': form}
    )


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        form = StudentCreateForm(instance=student)
    else:
        form = StudentCreateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/update.html', {'form': form})


def delete_student(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': student})
