from sqlalchemy import create_engine, engine
from sqlalchemy.orm import Session

from app.config import DATABASE_URL

def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())

    session.execute("""
                    create tables user(
                        id integer not null primary key, 
                        email varchar(256),
                        password varchar(256),
                        first_name varchar(256),
                        register_date varchar(256)
                    );
                    
                    """)
    session.close()

if __name__ == '__main__':
    main()