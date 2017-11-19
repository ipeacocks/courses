from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render, redirect

from blog.models import Post
from blog.forms import PostForm



####################
# helper functions #
####################

def encode_url(url):
    return url.replace(' ', '_')


def get_popular_posts():
    return Post.objects.order_by('-views')[:5]


##################
# view functions #
##################

def index(request):
    latest_posts = Post.objects.all().order_by('-created_at')
    t = loader.get_template('blog/index.html')
    context_dict = {
        'latest_posts': latest_posts,
        'popular_posts': get_popular_posts(),
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def post(request, slug):
    single_post = get_object_or_404(Post, slug=slug)
    # increment the number of views and save it
    single_post.views += 1
    single_post.save()
    t = loader.get_template('blog/post.html')
    context_dict = {
        'single_post': single_post,
        'popular_posts': get_popular_posts(),
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            # title_value = form.cleaned_data['title']
            # redirect_link = ('/blog/{}/').format(encode_url(title_value))
            return redirect(index)
        else:
            print(form.errors)
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})
