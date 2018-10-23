from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . models import myBooks
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

app_name = 'Books'

def index(request):
    return render(request,'Books/home.html')

class AllBooksView(generic.ListView):
    template_name = 'Books/books_in_store.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return  myBooks.objects.all()

class DetailsView(generic.DetailView):
        model = myBooks
        template_name = 'Books/book_description.html'


class AddBook(CreateView):
    model = myBooks
    fields = ['Book_Art', 'Type', 'Title', 'Author', 'Description', 'Publisher', 'Year_Of_Publication',
              'No_Of_Copies']

class UpdateBook(UpdateView):
    model = myBooks
    fields = ['Book_Art', 'Type', 'Title', 'Author', 'Description', 'Publisher', 'Year_Of_Publication',
              'No_Of_Copies']

class DeleteBook(DeleteView):
    model = myBooks
    success_url = reverse_lazy('index')
























