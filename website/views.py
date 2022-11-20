from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, Game, Country, Pickem
from . import db
import json
from sqlalchemy import cast, Date

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required

#### IMPORTANTE ->
def home():
    games_raw = Game.query.all()
    
    dates = [(game.date.month, game.date.day)  for game in games_raw]
    d = list(set(dates))
    d.sort()

    if len(d) > 1:
        g1 = dates.count(d[0])
        g2 = dates.count(d[1])
    else:
        g1, g2 = 1, 0

    for game in games_raw[:g1+g2]:
        if game.home_id is not None:
            game.home_name = Country.query.filter_by(id=game.home_id).first().name
            game.away_name = Country.query.filter_by(id=game.away_id).first().name
            game.home_fid = Country.query.filter_by(id=game.home_id).first().fid
            game.away_fid = Country.query.filter_by(id=game.away_id).first().fid

    return render_template("home.html", user=current_user, games1 = games_raw[:g1], games2 = games_raw[g1:(g1+g2)], 
        g1_date = f"{d[0][1]}/{d[0][0]}", g2_date = f"{d[1][1]}/{d[1][0]}")

@views.route('/leaderboard', methods=['GET', 'POST'])
@login_required
def leaderboard():
    return render_template("leaderboard.html", user=current_user)

@views.route('/bets', methods=['GET', 'POST'])
@login_required
def bets():
    return render_template("bets.html", user=current_user)

@views.route('/pickem', methods=['GET', 'POST'])
@login_required
def pickem():
    
    user_pickem = Pickem.query.filter_by(user_id=current_user.id).first()
    if user_pickem is None:
        new_pickem = create_pickem(current_user.id)
        db.session.add(new_pickem)
        db.session.commit()
        user_pickem = new_pickem

    countries = model_to_data_pickem(user_pickem)
    return render_template("pickem.html", user=current_user, 
    gA = countries[:4],
    gB = countries[4:8],
    gC = countries[8:12],
    gD = countries[12:16],
    gE = countries[16:20],
    gF = countries[20:24],
    gG = countries[24:28],
    gH = countries[28:32])

def create_pickem(user_id):
    new_pickem = Pickem(pontos = 0,
    user_id = user_id,
    g_a_1 = 1,  g_a_2 = 2,  g_a_3 = 3,  g_a_4 = 4,
    g_b_1 = 5,  g_b_2 = 6,  g_b_3 = 7,  g_b_4 = 8,
    g_c_1 = 9,  g_c_2 = 10,  g_c_3 = 11, g_c_4 = 12,
    g_d_1 = 13, g_d_2 = 14, g_d_3 = 15, g_d_4 = 16,
    g_e_1 = 17, g_e_2 = 18, g_e_3 = 19, g_e_4 = 20,
    g_f_1 = 21, g_f_2 = 22, g_f_3 = 23, g_f_4 = 24,
    g_g_1 = 25, g_g_2 = 26, g_g_3 = 27, g_g_4 = 28,
    g_h_1 = 29, g_h_2 = 30, g_h_3 = 31, g_h_4 = 32)
    return new_pickem

