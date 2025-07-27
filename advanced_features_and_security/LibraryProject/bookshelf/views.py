from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Document, Book
from django.http import HttpResponseForbidden
# ✅ Use ORM and clean form input
from django.db.models import Q
from .forms import BookForm
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm


@permission_required('bookshelf.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'bookshelf/document_list.html', {'documents': documents})

@permission_required('bookshelf.can_create', raise_exception=True)
def document_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Document.objects.create(title=title, content=content)
        return redirect('document_list')
    return render(request, 'bookshelf/document_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def document_edit(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.title = request.POST['title']
        document.content = request.POST['content']
        document.save()
        return redirect('document_list')
    return render(request, 'bookshelf/document_form.html', {'document': document})

@permission_required('bookshelf.can_delete', raise_exception=True)
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('document_list')

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(Q(title__icontains=query))
    return render(request, 'bookshelf/book_list.html', {'books': books, 'query': query})


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Make sure you have this URL pattern
    else:
        form = BookForm()

    return render(request, 'bookshelf/book_form.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookshelf/book_form.html', {'form': form})




def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data securely
            cleaned_data = form.cleaned_data
            # (save, email, log, etc.)
            return redirect('success_url')
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
