''' CORE SQL ALCHEMY '''
# from sqlalchemy import create_engine, text
# engine = create_engine("sqlite+pysqlite:///mydb.db", echo=True, future=True)
# with engine.connect() as conn:
#     result = conn.execute(text("select 'hello world'"))
#     print(result.all())

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE value_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO value_table (x,y) VALUES (:x, :y)"),
#     [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
#     )
#     conn.commit()
#
# with engine.begin() as conn:
#     conn.execute(
#         text("INSERT INTO value_table (x, y) VALUES (:x, :y)"),
#         [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
#     )
# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM value_table"))
#     for row in result:
#         print(f"x: {row.x}  y: {row.y}")
#         x = row[0]
#         print(x)
#         y = row[1]
#         print(y)
#     result = conn.execute(text("select x, y from some_table"))
#
#     for dict_row in result.mappings():
#         x = dict_row['x']
#         y = dict_row['y']

# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT x,y FROM value_table WHERE y > :y"),
#         {"y": 2}
#     )
#     for row in result:
#         print(f"x: {row.x} y: {row.y}")

# stmt = text("SELECT x, y FROM value_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     for row in result:
#        print(f"x: {row.x}  y: {row.y}")

''' ORM METHOD'''

from sqlalchemy.orm import Session

from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///mydb.db", echo=True, future=True)
stmt = text("SELECT x, y FROM value_table WHERE y > :y ORDER BY x,y").bindparams(y=6)
with Session(engine) as session:
    result = session.execute(stmt)
    for row in result:
        print(f"x: {row.x}  y: {row.y}")
