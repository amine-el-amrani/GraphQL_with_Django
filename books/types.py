from graphene_django.types import DjangoObjectType
from .models import Books, Category, Author, Publisher



class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ('id', 'title', 'excerpt', 'price', 'category', 'publisher', 'authors')

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('id', 'name')

class PublisherType(DjangoObjectType):
    class Meta:
        model = Publisher
        fields = ('id', 'name')