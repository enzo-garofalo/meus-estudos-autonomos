from flask import Flask, render_template, request, redirect

# Faz o app rodar
app = Flask(__name__)

class Jogo:
  def __init__(self, nome, categoria, console):
    self.nome = nome
    self.categoria = categoria
    self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Adventure', 'PlayStation')
jogo3 = Jogo('Valorant', 'FPS', 'Console')
lista = [jogo1, jogo2, jogo3]

# Define Rota
@app.route('/')
def index():
  # Rederiza página HTML
  return render_template('lista.html', titulo = 'Jogos', jogos=lista)

@app.route('/novo')
def novo():
  return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  jogo = Jogo(nome, categoria, console)
  lista.append(jogo)
  return redirect('/')

app.run(debug=True)