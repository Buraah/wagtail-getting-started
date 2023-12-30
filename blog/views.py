from django.shortcuts import render
from .models import BlogPage

# Create your views here.
def index(request):
    return render(request, 'blog/blog_index_page.html')

def blog_index(request):
    blogpages = BlogPage.objects.all()
    return render(request, 'blog/blog_index_page.html', {'blogpages': blogpages})