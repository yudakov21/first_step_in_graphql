from typing import List
import strawberry
from src.app.students.models import college, student
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


@strawberry.type
class CollegeType:
    id: int
    name: str
    location: str

@strawberry.type
class StudentType:
    id: int
    name: str
    age: int
    college_id: int


@strawberry.type
class Query:
    @strawberry.field
    async def get_college(self, info)-> List[CollegeType]:
        session: AsyncSession = info.context["session"]
        query = select(college)
        result = await session.execute(query)
        return [CollegeType(**row._mapping) for row in result]
    
    @strawberry.field
    async def get_student(self, info)-> List[StudentType]:
        session: AsyncSession = info.context["session"]
        query = select(student)
        result = await session.execute(query)
        return [StudentType(**row._mapping) for row in result]
    

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_college(self, name: str, location: str, info) -> CollegeType:
        session: AsyncSession = info.context["session"]
        stmt = insert(college).values(name = name, location=location)\
        .returning(college.c.id, college.c.name, college.c.location)
        result = await session.execute(stmt)
        row = result.fetchone()
        await session.commit()

        return CollegeType(**row._mapping)
    
    @strawberry.mutation
    async def add_student(self, name: str, age: int, college_id: int, info) -> StudentType:
        session: AsyncSession = info.context["session"]
        stmt = insert(student).values(name = name, age=age, college_id=college_id)\
        .returning(student.c.id, student.c.name, student.c.age, student.c.college_id)
        result = await session.execute(stmt)
        row = result.fetchone()
        await session.commit()

        return StudentType(**row._mapping)

