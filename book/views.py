from django.http import JsonResponse,HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
# from rest_framework import viewsets
# from rest_framework.exceptions import NotFound
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'  #
    context_object_name = 'books'
    paginate_by = 5  

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book-create.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book-update.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_delete.html', {'book': book})


def multiplication_table(request):
    try:
        number = int(request.GET.get('number', 1))  # Default to 1 if 'number' parameter is not provided
    except ValueError:
        return HttpResponseBadRequest('Invalid input: number must be an integer number.')
    
    if number <= 0:
        return HttpResponseBadRequest('Invalid input: number must be a positive integer.')
     
    table = {i: i * number for i in range(1, 11)}
    return render(request, 'books/multiplication_table.html', {'number': number, 'table': table})
    

