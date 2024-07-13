# Dependências
Será necessário a criação de um ambiente virtual venv, podendo utilizar
o comando `python -m venv venv` ou `python3 -m venv venv`.

Após a criação da venv será necessário ativá-la.

# Ativar Venv Windows
Acessar a pasta `\venv\Scripts`
Depois digitar o comando `.\activate`
Depois retornar a pasta raiz `cd ../..`

# Ativar Venv Linux
Dar o comando no terminal `source venv/bin/activate`

# Instalando dependências
Na pasta raiz do projeto dar o comando `pip install -r requirements.txt`
Irá baixar e instalar as dependências necessárias para rodar o projeto.

# Environments
Terá um arquivo chamado .env-example, contendo todas variáveis necessárias de ambiente
que deverão ser criadas em um novo arquivo .env, que por sua vez não é versionado.
Aplicando as informações conforme o seu banco.

# Extra-Features
Nesse pacote, conterá uma coleção, contendo todos end-points da aplicação, para
que quando necessário, realize teste via postman/insominia.

# Comando para rodar o projeto
Ao rodar o `python manage.py runserver`, por padrão, irá rodar o projeto na porta 8000.
Caso seja a primeira vez rodando o projeto, será necessário aplicar as migrations, com 
o comando `python manage.py migrate`.

# Banco de Dados
Criar um banco de dados, utilizando postgres. Será necessário atualizar as variáveis
de ambiente.