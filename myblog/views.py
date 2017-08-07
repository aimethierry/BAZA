from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import User, Post, Answer, Notification, Comment, Project, School, Document
from .forms import PostForm, SignUpForm, AnswerForm, PasswordResetRequestForm,DocumentForm,CommentForm, ProjectForm,UserForm, SchoolForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
#from .filters import UserFilter
import operator
from django.db.models import Q
#from paypal.standard.forms import PayPalPaymentsForm
from django.core.urlresolvers import reverse
import requests 
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from django.views.generic import View
#from django.time import timezone
# class userTimeView(View):
#     template_name='user.html'
#     def get_context_data(self,*args,**kwargs)
#         context = super(userTimeView, self).get_context_data(*args,*kwargs)
#         time=timezone.now()
#         context['time']=time
#         if self.request.user.is_authenticated:
#            self.request.session["time_now"]=time
#         self.request.session["time_out"]=
#         return context

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'myblog/home.html', {'form': form})


@login_required
def model_form_upload(request):
    name = Document.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('model_form_upload')
    else:
        form = DocumentForm()
    return render(request, 'myblog/registration.html', {
        'form': form,'name':name
    })


#home of the platform    
def home(request):
    name = SchoolForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request,'myblog/home.html',{'form':form,'name':name })


def project(request):
    name = Project.objects.all()
    science=Project.objects.filter(field='science').order_by('created_date').reverse()
    arts=Post.objects.filter(field='science').order_by('created_date').reverse()
    skills=Post.objects.filter(field='science').order_by('created_date').reverse()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save()
            return redirect('project')
    else:
        form = ProjectForm()
    return render(request, 'myblog/project.html', {'form': form, 'name':name,'name':name, 'science':science,'arts':arts,'skills':skills})

#teachers
def teachers(request):
    return render(request,'myblog/teachers.html')

def science(request):
    filtered=Post.objects.filter(field='science').order_by('created_date').reverse()
    return render(request, 'myblog/project.html', {'filtered': filtered })

def arts(request):
    filtered=Post.objects.filter(field='arts').order_by('created_date').reverse()
    return render(request, 'myblog/project.html', {'filtered': filtered })

def skills(request):
    filtered=Post.objects.filter(field='skills').order_by('created_date').reverse()
    return render(request, 'myblog/project.html', {'filtered': filtered })


#list of all post
@login_required
def index(request):
    notification_count1=Post.objects.filter(field='Mathematics',check_date=datetime.date.today()).count()
    notification_count2=Post.objects.filter(field='Physics',check_date=datetime.date.today()).count()
    notification_count3=Post.objects.filter(field='Chemistry',check_date=datetime.date.today()).count()
    notification_count4=Post.objects.filter(field='Biology',check_date=datetime.date.today()).count()
    notification_count5=Post.objects.filter(field='Computer',check_date=datetime.date.today()).count()
    notification_count6=Post.objects.filter(field='Economics',check_date=datetime.date.today()).count()
    notification_count7=Post.objects.filter(field='History',check_date=datetime.date.today()).count()
    notification_count8=Post.objects.filter(field='Geography',check_date=datetime.date.today()).count()
    notification_count9=Post.objects.filter(field='Entrepreneurship',check_date=datetime.date.today()).count()
    notification_count10=Post.objects.filter(field='Literature',check_date=datetime.date.today()).count()
    
    notification_count=Notification.objects.filter(created_date=datetime.date.today()).count()
    name = Post.objects.filter().order_by('created_date').reverse()
    context = {'name':name, 'notification_count':notification_count, 'notification_count1':notification_count1,
                'notification_count2':notification_count2,'notification_count3':notification_count3,
                'notification_count4':notification_count4,'notification_count5':notification_count5,
                'notification_count6':notification_count6,'notification_count7':notification_count7,
                'notification_count8':notification_count8,'notification_count9':notification_count9,
                'notification_count10':notification_count10
    }
    return render(request,'myblog/index.html', context)

#change password 
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

#how to add comment to the post
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.post = post
            answer.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = AnswerForm()
    return render(request, 'myblog/answer.html', {'form': form})

