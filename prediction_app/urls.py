from django.urls import path
from . import views

urlpatterns = [
    # عندما يكتب المستخدم الرابط، يتم تشغيل دالة predict_diabetes
    path('predict/', views.predict_diabetes, name='predict'),
]