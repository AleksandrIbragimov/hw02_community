from django.shortcuts import render, get_object_or_404

from .models import Post, Group

NUMBER_OF_LAST_POSTS = 10


def index(request):
    posts = Post.objects.select_related('group').all()[:NUMBER_OF_LAST_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUMBER_OF_LAST_POSTS]
    context = {
        'posts': posts,
        'group': group,
    }
    return render(request, 'posts/group_list.html', context)


'''
def index(request):
    author = User.objects.get(username='leo')
    keyword = "утро"
    start_date = datetime.date(1854, 7, 7)
    end_date = datetime.date(1854, 7, 21)
    posts = Post.objects.filter(
        text__contains=keyword
    ).filter(
        author=author
    ).filter(
        pub_date__range=(start_date, end_date)
    )
    return render(request, "index.html", {"posts": posts})
'''
