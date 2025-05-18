os dados foram enviados
aprenda php para saber oq fazer com eles
<?php
// Verifica se o formulário foi enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtém os dados do formulário
    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $senha = $_POST['senha'];

    // Aqui você pode adicionar o código para processar os dados, como armazená-los em um banco de dados

    // Exibe uma mensagem de sucesso
    echo "Cadastro realizado com sucesso!";
} else {
    // Se o formulário não foi enviado, redireciona para a página do formulário
    header("Location: formulario.php");
    exit();
}
// Exibe os dados recebidos
echo "Nome: " . htmlspecialchars($nome) . "<br>";
echo "Email: " . htmlspecialchars($email) . "<br>";
echo "Senha: " . htmlspecialchars($senha) . "<br>";
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .container {
            margin-top: 50px;
        }
        .card {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .form-group {
            margin-bottom: 15px;
        }
        .btn {
            background-color: #007bff;
            color: white;
        }
        .btn:hover {
            background-color: #0056b3;
        }
        .alert {
            margin-top: 20px;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
        }
        .footer p {
            color: #6c757d;
        }
        .footer a {
            color: #007bff;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h2 class="text-center">Cadastro Realizado</h2>
            <p class="text-center">Os dados foram enviados com sucesso!</p>
            <div class="alert alert-success" role="alert">
                Nome: <?php echo htmlspecialchars($nome); ?><br>
                Email: <?php echo htmlspecialchars($email); ?><br>
                Senha: <?php echo htmlspecialchars($senha); ?>
            </div>
        </div>
    </div>
    <div class="footer">
        <p>&copy; 2023 Seu Nome. Todos os direitos reservados.</p>
        <p><a href="formulario.php">Voltar para o formulário</a></p>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
<?php
// Exibe os dados recebidos
