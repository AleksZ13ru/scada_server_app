import graphene
import graphql_jwt
import movies.schema
import users.schema
import notes.schema
import opc_ua.schema


class Query(
    notes.schema.Query,
    users.schema.Query,
    movies.schema.Query,
    opc_ua.schema.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    notes.schema.Mutation,
    users.schema.Mutation,
    movies.schema.Mutation,
    opc_ua.schema.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    # pass


schema = graphene.Schema(query=Query, mutation=Mutation)
