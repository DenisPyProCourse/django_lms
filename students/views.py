from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import StudentCreateForm
from .models import Student

from webargs.fields import Str, Int
from webargs.djangoparser import use_args


@use_args(
    {
        'first_name': Str(required=False),       # , missing=None)
        'last_name': Str(required=False),
        'age': Int(required=False)
    },
    location='query'
)
def get_students(request, args):
    st = Student.objects.all()
    for key, value in args.items():
        st = st.filter(**{key: value})      # key=value

    return render(
        request,
        'students/list.html',
        {'title': 'List of students', 'students': st}
    )


def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    else:
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('list'))

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

            return HttpResponseRedirect(reverse('list'))

    return render(request, 'students/update.html', {'form': form})


def delete_student(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('list'))

    return render(request, 'students/delete.html', {'student': student})
