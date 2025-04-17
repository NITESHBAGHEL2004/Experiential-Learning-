from django.urls import path
from myapp import views



urlpatterns = [
    path('get_schools/<int:academic_year_id>/', views.get_schools, name='get_schools'),
    path('get_programs/<int:school_id>/', views.get_programs, name='get_programs'),
    path('get_branches/<int:program_id>/', views.get_branches, name='get_branches'),
    path('get_facultys/<int:branch_id>/', views.get_facultys, name='get_facultys'),
    path('get_semesters/<int:faculty_id>/', views.get_semesters, name='get_semesters'),
    path('get_sections/<int:semester_id>/', views.get_sections, name='get_sections'),
    path('get_subjects/<int:section_id>/', views.get_subjects, name='get_subjects'),
    path('get_pbls/<int:subject_id>/', views.get_pbls, name='get_pbls'),
    path('', views.dropdown_page, name='index'),
    #part edit
    path('get_schools/<int:academic_year_id>/', views.get_schools, name='get_schools'),
    path('get_programs/<int:school_id>/', views.get_programs, name='get_programs'),
    path('get_facultys/<int:program_id>/', views.get_facultys, name='get_facultys'),
    path('edit', views.pbl_activity_view, name='pbl_activity_view'),
    path('home', views.dropdown_page, name='index'),
    path('update_activity/', views.update_activity, name='update_activity'),
    
    #pert report
    path('report', views.pbl_activity, name='pbl_activity'),
    path('uploads/', views.pbl_activity, name='pbl_activity')
    
   

]