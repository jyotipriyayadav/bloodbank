from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),

    path('about/',views.about,name='about'),

    path('contact/',views.contact,name='contact'),

    path('register/',views.register,name='register'),

    path('login/',views.login,name='login'),

    path('donor-dashboard/',views.donor_dashboard,name='donor_dashboard'),

    path('donate-blood/',views.donate_blood,name='donate_blood'),

    path('blood-request/',views.blood_request,name='blood_request'),

    path('blood-availability/',views.blood_availability,name='blood_availability'),

    path('admin-dashboard/',views.admin_dashboard,name='admin_dashboard'),

    path('manage-donors/',views.manage_donors,name='manage_donors'),

    path('manage-requests/',views.manage_requests,name='manage_requests'),

    path('delete-donor/<int:id>/',views.delete_donor,name='delete_donor'),
    
    path('approve-request/<int:id>/',views.approve_request,name='approve_request'),
    
    path('reject-request/<int:id>/',views.reject_request,name='reject_request'),

    path('logout/',views.logout,name='logout'),
  
    path('delete-request/<int:id>/',views.delete_request,name='delete_request'),

    path('update-profile/',views.update_profile,name='update_profile'),

    path('edit-donor/<int:id>/',views.edit_donor,name='edit_donor'),

]