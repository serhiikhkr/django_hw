from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = list(db.quotes_collection.find())
    per_page = 10
    paginator = Paginator(quotes, per_page)
    try:
        quotes_on_page = paginator.page(page)
    except EmptyPage:
        quotes_on_page = paginator.page(paginator.num_pages)
    # quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})
