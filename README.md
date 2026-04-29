# 📒 Agenda de Contatos - Django

Este projeto foi desenvolvido como meu primeiro contato com o framework Django, com o objetivo de aprender na prática como funciona o desenvolvimento de aplicações web com Python.

## 🚀 Funcionalidades

- Cadastro de usuários
- Sistema de login e autenticação
- Criação de contatos na agenda
- Listagem de contatos
- Atualização de informações dos contatos
- Remoção de contatos

## 🔐 Regras de Negócio

- Cada usuário pode criar seus próprios contatos
- Todo contato criado fica vinculado ao usuário logado
- Um usuário pode visualizar todos os contatos da agenda
- Porém, só pode editar ou excluir os contatos que ele mesmo criou

## 🛠️ Tecnologias Utilizadas

- Python
- Django
- SQLite (banco de dados padrão do Django)

## 📚 Aprendizados

Este projeto marcou meu primeiro contato com Django, onde pude aprender conceitos importantes como:

- Estrutura do framework Django (apps, models, views e templates)
- Sistema de autenticação de usuários
- Relacionamento entre usuário e dados (ForeignKey)
- CRUD (Create, Read, Update, Delete)
- Controle de permissões

## ▶️ Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/kahazdev/Projeto-Agenda.git


2. Acesse a pasta do projeto:
cd Projeto-Agenda

3. Crie um ambiente virtual:
python -m venv venv

4. Ative o ambiente virtual:
 Windows:
    venv\Scripts\activate
 Linux/Mac:
    source venv/bin/activate

5. Instale as dependências:
pip install -r requirements.txt

6. Execute as migrações:
python manage.py migrate

7. Inicie o servidor:
python manage.py runserver

8. Acesse no navegador:
http://127.0.0.1:8000/

📌 Observações

Este é um projeto de estudo, focado no aprendizado do Django. Ainda há várias melhorias que podem ser feitas, como:

Melhorar a interface
Adicionar paginação
Implementar busca de contatos
Deploy da aplicação
👨‍💻 Autor

Desenvolvido por [Thiago Rodrigues de Carvalho]