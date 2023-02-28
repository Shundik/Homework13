from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey

metadata = MetaData()

employees = Table('students2', metadata,
                  Column('name', Integer(), primary_key=True),
                  Column('surname', String(200), nullable=False),
                  )

employee_details = Table('auditorium5', metadata,
                         Column('auditorium', ForeignKey('students2.name'), primary_key=True),
                         )
