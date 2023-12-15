"""
URL configuration for wscubetech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from wscubetech import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home , name="home"),
    path('about/',views.aboutUs, name="about"),
    path('contact/',views.contactus,name="contact"),
    path('calculator/',views.calculator,name="calculator"),
    path('evenodd/',views.saveevenodd),
    path('marklist/',views.marklist),
    path('services/',views.services,name="services"),
    path('webdesignservice/',views.web,name="web"),
    path('uiux/',views.uiux,name="uiux"),
    path('appdev/',views.appdev,name="appdev"),
    path('enquiry/',views.enquiry,name="enquiry"),
   ]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 