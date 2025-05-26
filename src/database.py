from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.settings import DATABASE_URL 

# Here we are creating a AQLAlchemy engine that will connect to the db and manages the connection pool and dialects, will ad a debug statemnt to print all statemnts to the console
engine = create_engine()(DATABASE_URL, echo=True)

# next we create a session class that will be used to create sessions to the database
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# A Session is a "holding zone" for all objects loaded or associated with the database.
# 'autocommit=False': Transactions are not committed automatically. You need to call session.commit().
# 'autoflush=False': Objects are not flushed to the database automatically before query operations.
# 'bind=engine': Binds the session to our database engine.

# Next we create a declarative base method to return a base class for ORM models to inherit from
Base = declarative_base()
def create_tables():
    """
    Create all tables in the database.
    This function uses the Base metadata to create all tables defined in the ORM models.
    """
    print(f"Attempting to create tables in the database at the following URL: {DATABASE_URL}...")
    Base.metadata.create_all(engine)
    print("Tables created successfully.")

# we create a helper function to get a new database session
def get_db():
    """
    Returns a new SQLAlchemy session instance.
    This function is called whenever a database operation is needed
    to get a fresh session.
    It's important to close the session when done (session.close()).
    """
    session = Session()
    try:
        yield session # Use 'yield' for a context manager pattern (but since we dont know much on that),
                      # For now, a direct return is fine for simple CLI usage
    finally:
        session.close()

# for robust applications we can add the following block