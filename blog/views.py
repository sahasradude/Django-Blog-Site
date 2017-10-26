from django.shortcuts import render, get_object_or_404
from .models import *
from django.utils import timezone
from .forms import *
from django.forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
# Create your views here.
def subscribe (request, sub_pk):
    topic = get_object_or_404(Topic, topic_title=sub_pk)
    subslist, created = Subscribe.objects.get_or_create(username=request.user, topic_title=topic)
    if created == True:
        subslist.save()
        topic.number_followers += 1
        topic.save()
    return redirect('topic', topic_pk=sub_pk) 

def post_list (request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    topics = Topic.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'topics': topics})

def subscriptions(request):
    subs=Subscribe.objects.filter(username=request.user)
    return render(request, 'blog/subscribe.html', {'subs':subs})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html', {})

def topic(request, topic_pk):
    topic_posts = Post.objects.filter(post_topic__topic_title=topic_pk)
    title = topic_pk
    subs = get_object_or_404(Topic, topic_title=topic_pk)
    subno = subs.number_followers
    return render(request, 'blog/topic.html', {'topic_posts': topic_posts, 'title': title, 'subno': subno})
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@csrf_protect
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email']
			)
			return HttpResponseRedirect('/success/')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {
	'form': form
	})

	return render_to_response(
	'registration/register.html',
	variables,
	)

def register_success(request):
	return render_to_response(
	'registration/success.html',
	)

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def home(request):
	#return render_to_response(
	#'blog/post_list.html',
	#{ 'user': request.user }
	#)
        return redirect('post_list')