def model_to_data_pickem(pickem):
    g_a_1_name = Country.query.filter_by(id=pickem.g_a_1).first().name
    g_a_2_name = Country.query.filter_by(id=pickem.g_a_2).first().name
    g_a_3_name = Country.query.filter_by(id=pickem.g_a_3).first().name
    g_a_4_name = Country.query.filter_by(id=pickem.g_a_4).first().name

    g_b_1_name = Country.query.filter_by(id=pickem.g_b_1).first().name
    g_b_2_name = Country.query.filter_by(id=pickem.g_b_2).first().name
    g_b_3_name = Country.query.filter_by(id=pickem.g_b_3).first().name
    g_b_4_name = Country.query.filter_by(id=pickem.g_b_4).first().name

    g_c_1_name = Country.query.filter_by(id=pickem.g_c_1).first().name
    g_c_2_name = Country.query.filter_by(id=pickem.g_c_2).first().name
    g_c_3_name = Country.query.filter_by(id=pickem.g_c_3).first().name
    g_c_4_name = Country.query.filter_by(id=pickem.g_c_4).first().name

    g_d_1_name = Country.query.filter_by(id=pickem.g_d_1).first().name
    g_d_2_name = Country.query.filter_by(id=pickem.g_d_2).first().name
    g_d_3_name = Country.query.filter_by(id=pickem.g_d_3).first().name
    g_d_4_name = Country.query.filter_by(id=pickem.g_d_4).first().name

    g_e_1_name = Country.query.filter_by(id=pickem.g_e_1).first().name
    g_e_2_name = Country.query.filter_by(id=pickem.g_e_2).first().name
    g_e_3_name = Country.query.filter_by(id=pickem.g_e_3).first().name
    g_e_4_name = Country.query.filter_by(id=pickem.g_e_4).first().name
    
    g_f_1_name = Country.query.filter_by(id=pickem.g_f_1).first().name
    g_f_2_name = Country.query.filter_by(id=pickem.g_f_2).first().name
    g_f_3_name = Country.query.filter_by(id=pickem.g_f_3).first().name
    g_f_4_name = Country.query.filter_by(id=pickem.g_f_4).first().name

    g_g_1_name = Country.query.filter_by(id=pickem.g_g_1).first().name
    g_g_2_name = Country.query.filter_by(id=pickem.g_g_2).first().name
    g_g_3_name = Country.query.filter_by(id=pickem.g_g_3).first().name
    g_g_4_name = Country.query.filter_by(id=pickem.g_g_4).first().name

    g_h_1_name = Country.query.filter_by(id=pickem.g_h_1).first().name
    g_h_2_name = Country.query.filter_by(id=pickem.g_h_2).first().name
    g_h_3_name = Country.query.filter_by(id=pickem.g_h_3).first().name
    g_h_4_name = Country.query.filter_by(id=pickem.g_h_4).first().name

    r16_1_name = 'TBD'
    r16_2_name = 'TBD'
    r16_3_name = 'TBD'
    r16_4_name = 'TBD'
    r16_5_name = 'TBD'
    r16_6_name = 'TBD'
    r16_7_name = 'TBD'
    r16_8_name = 'TBD'
    qf1_name = 'TBD'
    qf2_name = 'TBD'
    qf3_name = 'TBD'
    qf4_name = 'TBD'
    sf1_name = 'TBD'
    sf2_name = 'TBD'
    tp_po_name = 'TBD'
    final_name = 'TBD'

    r16_1_fid = 'TBD'
    r16_2_fid = 'TBD'
    r16_3_fid = 'TBD'
    r16_4_fid = 'TBD'
    r16_5_fid = 'TBD'
    r16_6_fid = 'TBD'
    r16_7_fid = 'TBD'
    r16_8_fid = 'TBD'
    qf1_fid = 'TBD'
    qf2_fid = 'TBD'
    qf3_fid = 'TBD'
    qf4_fid = 'TBD'
    sf1_fid = 'TBD'
    sf2_fid = 'TBD'
    tp_po_fid = 'TBD'
    final_fid = 'TBD'

    g_a_1_fid = Country.query.filter_by(id=pickem.g_a_1).first().fid
    g_a_2_fid = Country.query.filter_by(id=pickem.g_a_2).first().fid
    g_a_3_fid = Country.query.filter_by(id=pickem.g_a_3).first().fid
    g_a_4_fid = Country.query.filter_by(id=pickem.g_a_4).first().fid

    g_b_1_fid = Country.query.filter_by(id=pickem.g_b_1).first().fid
    g_b_2_fid = Country.query.filter_by(id=pickem.g_b_2).first().fid
    g_b_3_fid = Country.query.filter_by(id=pickem.g_b_3).first().fid
    g_b_4_fid = Country.query.filter_by(id=pickem.g_b_4).first().fid

    g_c_1_fid = Country.query.filter_by(id=pickem.g_c_1).first().fid
    g_c_2_fid = Country.query.filter_by(id=pickem.g_c_2).first().fid
    g_c_3_fid = Country.query.filter_by(id=pickem.g_c_3).first().fid
    g_c_4_fid = Country.query.filter_by(id=pickem.g_c_4).first().fid

    g_d_1_fid = Country.query.filter_by(id=pickem.g_d_1).first().fid
    g_d_2_fid = Country.query.filter_by(id=pickem.g_d_2).first().fid
    g_d_3_fid = Country.query.filter_by(id=pickem.g_d_3).first().fid
    g_d_4_fid = Country.query.filter_by(id=pickem.g_d_4).first().fid

    g_e_1_fid = Country.query.filter_by(id=pickem.g_e_1).first().fid
    g_e_2_fid = Country.query.filter_by(id=pickem.g_e_2).first().fid
    g_e_3_fid = Country.query.filter_by(id=pickem.g_e_3).first().fid
    g_e_4_fid = Country.query.filter_by(id=pickem.g_e_4).first().fid
    
    g_f_1_fid = Country.query.filter_by(id=pickem.g_f_1).first().fid
    g_f_2_fid = Country.query.filter_by(id=pickem.g_f_2).first().fid
    g_f_3_fid = Country.query.filter_by(id=pickem.g_f_3).first().fid
    g_f_4_fid = Country.query.filter_by(id=pickem.g_f_4).first().fid

    g_g_1_fid = Country.query.filter_by(id=pickem.g_g_1).first().fid
    g_g_2_fid = Country.query.filter_by(id=pickem.g_g_2).first().fid
    g_g_3_fid = Country.query.filter_by(id=pickem.g_g_3).first().fid
    g_g_4_fid = Country.query.filter_by(id=pickem.g_g_4).first().fid

    g_h_1_fid = Country.query.filter_by(id=pickem.g_h_1).first().fid
    g_h_2_fid = Country.query.filter_by(id=pickem.g_h_2).first().fid
    g_h_3_fid = Country.query.filter_by(id=pickem.g_h_3).first().fid
    g_h_4_fid = Country.query.filter_by(id=pickem.g_h_4).first().fid

    #r16_1_fid = Country.query.filter_by(id=pickem.r16_1).first().fid
    #r16_2_fid = Country.query.filter_by(id=pickem.r16_2).first().fid
    #r16_3_fid = Country.query.filter_by(id=pickem.r16_3).first().fid
    #r16_4_fid = Country.query.filter_by(id=pickem.r16_4).first().fid
    #r16_5_fid = Country.query.filter_by(id=pickem.r16_5).first().fid
    #r16_6_fid = Country.query.filter_by(id=pickem.r16_6).first().fid
    #r16_7_fid = Country.query.filter_by(id=pickem.r16_7).first().fid
    #r16_8_fid = Country.query.filter_by(id=pickem.r16_8).first().fid
    #qf1_fid = Country.query.filter_by(id=pickem.qf1).first().fid
    #qf2_fid = Country.query.filter_by(id=pickem.qf2).first().fid
    #qf3_fid = Country.query.filter_by(id=pickem.qf3).first().fid
    #qf4_fid = Country.query.filter_by(id=pickem.qf4).first().fid
    #sf1_fid = Country.query.filter_by(id=pickem.sf1).first().fid
    #sf2_fid = Country.query.filter_by(id=pickem.sf2).first().fid
    #tp_po_fid = Country.query.filter_by(id=pickem.tp_po).first().fid
    #final_fid = Country.query.filter_by(id=pickem.final).first().fid

    #r16_1_name = Country.query.filter_by(id=pickem.r16_1).first().name
    #r16_2_name = Country.query.filter_by(id=pickem.r16_2).first().name
    #r16_3_name = Country.query.filter_by(id=pickem.r16_3).first().name
    #r16_4_name = Country.query.filter_by(id=pickem.r16_4).first().name
    #r16_5_name = Country.query.filter_by(id=pickem.r16_5).first().name
    #r16_6_name = Country.query.filter_by(id=pickem.r16_6).first().name
    #r16_7_name = Country.query.filter_by(id=pickem.r16_7).first().name
    #r16_8_name = Country.query.filter_by(id=pickem.r16_8).first().name
    #qf1_name = Country.query.filter_by(id=pickem.qf1).first().name
    #qf2_name = Country.query.filter_by(id=pickem.qf2).first().name
    #qf3_name = Country.query.filter_by(id=pickem.qf3).first().name
    #qf4_name = Country.query.filter_by(id=pickem.qf4).first().name
    #sf1_name = Country.query.filter_by(id=pickem.sf1).first().name
    #sf2_name = Country.query.filter_by(id=pickem.sf2).first().name
    #tp_po_name = Country.query.filter_by(id=pickem.tp_po).first().name
    #final_name = Country.query.filter_by(id=pickem.final).first().name

    return [[pickem.g_a_1, g_a_1_name, g_a_1_fid], [pickem.g_a_2, g_a_2_name, g_a_2_fid], 
            [pickem.g_a_3, g_a_3_name, g_a_3_fid], [pickem.g_a_4, g_a_4_name, g_a_4_fid],
            [pickem.g_b_1, g_b_1_name, g_b_1_fid], [pickem.g_b_2, g_b_2_name, g_b_2_fid],
            [pickem.g_b_3, g_b_3_name, g_b_3_fid], [pickem.g_b_4, g_b_4_name, g_b_4_fid],
            [pickem.g_c_1, g_c_1_name, g_c_1_fid], [pickem.g_c_2, g_c_2_name, g_c_2_fid],
            [pickem.g_c_3, g_c_3_name, g_c_3_fid], [pickem.g_c_4, g_c_4_name, g_c_4_fid],
            [pickem.g_d_1, g_d_1_name, g_d_1_fid], [pickem.g_d_2, g_d_2_name, g_d_2_fid],
            [pickem.g_d_3, g_d_3_name, g_d_3_fid], [pickem.g_d_4, g_d_4_name, g_d_4_fid],
            [pickem.g_e_1, g_e_1_name, g_e_1_fid], [pickem.g_e_2, g_e_2_name, g_e_2_fid],
            [pickem.g_e_3, g_e_3_name, g_e_3_fid], [pickem.g_e_4, g_e_4_name, g_e_4_fid],
            [pickem.g_f_1, g_f_1_name, g_f_1_fid], [pickem.g_f_2, g_f_2_name, g_f_2_fid],
            [pickem.g_f_3, g_f_3_name, g_f_3_fid], [pickem.g_f_4, g_f_4_name, g_f_4_fid],
            [pickem.g_g_1, g_g_1_name, g_g_1_fid], [pickem.g_g_2, g_g_2_name, g_g_2_fid],
            [pickem.g_g_3, g_g_3_name, g_g_3_fid], [pickem.g_g_4, g_g_4_name, g_g_4_fid],
            [pickem.g_h_1, g_h_1_name, g_h_1_fid], [pickem.g_h_2, g_h_2_name, g_h_2_fid],
            [pickem.g_h_3, g_h_3_name, g_h_3_fid], [pickem.g_h_4, g_h_4_name, g_h_4_fid],
            [pickem.r16_1, r16_1_name, r16_1_fid], [pickem.r16_2, r16_2_name, r16_2_fid],
            [pickem.r16_3, r16_3_name, r16_3_fid], [pickem.r16_4, r16_4_name, r16_4_fid],
            [pickem.r16_5, r16_5_name, r16_5_fid], [pickem.r16_6, r16_6_name, r16_6_fid],
            [pickem.r16_7, r16_7_name, r16_7_fid], [pickem.r16_8, r16_8_name, r16_8_fid],
            [pickem.qf1, qf1_name, sf1_fid], [pickem.qf2, qf2_name, qf2_fid],
            [pickem.qf3, qf3_name, qf3_fid], [pickem.qf4, qf4_name, qf4_fid],
            [pickem.sf1, sf1_name, sf1_fid], [pickem.sf2, sf2_name, sf2_fid], 
            [pickem.tp_po, tp_po_name, tp_po_fid], [pickem.final, final_name, final_fid]]

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/save_pickem', methods=['POST'])
def save_pickem():
    user_pickem = Pickem.query.filter_by(user_id=current_user.id).first()
    dados = request.get_json()
    print('Broooo')
    user_pickem.g_a_1 = dados[0]
    user_pickem.g_a_2 = dados[1]
    user_pickem.g_a_3 = dados[2]
    user_pickem.g_a_4 = dados[3]
    user_pickem.g_b_1 = dados[4]
    user_pickem.g_b_2 = dados[5]
    user_pickem.g_b_3 = dados[6]
    user_pickem.g_b_4 = dados[7]
    user_pickem.g_c_1 = dados[8]
    user_pickem.g_c_2 = dados[9]
    user_pickem.g_c_3 = dados[10]
    user_pickem.g_c_4 = dados[11]
    user_pickem.g_d_1 = dados[12]
    user_pickem.g_d_2 = dados[13]
    user_pickem.g_d_3 = dados[14]
    user_pickem.g_d_4 = dados[15]
    user_pickem.g_e_1 = dados[16]
    user_pickem.g_e_2 = dados[17]
    user_pickem.g_e_3 = dados[18]
    user_pickem.g_e_4 = dados[19]
    user_pickem.g_f_1 = dados[20]
    user_pickem.g_f_2 = dados[21]
    user_pickem.g_f_3 = dados[22]
    user_pickem.g_f_4 = dados[23]
    user_pickem.g_g_1 = dados[24]
    user_pickem.g_g_2 = dados[25]
    user_pickem.g_g_3 = dados[26]
    user_pickem.g_g_4 = dados[27]
    user_pickem.g_h_1 = dados[28]
    user_pickem.g_h_2 = dados[29]
    user_pickem.g_h_3 = dados[30]
    user_pickem.g_h_4 = dados[31]
    db.session.commit()
    
    return redirect(url_for('views.pickem'))

    #r16_1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #r16_2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #r16_3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #r16_4 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #r16_5 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #r16_6 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #r16_7 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #r16_8 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #qf1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #qf2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #qf3 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #qf4 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #sf1 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #sf2 = db.Column(db.Integer, db.ForeignKey('country.id'))
    #tp_po = db.Column(db.Integer, db.ForeignKey('country.id'))
    #final = db.Column(db.Integer, db.ForeignKey('country.id'))
