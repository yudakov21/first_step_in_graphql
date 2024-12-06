import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from src.app.students.schemas import Query, Mutation
from src.app.database import get_async_session  

app = FastAPI()

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, context_getter=get_async_session)

app.include_router(graphql_app, prefix='/graphql')