# addpost
@login_required
def add(request):
    name = Document.objects.all()
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('add')
    else:
        form = PostForm()
    return render(request, 'myblog/add.html', {'form': form,'name':name })


#save school data
def save_school(request):
    form = SchoolForm()
    if request.method =="POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            name = form.save()
            return redirect('save_school')
    return render(request, 'myblog/home.html', {'form':form})

#question detail
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post})

#comment details post
@login_required
def post_comment(request):
    name = Comment.objects.all()
    return render(request, 'myblog/display_comment.html', {'name': name})
#notifications
@login_required
def notifications(request):
    notifications=Notification.objects.filter(created_date=datetime.date.today()).order_by('created_time').reverse()
    notification_count=Notification.objects.filter(created_date=datetime.date.today()).count()
    return render(request,'myblog/notification.html',{'notifications':notifications,'notification_count':notification_count})

#new its a new index which ill be following
@login_required
def new(request):
    name = Post.objects.all().order_by('created_date').reverse()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('new')
    else:
        form = PostForm()
    return render(request, 'myblog/new.html', {
        'form': form, 'name':name})


#answ
def answ(album_id, request):
    name = get_object_or_404(Document, pk=album_id)
    context = {'name':name}
    return render(request,'myblog/answer.html', context)


def post(request):
    name = Document.objects.all()
    return render(request,'home.html',{'name':name})




@login_required
def answer(request, pk_id):
    post = get_object_or_404(Post, pk=pk_id )
    return render(request, 'myblog/answer.html', {'post': post})

#comment on an answer
def comment(request):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.post = post
            answer.save()
            return redirect('new', pk=post.pk)
    else:
        form = AnswerForm()
    return render(request,'myblog/yy.html', {'name':name})




def detail(request):
    filtered=Post.objects.filter(field='Mathematics').order_by('created_date').reverse()
    return render(request,'myblog/yy.html', { 'filtered':filtered})
    
#display comment
def display_comment(request):
    name = Comment.objects.all()
    return render(request,'myblog/comment.html', {'name':name})

@login_required
def chemistry(request):
    filtered=Post.objects.filter(field='Chemistry').order_by('created_date').reverse()
    return render(request, 'myblog/chem.html', {'filtered': filtered })


@login_required
def math(request):
    filtered=Post.objects.filter(field='Mathematics').order_by('created_date').reverse()
    return render(request, 'myblog/math.html', {'filtered': filtered})

@login_required
def computer(request):
    filtered=Post.objects.filter(field= 'Computer').order_by('created_date').reverse()
    return render(request, 'blog/computer.html', {'filtered': filtered})

@login_required
def history(request):
    filtered=Post.objects.filter(field= 'History').order_by('created_date').reverse()
    return render(request, 'myblog/hist.html', {'filtered': filtered})

@login_required
def economics(request):
    filtered=Post.objects.filter(field= 'Economics').order_by('created_date').reverse()
    return render(request, 'myblog/econ.html', {'filtered': filtered})

@login_required
def geography(request):
    filtered=Post.objects.filter(field= 'Geography').order_by('created_date').reverse()
    return render(request, 'myblog/geo.html', {'filtered': filtered})

def literature(request):

    filtered=Post.objects.filter(field= 'Literature').order_by('created_date').reverse()
    return render(request, 'myblog/lit.html', {'filtered': filtered})


def biology(request):
    filtered=Post.objects.filter(field= 'Biology').order_by('created_date').reverse()
    return render(request, 'myblog/bio.html', {'filtered': filtered})


@login_required
def physics(request):
    name=Post.objects.filter(field='Physics').order_by('created_date').reverse()
    return render(request, 'myblog/phy.html', {'name': name })


   

@login_required
def entrepreneurship(request):
    filtered=Post.objects.filter(field= 'Entrepreneurship').order_by('created_date').reverse()
    return render(request, 'myblog/ent.html', {'filtered': filtered})

@login_required
def computer(request):
    filtered=Post.objects.filter(field= 'Computer').order_by('created_date').reverse()
    return render(request, 'blog/comp.html', {'filtered': fitlered})
