from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Post, Answer, Notification
from .forms import PostForm, SignUpForm, AnswerForm, PasswordResetRequestForm
from django.contrib.auth import authenticate,login, logout
from django.core.files.storage import FileSystemStorage
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail


send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)



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


# addpost
@login_required
def add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('add')
    else:
        form = PostForm()
    return render(request, 'myblog/add.html', {'form': form})


#question detail
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post})

#notifications
@login_required
def notifications(request):
    notifications=Notification.objects.filter(created_date=datetime.date.today()).order_by('created_time').reverse()
    notification_count=Notification.objects.filter(created_date=datetime.date.today()).count()
    return render(request,'myblog/notification.html',{'notifications':notifications,'notification_count':notification_count})


#signup
@login_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})

#answer

@login_required
def answer(request, pk):
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
    filtered=Post.objects.filter(field= 'Computer')
    return render(request, 'blog/computer.html', {'filtered': filtered})

@login_required
def history(request):
    filtered=Post.objects.filter(field= 'History')
    return render(request, 'blog/history.html', {'posts': posts})

@login_required
def economics(request):
    filtered=Post.objects.filter(field= 'Economics')
    return render(request, 'blog/economics.html', {'posts': posts})

@login_required
def geography(request):
    filtered=Post.objects.filter(field= 'Geography')
    return render(request, 'blog/geography.html', {'posts': posts})

def literature(request):

    filtered=Post.objects.filter(field= 'Literature')
    return render(request, 'blog/literature.html', {'posts': posts})


def biology(request):
    filtered=Post.objects.filter(field= 'Biology')
    return render(request, 'blog/biology.html', {'filtered': filtered})


def physics(request):
    filtered=Post.objects.all()
    context = {'filtered': filtered}
    return render(request, 'myblog/phy.html', context)

   

@login_required
def entrepreneurship(request):
    filtered=Post.objects.filter(field= 'Entrepreneurship')
    return render(request, 'blog/ent.html', {'posts': posts})

@login_required
def computer(request):
    filtered=Post.objects.filter(field= 'Computer')
    return render(request, 'blog/comp.html', {'posts': posts})
