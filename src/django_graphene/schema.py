import graphene
from manager.schema import Query as manager_query

class Query(
    manager_query, 
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
