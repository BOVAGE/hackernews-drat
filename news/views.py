from django.shortcuts import render
from .models import Story, Comment, Job, Poll, PollOption
from django.core.paginator import Paginator
from itertools import chain
from django.db.models import Q
from .utils import get_an_item_from_all_models

# Create your views here.
def home(request):
    item_type = request.GET.get("type", "")
    allow_type = {
        "story": Story.objects.all(),
        "comment": Comment.objects.all(),
        "job": Job.objects.all(),
        "poll": Poll.objects.all(),
        "pollopt": PollOption.objects.all(),
    }
    if item_type not in allow_type.keys():
        all_stories = allow_type["story"]
        all_comments = allow_type["comment"]
        all_job = allow_type["job"]
        all_polls = allow_type["poll"]
        all_poll_options = allow_type["pollopt"]
        all_items = chain(
            all_stories, all_comments, all_job, all_polls, all_poll_options
        )
        all_items = list(all_items)
    else:
        all_items = allow_type[item_type]
    paginator = Paginator(all_items, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "news/index.html", {"page_obj": page_obj, "item_type": item_type}
    )


def search(request):
    query = request.GET.get("q")
    page_number = request.GET.get("page")
    page_obj = []
    if query:
        search_query = Q(text__icontains=query)
        story_queryset = Story.objects.filter(search_query)
        comment_queryset = Comment.objects.filter(search_query)
        poll_queryset = Poll.objects.filter(search_query)
        job_queryset = Job.objects.filter(search_query)
        result = chain(story_queryset, comment_queryset, poll_queryset, job_queryset)
        result = list(result)
        paginator = Paginator(result, 5)
        page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "query": query}
    return render(request, "news/search_result.html", context)


def detail(request, hnid):
    item = get_an_item_from_all_models(hnid)
    return render(request, "news/detail.html", {"item": item})
