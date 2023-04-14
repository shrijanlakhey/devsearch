from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        # django's gonna look at this model(i.e Project) and it's gonna create a form based on this model
        # it's gonna look at all of the attributes, see the type of fields and generate a from
        # since  "fields = '__all__' ", it's going to generate a field for attribute of the model
        # but id won't be there because it is not editable
        # and created won't be there because it is automatically generated
        model = Project 
        fields = '__all__'