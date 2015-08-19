"""Yogi_Brat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', views.home, name='home'),
    url(r'^yoga/', views.yoga, name='yoga'),
    url(r'^thai_yoga_massage/', views.thai_yoga_massage, name = 'thai_yoga_massage'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^blog/', views.blog, name = 'blog'),
    url(r'^blog/(\d+)/$', views.blog_page, name="blog_page"),
    url(r'^events/', views.events, name = 'events'),
    url(r'^submit_contact', views.submit_contact, name = 'contact'),
    url(r'^quiz$', views.quiz, name ='quiz'),
    url(r'^quiz_results$', views.quiz_results, name = 'quiz_results'),
    # url(r'^course_register', views.course_register, name = 'course_register'),
    # url(r'^appt_scheduler', views.appt_scheduler, name = 'appt_scheduler'),
]
