from django.urls import path
from . import views


urlpatterns = [

    path(
        'sign-in/',
        views.sign_in,
        name='sign_in'
    ),

    path(
        'sign-out/',
        views.sign_out,
        name='sign_out'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'dashboard/projects/create/',
        views.create_project,
        name='create_project'
    ),

    path(
    'dashboard/projects/<int:id>/edit/',
    views.edit_project,
    name='edit_project'
),

    path(
        'dashboard/tech-stacks/create/',
        views.create_tech_stack,
        name='create_tech_stack'
    ),

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'projects/',
        views.projects,
        name='projects'
    ),

    path(
        'projects/<int:id>/',
        views.project_detail,
        name='project_detail'
    ),

    path(
        'add-project/',
        views.add_project,
        name='add_project'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),

    path(
        'testimony/',
        views.add_testimony,
        name='add_testimony'
    ),

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