# config=utf-8

from flask_login import UserMixin
from common import db

class Student(db.Model,UserMixin):
    bf_StudentID = db.Column('bf_StudentID',db.Integer,primary_key=True)
    bf_Name = db.Column(db.String(100),unique=True)
    bf_sex = db.Column(db.String(20), unique=True)
    bf_nation = db.Column(db.String(50), unique=True)
    bf_BornDate = db.Column(db.Integer, unique=True)
    cla_Name = db.Column(db.String(100), unique=True)
    bf_NativePlace = db.Column(db.String(100), unique=True)
    bf_ResidenceType= db.Column(db.String(80), unique=True)
    bf_policy = db.Column(db.String(70), unique=True)
    cla_id = db.Column(db.String(20), unique=True)
    cla_term = db.Column(db.String(100), unique=True)
    bf_zhusu = db.Column(db.String(100), unique=True)
    bf_leaveSchool = db.Column(db.String(100), unique=True)
    bf_qinshihao = db.Column(db.String(60), unique=True)
    __tablename__='student_info'

    def __init__(self,bf_StudentID=None,bf_Name=None, bf_nation =None,bf_BornDate=None,cla_Name=None,bf_NativePlace=None,bf_ResidenceType=None,bf_policy=None,cla_id =None,cla_term=None,bf_zhusu=None, bf_leaveSchool =None,bf_qinshihao=None,bf_sex=None,):
        self.bf_StudentID =bf_StudentID
        self.bf_Name=bf_Name
        self. bf_sex=  bf_sex
        self.bf_nation =bf_nation
        self.bf_BornDate = bf_BornDate
        self.cla_Name = cla_Name
        self.bf_NativePlace= bf_NativePlace
        self.bf_ResidenceType= bf_ResidenceType
        self.bf_policy =bf_policy
        self.cla_id  = cla_id
        self.cla_term =cla_term
        self.bf_zhusu= bf_zhusu
        self. bf_leaveSchool  =  bf_leaveSchool
        self.bf_qinshihao= bf_qinshihao
        self.bf_sex = bf_sex

