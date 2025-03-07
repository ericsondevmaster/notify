
# NOTIFY

Bem-vindo ao Notify! Um projeto desenvolvido em Django, que integra Webhooks ao SGE (um projeto que está hospedado no meu GitHub em https://github.com/ericsondevmaster/sge_integration_master). Resumindo, a cada venda realizada no SGE, por exemplo, dispara um webhook que é salvo no banco de dados para fins de auditoria. A notificação de cada venda também é enviada para o Whatsapp e por email. Este README fornece informações essenciais sobre como configurar e executar o projeto em seu ambiente local.

## Requisitos:

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Python (versão recomendada: 3.7 ou superior)
- Django (instalado automaticamente ao seguir as instruções abaixo)
- Outras dependências listadas no arquivo `requirements.txt`

## Criação do Ambiente Virtual:

Certifique-se de que você está no diretório do projeto e crie o ambiente virtual com o comando:
```bash
python3 -m venv venv
```

## Instalação das Dependências:

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```bash
pip install -r requirements.txt
```

## Configuração das Variáveis de Ambiente:

Crie um arquivo `.env` dentro da pasta `app/` com as seguintes configurações:
```bash
CALLMEBOT_API_URL='https://api.callmebot.com/whatsapp.php'
CALLMEBOT_PHONE_NUMBER='numero_telefone'
CALLMEBOT_API_KEY='api_key'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT='587'
EMAIL_HOST_USER='email_origem'
EMAIL_HOST_PASSWORD='senha_app'
EMAIL_ADMIN_RECEIVER='email_destino'
```

## Rodando o Projeto:

Após instalar as dependências, aplique as migrations no banco de dados com o comando:
```bash
python manage.py migrate
```

Criar um super usuário com o comando:
```bash
python manage.py createsuperuser
```

Agora, o projeto já pode ser inicializado com o comando:
```bash
python manage.py runserver 8001
```

OBS: Esse comando subirá um servidor local de desenvolvimento. Foi colocado o parâmetro 8001 no final do comando para não dar conflito com o SGE, que irá rodar localmente com o comando `python manage.py runserver 8000`.

Após isso, o admin do projeto Notify poderá ser acessado em:
[http://localhost:8001/admin](http://localhost:8001/admin)

Você será direcionado para a tela de login do Admin do Django. Para acessar, bastar informar as credenciais criadas através do comando `python manage.py createsuperuser`
