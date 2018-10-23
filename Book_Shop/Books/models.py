from django.db import models
import datetime
from django.urls import reverse

class myBooks(models.Model):
    Book_Art = models.FileField(blank=True, null=True)  # this is the logo of the book
    Type = models.CharField(max_length=250, default='Horror')  # this is the type of the book; horror, adventure...
    Title = models.CharField(max_length=250)  # title of the book
    Author = models.CharField(max_length=250)  # The Writer of the book
    Description = models.CharField(max_length=10000, null=True)  # A brief description of the book
    Publisher = models.CharField(max_length=250)  # The publishing company
    Year_Of_Publication = models.IntegerField(default=2018)  # current year
    No_Of_Copies = models.IntegerField(default=1)  # No of Copies in Stock
    Date_Added = models.DateTimeField(default=datetime.datetime.now())  # this is the date the book was added

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Title + ' - ' + self.Author