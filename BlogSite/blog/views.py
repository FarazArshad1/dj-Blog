from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.views.generic import ListView
from .models import Post
import sys

def printError(e):
    error_type = type(e).__name__
    line_number = sys.exc_info()[-1].tb_lineno
    if e.args:
        error_name = e.args[0]
    else:
        error_name = "No additional information available"
    error_msg = f"Error Type: {error_type}\nError Name: {error_name}\nLine where error occurred: {line_number}"
 
    print(error_msg)

class PostListView(ListView):

    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'


def post_list(request):
    try:
        post_list = Post.published.all()
        
        # Pagination with 3 posts per page
        paginator = Paginator(post_list,3)
        page_number = request.GET.get('page')
        
        try:
            posts = paginator.page(page_number)
        except PageNotAnInteger:
            # If page_number is not an integer get the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If page_number is out of range get last page of result
            posts = paginator.page(paginator.num_pages)

        return render(
            request,
            'list.html',
            {'posts': posts}
        )
    
    except Exception as e:
        printError(e)
        render(
            request,
            'list.html',
            {'posts': posts}
        )


def post_detail(request, year, month, day, post):
    try:
        post = get_object_or_404(
            Post,
            status=Post.Status.PUBLISHED,
            slug=post,
            publish__year=year,
            publish__month=month,
            publish__day=day
        )
        return render(
            request,
            'detail.html',
            {'post': post}
        )
    except Exception as e:
        printError(e)
        return render(
            request,
            'detail.html',
            {'post': "This Blog can't be fetched at this moment"}
        )
