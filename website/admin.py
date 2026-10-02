from django.contrib import admin
from .models import PersonalInformation, Project, Testimony, Inquiry, TechStack


admin.site.register(PersonalInformation)
admin.site.register(Project)
admin.site.register(Testimony)
admin.site.register(Inquiry)
admin.site.register(TechStack)