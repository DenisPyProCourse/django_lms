from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import GroupUpdateForm
from .models import Group


def create_group(request):
    pass


def delete_group(request, pk):
    pass


def get_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups/list.html', {'groups': groups})


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupUpdateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupUpdateForm(instance=group)

    return render(request, 'groups/update.html', {'form': form, 'group': group})
