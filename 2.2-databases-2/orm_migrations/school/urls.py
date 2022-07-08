from django.urls import path


from school.views import students_list

urlpatterns = [
    path('', view=students_list),
]
