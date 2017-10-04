from django.shortcuts import render

from .forms import CommentForm
from .models import Comment


# Create your views here.


def comments(request):
    comments_list = Comment.objects.order_by('-created')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()

    return render(request,
                  'Comments/comment.html', {
                      'comments': comments_list,
                      'form': form
                  })
