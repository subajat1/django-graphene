import graphene
from graphene_django.types import DjangoObjectType
from .models import Message

class MessageType(DjangoObjectType):
    class Meta:
        model = Message

class Query(graphene.ObjectType):
    all_messages_man = graphene.List(MessageType)

    def resolve_all_messages_man(self, info):
        return Message.objects.all()
