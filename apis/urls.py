# inquiries/urls.py
from django.urls import path
from .views import school_partnership_inquiry
from .views import enrollment_inquiry

urlpatterns = [
    path('school-partnership/', school_partnership_inquiry),
    path('enrollment/', enrollment_inquiry, name='enrollment'),
]
