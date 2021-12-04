from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy() #SQLAlchemy를 사용해 데이터베이스 저장

class User(db.Model): #데이터 모델을 나타내는 객체 선언
    __tablename__ = 'user_table' #테이블 이름
    
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    score = db.Column(db.Integer, nullable=True) #왜 오류가...?
    rank = db.Column(db.Integer, nullable=True) #여기에 본인 등수 넣기 중복 가능
    #nicakname

    # def __init__(self, email, password):
    #     self.email = email
    #     self.set_password(password)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
 
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    save_path = db.Column(db.String(128), nullable=False)
    label = db.Column(db.String(50))


    def __init__(self, save_file_name, save_path):
        self.save_file_name = save_file_name
        self.save_path = save_path


    @property
    def serialize(self):
        return {
            'id': self.id,
            'save_file_name': self.save_file_name,
            'save_path': self.save_path,
            'created_date': self.created_date
        }
