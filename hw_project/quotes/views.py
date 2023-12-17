from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required

from .models import Quote, Author
from .forms import AuthorForm, QuoteForm


def main(request, page=1):
    quotes = Quote.objects.order_by('id')
    per_page = 10
    paginator = Paginator(quotes, per_page)
    try:
        quotes_on_page = paginator.page(page)
    except EmptyPage:
        quotes_on_page = paginator.page(paginator.num_pages)
    # quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'quotes/author_detail.html', context={'author': author})


@login_required
def create_author(request):
    form = AuthorForm(instance=Author())
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            form.save()
            return redirect(to='/')
    return render(request, 'quotes/add_author.html', context={'form': form})


@login_required
def create_quote(request):
    form = QuoteForm(instance=Quote())
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=Quote())
        if form.is_valid():
            quote = form.cleaned_data['quote']
            print(quote)
            form.save()
            return redirect(to='/')
    return render(request, 'quotes/add_quote.html', context={'form': form})
