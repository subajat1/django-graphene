import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField

from .models import Message

class MessageType(DjangoObjectType):
    class Meta:
        model = Message
        filter_fields = {'message': ['icontains']}
        interfaces = (graphene.Node, )

class CreateMessage(graphene.Mutation):
    class Input:
        message = graphene.String()

    form_errors = graphene.String()
    message = graphene.Field(lambda: MessageType)

    @staticmethod
    def mutate(self, info):
        if not info.context.user.is_authenticated():
            return CreateMessage(form_errors=json.dumps('Please login!'))
        content = 'asdf message'#info.args.get('message')
        message = Message.objects.create(
            user=info.context.user, 
            message=str(content))
        return CreateMessage(message=message, form_errors=None)

class Mutation(graphene.AbstractType):
    create_message = CreateMessage.Field()

class Query(graphene.AbstractType):
    all_messages = DjangoFilterConnectionField(MessageType)

    def resolve_all_messages(self, info):
        return Message.objects.all()
