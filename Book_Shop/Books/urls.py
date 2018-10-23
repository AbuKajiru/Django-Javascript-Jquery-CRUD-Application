from django.urls import path

# import views from the cirrent directory Books App
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('OurBooks', views.AllBooksView.as_view(), name='all_books_view'),
    path('book/<int:pk>', views.DetailsView.as_view(), name='detail'),
    path('book/add', views.AddBook.as_view(), name='add_book'),
    path('book/update/<int:pk>', views.UpdateBook.as_view(), name='update_book'),
    path('book/<int:pk>/delete', views.DeleteBook.as_view(), name='delete_book')
]
