function emprestarLivro() {
    var livroId = document.getElementById('livro-id').value;

    // Verificar se o campo do ID do livro está vazio
    if (!livroId) {
        alert("Por favor, insira o ID do livro.");
        return;
    }

    // Verificar se o ID do livro é um número válido
    if (isNaN(livroId)) {
        alert("O ID do livro deve ser um número válido.");
        return;
    }

    // Verificar se o livro com o ID fornecido existe na lista de livros
    var livro = livros.find(livro => livro.id === parseInt(livroId));
    if (!livro) {
        alert("Livro não encontrado com o ID fornecido.");
        return;
    }

    // Verificar se o livro já está emprestado
    if (!livro.disponivel) {
        alert("O livro já está emprestado.");
        return;
    }

    // Realizar empréstimo do livro
    livro.disponivel = false;
    console.log("Livro emprestado com ID: " + livroId);
}

function devolverLivro() {
    var livroId = document.getElementById('livro-id').value;

    // Verificar se o campo do ID do livro está vazio
    if (!livroId) {
        alert("Por favor, insira o ID do livro.");
        return;
    }

    // Verificar se o ID do livro é um número válido
    if (isNaN(livroId)) {
        alert("O ID do livro deve ser um número válido.");
        return;
    }

    // Verificar se o livro com o ID fornecido existe na lista de livros
    var livro = livros.find(livro => livro.id === parseInt(livroId));
    if (!livro) {
        alert("Livro não encontrado com o ID fornecido.");
        return;
    }

    // Verificar se o livro já está disponível
    if (livro.disponivel) {
        alert("O livro já está disponível.");
        return;
    }

    // Realizar devolução do livro
    livro.disponivel = true;
    console.log("Livro devolvido com ID: " + livroId);
}

