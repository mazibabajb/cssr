from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('about', views.about, name ='about'),
    path('contact', views.contact, name ='contact'),
    path('business', views.business, name ='business'),
    path('hospitality', views.hospitality, name ='hospitality'),
    path('hrm', views.hrm, name ='hrm'),
    path('accounting', views.accounting, name ='accounting'),
    path('businessm', views.businessm, name ='businessm'),
    path('social', views.social, name ='social'),
    path('blog', views.blog, name ='blog'),
    path('marketing', views.marketing, name ='marketing'),
    path('businessm', views.businessm, name ='businessm'),
    path('hac', views.hac, name ='hac'),
    path('tourism', views.tourism, name ='tourism'),
    path('register', views.register, name ='register'),
    path('admissions', views.admissions, name ='admissions'),
    path('infomation', views.infomation, name ='infomation'),
    path('fees', views.fees, name ='fees'),
    
    




]
