from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "postgresql://postgres.polrwprthazfklcpvhbr:Test1234@aws-0-ap-south-1.pooler.supabase.com:5432/postgres"

engine =create_engine(url=database_url, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()