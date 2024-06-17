from flask import request, redirect, render_template, flash, url_for, session
from helpers import FormularioUsuario
from models import Usuarios
from jogoteca import app


@app.route('/login')
def login():
  proxima = request.args.get('proxima')
  form = FormularioUsuario()
  return render_template('login.html', proxima=proxima, form=form)
        
@app.route('/autenticar', methods=['POST'])
def autenticar():

  form = FormularioUsuario(request.form)

  usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
  if usuario:
    if form.senha.data == usuario.senha:
      session['usuario_logado'] = usuario.nickname
      flash(usuario.nickname + ' Logado com suceso!') 
      proxima_pagina = request.form['proxima']
      return redirect(proxima_pagina)
  
  else:
    flash('Usuário não encontrado!')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
  session['usuario_logado'] = None
  flash('Logout efetuado com sucesso!')
  return redirect(url_for('index'))
