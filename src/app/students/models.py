from sqlalchemy import Column, Integer, String, Table, ForeignKey, MetaData

metadata = MetaData()

college = Table(
    'college',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String, index=True),
    Column('location', String),
)

student = Table(
    'student',
    metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String, index=True),
    Column('age', Integer),
    Column('college_id', Integer, ForeignKey(college.c.id)),
)

# class College(Base):
#     __tablename__ = "colleges"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     location = Column(String)


# class Student(Base):
#     __tablename__ = "students"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     age = Column(Integer)
#     college_id = Column(Integer, ForeignKey("colleges.id"))

