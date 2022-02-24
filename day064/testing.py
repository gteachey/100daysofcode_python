from sqlalchemy import create_engine
import os
from sqlalchemy import text

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(THIS_FOLDER, 'movie-list.db')
db_path = f"sqlite:///{db_file}"
print(db_path)

# engine = create_engine(db_path, echo=True, future=True)
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
