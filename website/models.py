from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#Aqui é onde se craim as tabelas basicamente

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150)) #first_name
    notes = db.relationship('Note')
    bets = db.relationship('Bet')
    pickem = db.relationship('Pickem')

#Só um modelo -> apagar
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#On Work

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    state = db.Column(db.String(20))
    group = db.Column(db.String(20))
    home_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    away_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    home_score = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
    bets = db.relationship('Bet')

class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    type = db.Column(db.String(20))
    odd = db.Column(db.Float)
    result = db.Column(db.Integer)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(1))
    name = db.Column(db.String(20))
    fid = db.Column(db.String(10))
    
class Pickem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pontos = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    g_a_1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_a_2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_a_3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_a_4 = db.Column(db.Integer, db.ForeignKey('country.id'))

    g_b_1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_b_2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_b_3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_b_4 = db.Column(db.Integer, db.ForeignKey('country.id'))

    g_c_1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_c_2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_c_3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_c_4 = db.Column(db.Integer, db.ForeignKey('country.id'))

    g_d_1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_d_2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_d_3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_d_4 = db.Column(db.Integer, db.ForeignKey('country.id'))

    g_e_1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_e_2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_e_3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_e_4 = db.Column(db.Integer, db.ForeignKey('country.id'))
    
    g_f_1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_f_2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_f_3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_f_4 = db.Column(db.Integer, db.ForeignKey('country.id'))

    g_g_1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_g_2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_g_3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_g_4 = db.Column(db.Integer, db.ForeignKey('country.id'))

    g_h_1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_h_2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_h_3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    g_h_4 = db.Column(db.Integer, db.ForeignKey('country.id'))

    r16_1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    r16_2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    r16_3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    r16_4 = db.Column(db.Integer, db.ForeignKey('country.id'))
    r16_5 = db.Column(db.Integer, db.ForeignKey('country.id'))
    r16_6 = db.Column(db.Integer, db.ForeignKey('country.id'))
    r16_7 = db.Column(db.Integer, db.ForeignKey('country.id'))
    r16_8 = db.Column(db.Integer, db.ForeignKey('country.id'))
    qf1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    qf2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    qf3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    qf4 = db.Column(db.Integer, db.ForeignKey('country.id'))
    sf1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    sf2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    tp_po = db.Column(db.Integer, db.ForeignKey('country.id'))
    final = db.Column(db.Integer, db.ForeignKey('country.id'))
