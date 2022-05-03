from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
from .utils import qs2html

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

    html = qs2html(st)
    return HttpResponse(html)
