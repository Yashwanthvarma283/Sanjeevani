# import os
# from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# load_dotenv()

# url = os.getenv("DATABASE_URL")
url ="postgresql://postgres.sidfgjcwhquuicxqtdkx:Project%40Sanjeevani@aws-1-ap-south-1.pooler.supabase.com:5432/postgres"

engine = create_engine(url)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()