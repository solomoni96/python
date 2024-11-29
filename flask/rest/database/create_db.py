from app import app_init, db

def db_init():
    app = app_init()
    with app.app_context():
        db.create_all()
        print("***** Database created successfully. *****")

if __name__ == '__main__':
    db_init()
