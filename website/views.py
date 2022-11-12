from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def mainPage():
    return render_template("base.html")

@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/calendar')
@login_required
def calendar():
    return render_template("calendar.html", user=current_user)

@views.route('/schedule')
@login_required
def schedule():
    return render_template("schedule.html", user=current_user)

@views.route('/customers')
@login_required
def customers():
    return render_template("customers.html", user=current_user)

@views.route('/statistics')
@login_required
def statistics():
    return render_template("statistics.html", user=current_user)