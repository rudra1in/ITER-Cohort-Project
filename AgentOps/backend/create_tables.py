from app.database.database import engine, Base
from app.database.models import KnowledgeChunk


print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")