import books.schema
import graphene





class Query(books.schema.Query, graphene.ObjectType):
    pass


class Mutation(books.schema.Mutation, graphene.ObjectType):
    pass



schema = graphene.Schema(query=Query, mutation=Mutation)