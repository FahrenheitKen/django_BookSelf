from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')

    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})


def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
