# student_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('student.urls')),  # Include the app's URLs here
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('add-student/', TemplateView.as_view(template_name='add_student.html'), name='add-student'),
    path('add-marks/', TemplateView.as_view(template_name='add_marks.html'), name='add-marks'),
    path('add-subject/', TemplateView.as_view(template_name='add_subject.html'), name='add-subject'),
    path('calculate-rank/', TemplateView.as_view(template_name='student_rank.html'), name='calculate-rank'),

]
