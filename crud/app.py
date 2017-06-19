#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Leandro Batista
# e-mail: leandrobatistapereira98@gmail.com
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Pessoa(db.Model):
    __tablename__ = "clientes"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    telephone = db.Column(db.String)
    cpf = db.Column(db.String)
    email = db.Column(db.String)

    def __init__(self, name, telefone, cpf, email):
        self.name = name
        self.telefone = telefone
        self.cpf = cpf
        self.email = email


db.create_all()


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/cadastro")
def cadastrar():
    return render_template("cadastrar.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        name = request.form.get("NOME")
        telefone = request.form.get("TELEFONE")
        cpf = request.form.get("CPF")
        email = request.form.get("E-MAIL")
        if name and telefone and cpf and email:
            p = Pessoa(name, telefone, cpf, email)
            db.session.add(p)
            db.session.commit()

    return redirect(url_for("index"))


@app.route("/listar")
def listar_clientes():
    clientes = Pessoa.query.all()
    return render_template("lista.html", clientes=clientes)

if __name__ == "__main__":
    app.run(debug=True)
