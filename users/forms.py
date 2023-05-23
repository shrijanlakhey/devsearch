from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm): # 'CustomUserCreationForm(UserCreationForm)' means that CustomUserCreationForm inherist from UserCreationForm
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2' ]
        # modifying how the name of fields will be displyed
        labels = {
            'first_name': 'Name',
        }