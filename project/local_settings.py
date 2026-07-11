# # type: ignore
# # flake8: noqa

# # Comando:
# # python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
# SECRET_KEY = 'KOYMPTQvHTn!`9CZm5e~wKM?2_.Vpi&~~n*bO%NJr]_Ta,b"s@x!3c&_]6@V.wl^'

# # DEBUG DEVE SER False em produção
# DEBUG = False

# # Seu domínio ou IP devem vir aqui
# ALLOWED_HOSTS = [
#     '34.176.17.91',
# ]  # Troque * para seu domínio ou IP

# # Config para postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'NOME_DA_BASE_DE_DADOS',
#         'USER': 'USUARIO_DA_BASE_DE_DADOS',
#         'PASSWORD': 'SENHA_DA_BASE_DE_DADOS',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
