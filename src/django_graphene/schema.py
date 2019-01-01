import graphene
from manager.schema import Query as manager_query
from manager.schema import Mutation as manager_mutation

class Mutation(
    manager_mutation, 
    graphene.ObjectType):
    pass

class Query(
    manager_query, 
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
