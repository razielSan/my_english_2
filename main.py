from english.routes import app
from english import db, English


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
