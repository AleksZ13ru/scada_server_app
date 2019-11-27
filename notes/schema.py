import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Machine, Note


class MachineType(DjangoObjectType):
    class Meta:
        model = Machine


class NoteType(DjangoObjectType):
    class Meta:
        model = Note


class Query(ObjectType):
    machine = graphene.Field(MachineType, id=graphene.Int())
    note = graphene.Field(NoteType, id=graphene.Int())
    machines = graphene.List(MachineType)
    notes = graphene.List(NoteType)

    def resolve_machine(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Machine.objects.get(pk=id)
        return None

    def resolve_note(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Note.objects.get(pk=id)
        return None

    def resolve_machines(self, info, **kwargs):
        return Machine.objects.all()

    def resolve_notes(self, info, **kwargs):
        return Note.objects.all()


class MachineInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class NoteInput(graphene.InputObjectType):
    id = graphene.ID
    machine = graphene.List(MachineInput)
    datetime_start = graphene.DateTime()
    text = graphene.String()


# mutation{
#   createNote(input:{
#     machine:{id:1}
#     datetimeStart: "2017-10-06T14:54:54+00:00"
#     text:"test"
#   }){
#     ok
#   }
# }
class CreateNote(graphene.Mutation):
    class Arguments:
        input = NoteInput(required=True)

    ok = graphene.Boolean()
    note = graphene.Field(NoteType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        machine_instance = Machine.objects.get(pk=input.machine[0].id)
        note_instance = Note(machine=machine_instance, datetime_start=input.datetime_start, text=input.text, )
        note_instance.save()
        return CreateNote(ok=ok, note=note_instance)


class Mutation(graphene.ObjectType):
    create_note = CreateNote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
# schema = graphene.Schema(query=Query)
