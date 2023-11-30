from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, SubjectViewSet, MarksViewSet, JSONDataViewSet, RankViewSet

app_name = 'student'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'marks', MarksViewSet, basename='marks')
router.register(r'json-data', JSONDataViewSet, basename='json-data')
router.register(r'rank', RankViewSet, basename='rank')
 
urlpatterns = [
    path('', include(router.urls)),
    # Add the following lines for the Add views
    path('add-student/', StudentViewSet.as_view({'post': 'create'}), name='add-student'),
    path('add-subject/', SubjectViewSet.as_view({'post': 'create'}), name='add-subject'),
    path('add-marks/', MarksViewSet.as_view({'post': 'create'}), name='add-marks'),
]
