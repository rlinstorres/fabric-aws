# fabric-aws

- Script para rodar comandos em instâncias da AWS

Exemplo de fabric file para rodar comandos em instâncias da AWS.
Utiliza roles para filtrar as instâncias

http://www.fabfile.org/

##### Instalação:

```
pip install fabric boto
```

##### Exemplos de Uso:

Executa a task hostname para todas as maquinas da AWS. O role 'all' contem todas as maquinas

```
fab -R all hostname
```

Faz o mesmo acima, porem em paralelo, limitando em 4 operacoes concorrentes:

```
fab -R all -P -z 4 hostname
```

Executa o comando parametrizavel de hello world em paralelo para as maquinas que tem o nome 'teste-1':

```
fab -R teste-1 -P hello:what=World
```

Para maiores detalhes, consulte o help do fabric: 'fab --help'

##### No script existem parâmetros a serem informados:

```
# Server user, normally AWS Ubuntu instances have default user "ubuntu"
env.user = "ubuntu"

# List of AWS private key Files
env.key_filename = ["~/.ssh/key-name.pem"]

# Export Access_Key and Secret_key
access_key = os.environ.get("ACCESS_KEY")
secret_key = os.environ.get("SECRET_KEY")
```
