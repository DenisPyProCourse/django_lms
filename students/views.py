from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import StudentCreateForm
from .forms import StudentFilterForm
from .models import Student


class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'

    def get_queryset(self):
        students_filter = StudentFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headman_group')
        )

        return students_filter


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


class UpdateStudentView(UpdateView):
    pk_url_kwarg = 'identity'
    model = Student
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


def delete_student(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': student})
