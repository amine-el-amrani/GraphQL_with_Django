import graphene
from graphql import GraphQLError
from .types import BooksType
from .models import Books, Category, Author, Publisher



class CreateBook(graphene.Mutation):
    '''
    example:
    mutation{
        createBook(
            title: "Python",
            excerpt: "Junior"
            price: 10.55
            categoryId: 1
            publisherId: 2
            authorIds: [1, 2]
        ) {
            book {
            id
            title
            excerpt
            price
            category {
                id
                name
            }
            publisher {
                id
                name
            }
            authors {
                id
                name
            }
            }
        }
    }
    '''

    class Arguments:
        title = graphene.String()
        excerpt = graphene.String()
        price = graphene.Float()
        category_id = graphene.Int()
        publisher_id = graphene.Int()
        author_ids = graphene.List(graphene.Int)

    book = graphene.Field(BooksType)

    def mutate(self, info, title, excerpt, price, category_id, publisher_id, author_ids):
        # Fetching related objects from their IDs
        category = Category.objects.get(pk=category_id)
        publisher = Publisher.objects.get(pk=publisher_id)
        authors = Author.objects.filter(pk__in=author_ids)

        # Creating the book instance
        book = Books(
            title=title,
            excerpt=excerpt,
            price=price,
            category=category,
            publisher=publisher
        )
        book.save()

        # Adding authors to the book
        book.authors.add(*authors)

        return CreateBook(book=book)
    
class EditBook(graphene.Mutation):
    '''
    example:
    mutation{
        editBook(
            id: 1,
            title: "Python",
            excerpt: "Expert"
            price: 10.55
            categoryId: 1
            publisherId: 2
            authorIds: 1
        ) {
            book {
            id
            title
            excerpt
            price
            category {
                id
                name
            }
            publisher {
                id
                name
            }
            authors {
                id
                name
            }
            }
        }
    }
    '''
    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        excerpt = graphene.String()
        price = graphene.Float()
        category_id = graphene.Int()
        publisher_id = graphene.Int()
        author_ids = graphene.List(graphene.Int)

    book = graphene.Field(BooksType)

    def mutate(self, info, id, title, excerpt, price, category_id, publisher_id, author_ids):
        try:
            book = Books.objects.get(pk=id)
        except Books.DoesNotExist:
            raise GraphQLError(f"Book with id {id} does not exist.")

        if title is not None:
            book.title = title
        if excerpt is not None:
            book.excerpt = excerpt
        if price is not None:
            book.price = price

        # Fetching related objects from their IDs and updating the book
        if category_id is not None:
            category = Category.objects.get(pk=category_id)
            book.category = category
        if publisher_id is not None:
            publisher = Publisher.objects.get(pk=publisher_id)
            book.publisher = publisher
        if author_ids is not None:
            authors = Author.objects.filter(pk__in=author_ids)
            book.authors.set(authors)
        book.save()

        # Clearing old authors and adding new authors to the book
        book.authors.clear()
        book.authors.add(*authors)

        return EditBook(book=book)
    
class DeleteBook(graphene.Mutation):
    '''
    example:
    mutation{
        deleteBook(id: 1) {
            book {
            id
            title
            excerpt
            price
            category {
                id
                name
            }
            publisher {
                id
                name
            }
            authors {
                id
                name
            }
            }
        }
    }
    '''
    class Arguments:
        id = graphene.Int()

    book = graphene.Field(BooksType)

    def mutate(self, info, id):
        # Fetching the book instance
        book = Books.objects.get(pk=id)
        book.delete()

        return None