from app import create_app, db
from app.model import users, Task  # import your models

app = create_app()

with app.app_context():
    db.drop_all()   # drop old tables
    db.create_all() # create fresh tables
    print("✅ Database has been reset with the latest schema.")

