from django.views.generic import ListView
from django.shortcuts import render
from .models import Student


#class StudentListView(ListView):
#    model = Student
#    ordering = 'group'


def students_list(request):
    template = 'school/student_list.html'
    context = {}
    students = Student.objects.order_by("group")
    context['object_list'] = students
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)
