from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        # django's gonna look at this model(i.e Project) and it's gonna create a form based on this model
        # it's gonna look at the specified attributes, see the type of fields and generate a from
        model = Project 
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']