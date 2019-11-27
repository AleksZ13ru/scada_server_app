import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Server, Tag, Result


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class ResultType(DjangoObjectType):
    class Meta:
        model = Result


class Query(ObjectType):
    result = graphene.Field(ResultType, id=graphene.Int())
    result_in_date = graphene.Field(ResultType, id=graphene.Int(), date=graphene.Date())
    results = graphene.List(ResultType)

    tag = graphene.Field(TagType, id=graphene.Int())
    tags = graphene.List(TagType)

    @staticmethod
    def resolve_result(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Result.objects.get(pk=id)
        return None

    @staticmethod
    def resolve_result_in_date(self, info, **kwargs):
        id = kwargs.get('id')
        date = kwargs.get('date')
        if id is not None:
            return Result.objects.get(pk=id, date=date)
        return None

    @staticmethod
    def resolve_results(self, info, **kwargs):
        return Result.objects.all()

    @staticmethod
    def resolve_tag(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Tag.objects.get(pk=id)
        return None

    @staticmethod
    def resolve_tags(self, info, **kwargs):
        return Tag.objects.all()


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
