"""
URL configuration for anesthesia_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# anesthesia_project/urls.py
from django.contrib import admin
from django.urls import path, include
from patient_records import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patient_records.urls')),  # Includes patient_records URLs
    path ('', views.home, name='home'),
]