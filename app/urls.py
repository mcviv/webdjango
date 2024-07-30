"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('save', views.save, name='save'),
    path('edit/<id>', views.editstudent, name='edit'),
    path('delete/<id>', views.deletestudent, name='delete'),
    path('students/', views.student_list, name='list'),
    path('daraja/stk_push', views.stk_push_callback, name='stk_push_callback'),
    path('mpesaapi/', views.mpesaapi, name='mpesaapi')

]
