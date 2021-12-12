from django.urls import path

from . import views

app_name = 'regserve'

urlpatterns = [
    path('/students/',
         views.StudentListForm.as_view(),
         name="students"),
    # CRUD for student
    # Create
    path('/students/create',
         views.StudentCreateForm.as_view(),
         name="create_students"),
    # Read
    path('/students/<pk>/',
         views.StudentReadView.as_view(),
         name="student_detail"),
    # Update
    path('/students/<pk>/update',
         views.StudentUpdateForm.as_view(),
         name="student_update"),
    # Delete
    path('/students/<pk>/delete',
         views.StudentDeleteForm.as_view(),
         name="student_update"),
    path('/data/students/',
         views.StudentListCreate.as_view()),
    path('', views.index, name='index')
]
