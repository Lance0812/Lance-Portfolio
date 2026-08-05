from django.urls import path
from . import views


urlpatterns = [

    path('',views.home,name='home'),

    path('about/',views.about,name='about'),

    path('projects/',views.projects,name='projects'),

    path('projects/<int:id>/',views.project_detail,name='project_detail'),


    path('add-project/',views.add_project,name='add_project'),


    path('contact/',views.contact,name='contact'),


    path('testimony/',views.add_testimony,name='add_testimony'),

    path(
        'testimonies/',
        views.TestimonyListView.as_view(),
        name='testimony_list'
    ),


    path(
        'testimony/<int:id>/',
        views.testimony_detail,
        name='testimony_detail'
    ),

]