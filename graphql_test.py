import graphene

class Query(graphene.ObjectType):
    is_staff = graphene.Boolean()

    def resolve_is_staff(self, info):
        return True

schema = graphene.Schema(query=Query)

result = schema.execute('{isStaff}')

items = dict(result.data.items())
print(items)

import graphene

# class Query(graphene.ObjectType):
#   hello = graphene.String(name=graphene.String(default_value="World"))

#   def resolve_hello(self, info, name):
#     return 'Hello ' + name

# schema = graphene.Schema(query=Query)
# result = schema.execute('{ hello }')
# print(result.data['hello']) # "Hello World"