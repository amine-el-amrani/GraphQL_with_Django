import graphene
from .models import Books, Category, Author, Publisher
from .types import BooksType, CategoryType, AuthorType, PublisherType
from .mutations import CreateBook, EditBook, DeleteBook






class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)
    all_categories = graphene.List(CategoryType)
    all_authors = graphene.List(AuthorType)
    all_publishers = graphene.List(PublisherType)
    book = graphene.Field(BooksType, id=graphene.Int())
    category = graphene.Field(CategoryType, id=graphene.Int())
    author = graphene.Field(AuthorType, id=graphene.Int())
    publisher = graphene.Field(PublisherType, id=graphene.Int())

    def resolve_all_books(self, info, **kwargs):
        return Books.objects.all()
    
    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all().order_by('name')
    
    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()
    
    def resolve_all_publishers(self, info, **kwargs):
        return Publisher.objects.all().order_by('name')
    
    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Books.objects.get(pk=id)
        return None

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Category.objects.get(pk=id)
        return None
    
    def resolve_author(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Author.objects.get(pk=id)
        return None
    
    def resolve_publisher(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Publisher.objects.get(pk=id)
        return None
    
    

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    edit_book = EditBook.Field()
    delete_book = DeleteBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


