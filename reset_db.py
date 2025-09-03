from app import create_app, db
from app.model import users, Task  # import your models

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    print("✅ Database has been reset with the latest schema.")
