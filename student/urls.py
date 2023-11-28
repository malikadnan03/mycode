# student/urls.py
from django.urls import path
from .views import AddStudentFormView, AddSubjectFormView, AddMarksFormView, StudentAPIView, SubjectAPIView, MarksAPIView, JSONDataView, RankAPIView

app_name = 'student'

urlpatterns = [
    path('add-student-form/', AddStudentFormView.as_view(), name='add-student-form'),
    path('add-subject-form/', AddSubjectFormView.as_view(), name='add-subject-form'),
    path('add-marks-form/', AddMarksFormView.as_view(), name='add-marks-form'),
    path('add-student/', StudentAPIView.as_view(), name='add-student'),
    path('add-subject/', SubjectAPIView.as_view(), name='add-subject'),
    path('add-marks/', MarksAPIView.as_view(), name='add-marks'),
    path('json-data/', JSONDataView.as_view(), name='json-data'),
    path('calculate-rank/', RankAPIView.as_view(), name='calculate-rank'),  # Add this line for the RankAPIView
]
