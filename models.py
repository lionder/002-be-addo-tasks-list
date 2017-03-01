import peewee as pw
from flask_login._compat import unicode
from playhouse.fields import PasswordField

db = pw.SqliteDatabase('database.db')


def initialize_database():
    User.create_table(fail_silently=True)

    try:
        User.create(
            username='root',
            password='123'
        )
    except pw.IntegrityError:
        pass


class BaseModel(pw.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = pw.CharField(max_length=70, unique=True)
    password = PasswordField()
    state = pw.BooleanField(default=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.state

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.username