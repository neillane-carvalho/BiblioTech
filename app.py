# app.py

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

livros = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        
        if not titulo or not autor:
            flash('Por favor, preencha todos os campos.', 'error')
            return redirect(url_for('cadastrar_livro'))
        
        # Adicionar livro à lista de livros com ID e status inicial de disponível
        livro_id = len(livros) + 1
        livros.append({'id': livro_id, 'titulo': titulo, 'autor': autor, 'disponivel': True})
        flash('Livro cadastrado com sucesso!', 'success')
        return redirect(url_for('consulta_acervo'))
    
    return render_template('cadastrar_livro.html')

@app.route('/consulta_acervo')
def consulta_acervo():
    return render_template('consulta_acervo.html', livros=livros)

@app.route('/emprestimo/<int:livro_id>')
def emprestimo(livro_id):
    if livro_id <= len(livros):
        livro = livros[livro_id - 1]
        if livro['disponivel']:
            # Realizar empréstimo se o livro estiver disponível
            livro['disponivel'] = False
            flash(f'O livro "{livro["titulo"]}" foi emprestado com sucesso!', 'success')
        else:
            flash('O livro já está emprestado.', 'error')
    else:
        flash('Livro não encontrado.', 'error')
    
    return redirect(url_for('consulta_acervo'))

@app.route('/devolucao/<int:livro_id>')
def devolucao(livro_id):
    if livro_id <= len(livros):
        livro = livros[livro_id - 1]
        if not livro['disponivel']:
            # Realizar devolução se o livro estiver emprestado
            livro['disponivel'] = True
            flash(f'O livro "{livro["titulo"]}" foi devolvido com sucesso!', 'success')
        else:
            flash('O livro já está disponível.', 'error')
    else:
        flash('Livro não encontrado.', 'error')
    
    return redirect(url_for('consulta_acervo'))

@app.route('/remover/<int:livro_id>')
def remover_livro(livro_id):
    global livros
    if livro_id <= len(livros):
        del livros[livro_id - 1]
        flash('Livro removido com sucesso!', 'success')
    else:
        flash('Livro não encontrado.', 'error')

    return redirect(url_for('consulta_acervo'))

@app.route('/relatorios')
def relatorios():
    # Contagem de livros disponíveis e emprestados
    livros_disponiveis = sum(1 for livro in livros if livro['disponivel'])
    livros_emprestados = sum(1 for livro in livros if not livro['disponivel'])

    return render_template('relatorios.html', livros_disponiveis=livros_disponiveis, livros_emprestados=livros_emprestados)

if __name__ == '__main__':
    app.run(debug=True)
