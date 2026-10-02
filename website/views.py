from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView

from .models import Project, PersonalInformation, Testimony, TechStack
from .forms import ProjectForm, InquiryForm, TestimonyForm, TechStackForm


def sign_in(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_superuser:

            login(request, user)

            return redirect('dashboard')

        return render(
            request,
            'sign_in.html',
            {
                'error': 'Invalid username or password.'
            }
        )

    return render(
        request,
        'sign_in.html'
    )


def sign_out(request):

    logout(request)

    return redirect('sign_in')


def is_superuser(user):

    return user.is_authenticated and user.is_superuser


@login_required(login_url='sign_in')
@user_passes_test(is_superuser, login_url='sign_in')
def dashboard(request):

    projects = Project.objects.all()
    tech_stacks = TechStack.objects.all()

    return render(
        request,
        'dashboard.html',
        {
            'projects': projects,
            'tech_stacks': tech_stacks
        }
    )


@login_required(login_url='sign_in')
@user_passes_test(is_superuser, login_url='sign_in')
def create_tech_stack(request):

    if request.method == "POST":

        form = TechStackForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = TechStackForm()

    return render(
        request,
        'create_tech_stack.html',
        {
            'form': form
        }
    )


@login_required(login_url='sign_in')
@user_passes_test(is_superuser, login_url='sign_in')
def create_project(request):

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = ProjectForm()

    return render(
        request,
        'create_project.html',
        {
            'form': form
        }
    )

@login_required(login_url='sign_in')
@user_passes_test(is_superuser, login_url='sign_in')
def edit_project(request, id):

    project = get_object_or_404(
        Project,
        id=id
    )

    if request.method == "POST":

        form = ProjectForm(
            request.POST,
            instance=project
        )

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = ProjectForm(
            instance=project
        )

    return render(
        request,
        'edit_project.html',
        {
            'form': form,
            'project': project
        }
    )

def home(request):

    return render(
        request,
        'home.html'
    )


def about(request):

    personal_info = PersonalInformation.objects.first()

    return render(
        request,
        'about.html',
        {
            'personal_info': personal_info
        }
    )


def projects(request):

    projects = Project.objects.all()

    return render(
        request,
        'projects.html',
        {
            'projects': projects
        }
    )


def project_detail(request, id):

    project = get_object_or_404(
        Project,
        id=id
    )

    return render(
        request,
        'project_detail.html',
        {
            'project': project
        }
    )


@login_required(login_url='sign_in')
@user_passes_test(is_superuser, login_url='sign_in')
def add_project(request):

    if request.method == "POST":

        form = ProjectForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('projects')

    else:

        form = ProjectForm()

    return render(
        request,
        'add_project.html',
        {
            'form': form
        }
    )


def contact(request):

    if request.method == "POST":

        form = InquiryForm(request.POST)

        if form.is_valid():

            form.save()

            return render(
                request,
                'contact_success.html'
            )

    else:

        form = InquiryForm()

    return render(
        request,
        'contact.html',
        {
            'form': form
        }
    )


def add_testimony(request):

    if request.method == "POST":

        form = TestimonyForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('testimony_list')

    else:

        form = TestimonyForm()

    return render(
        request,
        'testimony.html',
        {
            'form': form
        }
    )


class TestimonyListView(ListView):

    model = Testimony
    template_name = 'testimony_list.html'
    context_object_name = 'testimonies'


def testimony_detail(request, id):

    testimony = get_object_or_404(
        Testimony,
        id=id
    )

    return render(
        request,
        'testimony_detail.html',
        {
            'testimony': testimony
        }
    )