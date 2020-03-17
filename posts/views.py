from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe
# from django.template import loader
from bleach import ALLOWED_TAGS, ALLOWED_ATTRIBUTES
from bleach.sanitizer import Cleaner

from .models import Post

VALID_TAGS = ['img', 'p', 'strike', 'br',
              'span', 'blockquote', 'pre'] + ALLOWED_TAGS

VALID_ATTR = ALLOWED_ATTRIBUTES
VALID_ATTR['img'] = ['src', 'alt', 'rel']

cleaner = Cleaner(tags=VALID_TAGS, attributes=VALID_ATTR)


def index(req):
    orders = {'creation-date': '-creationDate',
              'view-count': 'viewCount',
              'score': 'score'
              }

    order = req.GET.get('order', 'creation-date')
    posts = list(Post.objects.filter(postTypeId=1).order_by(orders[order]))

    for i, e in enumerate(posts):
        posts[i].body = mark_safe(cleaner.clean(posts[i].body))
        posts[i].title = mark_safe(cleaner.clean(posts[i].title))

    context = {'posts': posts}
    return render(req, 'posts/index.html', context)


def view(req, post_id):
    question = Post.objects.get(id=post_id)
    question.body = mark_safe(cleaner.clean(question.body))
    question.title = mark_safe(cleaner.clean(question.title))
    answers = list(Post.objects.filter(parentId=post_id))
    for i, answer in enumerate(answers):
        answers[i].body = mark_safe(cleaner.clean(answers[i].body))

    return render(req, 'posts/view.html', {
        'question': question, 'answers': answers
    })
