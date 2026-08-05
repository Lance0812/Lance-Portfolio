from django.shortcuts import render
from .models import Project, PersonalInformation

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


from .models import Project


def projects(request):

    projects = Project.objects.all()

    return render(
        request,
        "projects.html",
        {
            "projects": projects
        }
    )

from django.shortcuts import render

def contact(request):

    personal_info = PersonalInformation.objects.first()

    return render(
        request,
        "contact.html",
        {
            "personal_info": personal_info
        }
    )


    if request.method == "POST":

        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )


    return render(
        request,
        "contact.html",
        {
            "personal_info": personal_info
        }
    )

def project_detail(request, id):

    project = Project.objects.get(id=id)

    return render(
        request,
        "project_detail.html",
        {
            "project": project
        }
    )
    projects = [
        {
            "id": 1,
            "title": "Personal Portfolio Website",
            "description": "A responsive portfolio website created using Django.",
            "tech": "HTML, CSS, JavaScript, Django",
            "github": "https://github.com/yourusername"
        },

        {
            "id": 2,
            "title": "Student Grade Calculator",
            "description": "A program that calculates student grades.",
            "tech": "C++, Object-Oriented Programming",
            "github": "https://github.com/yourusername"
        },

        {
            "id": 3,
            "title": "Smart Temperature Monitor",
            "description": "An IoT project that monitors temperature.",
            "tech": "Arduino C++, Sensors",
            "github": "https://github.com/yourusername"
        }
    ]


    project = None

    for item in projects:
        if item["id"] == id:
            project = item


    return render(
        request,
        "project_detail.html",
        {"project": project}
    )
