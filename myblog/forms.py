from .models import Post, Answer,Account, Comment, Project, School, Document,Teacher
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions



class UserForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    school_name = forms.CharField(max_length=300)
    class Meta:
        model = User
        fields = ('username', 'email')

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'text', 'document']


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
        fields = ['text']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['first_name', 'last_name', 'email', 'field','text','image']

class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ['school_email','school_name','adress']


    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document','text')


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )

