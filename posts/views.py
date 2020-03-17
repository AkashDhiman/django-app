from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe
from bleach import ALLOWED_TAGS, ALLOWED_ATTRIBUTES
from bleach.sanitizer import Cleaner

from .models import Post

VALID_TAGS = ['img', 'p', 'strike', 'br',
              'span', 'blockquote', 'pre', 'hr'] + ALLOWED_TAGS

VALID_ATTR = ALLOWED_ATTRIBUTES
VALID_ATTR['img'] = ['src', 'alt', 'rel']

orders = {'creation-date': '-creationDate',
          'view-count': '-viewCount',
          'score': '-score'
          }

cleaner = Cleaner(tags=VALID_TAGS, attributes=VALID_ATTR)


def index(req):
    order = req.GET.get('order', 'creation-date')
    title = req.GET.get('title', '')
    body = req.GET.get('body', '')
    if order in orders:
        posts = list(Post.objects
                     .filter(postTypeId=1,
                             body__icontains=body,
                             title__icontains=title)
                     .order_by(orders[order]))
    else:
        posts = list(Post.objects
                     .filter(postTypeId=1,
                             body__icontains=body,
                             title__icontains=title)
                     .order_by(orders['creation-date']))

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
    if question.acceptedAnswerId != None:
        for i, answer in enumerate(answers):
            if question.acceptedAnswerId == answer.id:
                ans = answer
                ans_i = i
                break
        answers.pop(i)
        answers.insert(0, ans)

    for i, answer in enumerate(answers):
        answers[i].body = mark_safe(cleaner.clean(answers[i].body))

    return render(req, 'posts/view.html', {
        'question': question, 'answers': answers
    })


def search(req):
    title = req.GET.get('title', '')
    body = req.GET.get('body', '')
    order = req.GET.get('order', 'creation-date')
    if order in orders:
        posts = list(Post.objects
                     .filter(body__icontains=body,
                             title__icontains=title,
                             postTypeId=1)
                     .order_by(orders[order]))
    else:
        posts = list(Post.objects
                     .filter(body__icontains=body,
                             title__icontains=title,
                             postTypeId=1)
                     .order_by('creationDate'))

    for i, e in enumerate(posts):
        posts[i].body = mark_safe(cleaner.clean(posts[i].body))
        posts[i].title = mark_safe(cleaner.clean(posts[i].title))

    if body == '' and title == '':
        return render(req, 'posts/search.html')

    else:
        return render(req, 'posts/index.html', {
            'posts': posts
        })
