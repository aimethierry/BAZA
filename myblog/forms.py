from .models import Post, Answer,Account
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'text', 'field']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    profile_pc = forms.FileField()
    

class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)



class AnswerForm(forms.ModelForm):


    class Meta:
        model = Answer
        fields = ['text',]