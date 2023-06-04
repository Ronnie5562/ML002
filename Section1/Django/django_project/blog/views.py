from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


posts = [
    {
        'title': 'Blog Post 1',
        'author': 'Ronald Abimbola',
        'date_posted': 'February 20, 2023',
        'content': "This is blog post ONE"
    },
    {
        'title': 'Blog Post 2',
        'author': 'Benita Abimbola',
        'date_posted': 'November 12, 2023',
        'content': "This is blog post TWO"
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})