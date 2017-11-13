from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here
from django.http import HttpResponse
from django.template import Context, loader

from blog.models import Post


# helper function
def encode_url(url):
    return url.replace(' ', '_')


def popular_posts():
    return Post.objects.order_by('-views')[:5]


def index(request):
    latest_posts = Post.objects.all().order_by('-created_at')
    t = loader.get_template('blog/index.html')
    context_dict = {
        'latest_posts': latest_posts,
        'popular_posts': popular_posts(),
    }
    for post in latest_posts:
        post.url = encode_url(post.title)
    for popular_post in popular_posts():
        popular_post.url = encode_url(popular_post.title)
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def post(request, post_url):
    single_post = get_object_or_404(Post, title=post_url.replace('_', ' '))
    # increment the number of views and save it
    single_post.views += 1
    single_post.save()
    t = loader.get_template('blog/post.html')
    context_dict = {
        'single_post': single_post,
        'popular_posts': popular_posts(),
    }
    for popular_post in popular_posts():
        popular_post.url = encode_url(popular_post.title)
    c = Context(context_dict)
    return HttpResponse(t.render(c))
