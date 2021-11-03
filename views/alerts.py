from flask import Blueprint, render_template, url_for

alert_blueprint = Blueprint("alerts", __name__)

@alert_blueprint.route("/")
def index():
	return render_template("alerts/index.html")

@alert_blueprint.route("/new")
def new():
	return render_template("alerts/new_alerts.html")

