from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template import loader
# Create your views here.
from django.urls import reverse

from book_app.forms import BookForm, AuthorForm
from book_app.models import Book, Author


def home_view(request):
    return render(request, template_name='home.html')


# Facem un view ce afiseaza tot ce avem in baza de dte(models.py):

def show_books_view(request):
    books = Book.objects.all()
    search_text = request.GET.get("search", "")
    if search_text:
        books = books.filter(title__contains=search_text)
    return render(request, template_name='books.html', context={'context_books': books, "search_text": search_text})


def create_book(request):
    if request.method == 'GET':
        form = BookForm()
        author_form = AuthorForm()
        # Folosim loader in loc de render
        content = loader.render_to_string('create_book.html', {'form': form, 'author_form': author_form}, request)
        return HttpResponse(content)
    elif request.method == 'POST':
        form = BookForm(data=request.POST)
        author_form = AuthorForm(data=request.POST)
        if form.is_valid() and author_form.is_valid():
            try:
                author = Author.objects.get(first_name=author_form.cleaned_data['first_name'],
                                            last_name=author_form.cleaned_data['last_name'])
            except Author.DoesNotExist:
                author = Author.objects.create(first_name=author_form.cleaned_data['first_name'],
                                               last_name=author_form.cleaned_data['last_name'])

            book = Book.objects.create(
                title=form.cleaned_data['title'],
                genre=form.cleaned_data['genre'],
                number_of_pages=form.cleaned_data['number_of_pages'],
                description=form.cleaned_data['description'],
                published=form.cleaned_data['published'],
                state=form.cleaned_data['state']
            )
            # book.authors.set(form.cleaned_data['authors'])
            book.authors.add(author)

            # form.save()
            return redirect(reverse('books_list'))
        else:
            return render(request, template_name='create_book.html', context={'form': form, "author_form": author_form})


def update_book_view(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = BookForm(instance=book)
        return render(request, template_name='update_book.html', context={'book': book, 'form': form})

    elif request.method == 'POST':
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            # V1:
            form.save()
            # v2:
            book.title = form.cleaned_data['title']
            book.genre = form.cleaned_data['genre']
            book.number_of_pages = form.cleaned_data['number_of_pages']
            book.description = form.cleaned_data['description']
            book.published = form.cleaned_data['published']
            book.state = form.cleaned_data['state']

            book.save()
            messages.success(request, 'Book updated successfully.')

        return render(request, template_name='update_book.html', context={'book': book, 'form': form})

def delete_book_view(request, book_id):
    if request.method == 'GET':
        return render(request, template_name='delete_book.html')
