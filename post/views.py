from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict
from django.views import View

from user.models import User

from .forms import MessageForm, CommentForm
from .models import Post


# Create your views here.
class PostView(View):
    def get(self, request, user_id=None, post_id=None):
        if post_id:
            return redirect('/post/' + str(user_id))

        if user_id:
            user = User.objects.get(id=user_id)
            post = Post.objects.filter(user=user)

            return render(request, "post/post.html", {"user": user, "post": post, "msgform": MessageForm,
                          "cmtform": CommentForm})

        else:
            users = User.objects.all()

            for user in users:
                post = Post.objects.filter(user=user)
                user.total_messages = len(post)
                thumbs = 0

                for thumb in post:
                    thumbs += thumb.thumbs

                user.total_thumbs = thumbs
                user.save()

            return render(request, "post/post_list.html", {"post": User.objects.all()})

    def post(self, request, user_id, post_id=None):
        message = request.POST.get("message", None)
        comment = request.POST.get("comment", None)
        thumbs = request.POST.get("thumbs", None)

        if thumbs and post_id:
            post = Post.objects.get(id=post_id)
            post.thumbs += 1

            post.save()

        if message:
            Post.objects.create(user=User.objects.get(id=user_id), message=message)

        elif comment and post_id:
            post = Post.objects.get(id=post_id)

            post.comment = comment
            post.save()

        return redirect("/post/{}".format(user_id))

    def delete(self, request, user_id=None, post_id=None):
        try:
            post = Post.objects.get(id=post_id)
        except:
            return HttpResponse(status=400)

        post.delete()

        return HttpResponse(status=200)
