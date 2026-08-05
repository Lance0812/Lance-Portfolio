from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import Project, PersonalInformation, Testimony
from .forms import ProjectForm, InquiryForm, TestimonyForm



def home(request):
    return render(request, 'home.html')



def about(request):
    personal_info = PersonalInformation.objects.first()

    return render(request, 'about.html',{
        'personal_info': personal_info
    })



def projects(request):
    projects = Project.objects.all()

    return render(request,'projects.html',{
        'projects':projects
    })



def project_detail(request,id):

    project = get_object_or_404(Project,id=id)

    return render(request,'project_detail.html',{
        'project':project
    })



def add_project(request):

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('projects')

    else:

        form = ProjectForm()


    return render(request,'add_project.html',{
        'form':form
    })



def contact(request):

    if request.method == "POST":

        form = InquiryForm(request.POST)

        if form.is_valid():

            form.save()

            return render(request,'contact_success.html')

    else:

        form = InquiryForm()


    return render(request,'contact.html',{
        'form':form
    })



def add_testimony(request):

    if request.method == "POST":

        form = TestimonyForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('testimony_list')


    else:

        form = TestimonyForm()


    return render(request,'testimony.html',{
        'form':form
    })



class TestimonyListView(ListView):

    model = Testimony

    template_name = "testimony_list.html"

    context_object_name = "testimonies"



def testimony_detail(request,id):

    testimony = get_object_or_404(Testimony,id=id)


    return render(request,'testimony_detail.html',{
        'testimony':testimony
    })