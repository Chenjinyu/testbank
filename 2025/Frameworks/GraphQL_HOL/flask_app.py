from flask import Flask
from flask_graphql import GraphQLView
import graphene


# Define the data types (like models)
class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    

# define queries
class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.ID(required=True))
    
    def resolve_user(self, info, id):
        # Normally you'd fetch from DB
        fake_users = {
            1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
            2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
        }
        return fake_users.get(int(id))
        
# Create schema
schema = graphene.Schema(query=Query)

# Setup Flask
app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enable GraphiQL interface
    )
)


if __name__ == '__main__':
    app.run(debug=True)