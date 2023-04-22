from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        # django's gonna look at this model(i.e Project) and it's gonna create a form based on this model
        # it's gonna look at the specified attributes, see the type of fields and generate a from
        model = Project 
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']

        # modifying the widgets
        widgets = {
            'tags': forms.CheckboxSelectMultiple(), 
        }
    
    # overwriting __init__ method
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input'}) # updatiing class attributes 'class' is set to 'input' because I want to get the css for the input class

        for name, field in self.fields.items(): # name = key, field = value
            field.widget.attrs.update({'class':'input'})