# Aplicativo Seu Direito

Aplicativo criado para teste de habilidades com a linguagem Python e framework Django.

## Getting Started
Instruções para copia identica e montagem do ambiente do desenvolvimento, com todas as funcionalidades atendidas.

### Prerequisites
```
Virtualenv=15.1.0
Python=3.6
Django=1.11
```

### Installing

Instalar virtualenv

```
pip3 install virtualenv
```

Criar um ambiente virtualenv

```
No diretorio desejado:

virtualenv --python='/usr/local/bin/python3' venv
```

Após criar o ambiente vitual e ativa-lo, executar o clone do projeto:


```
git clone https://github.com/prdioliveira/seudireito.git
```

Acessar o diretorio seudireito e instalar as dependências

```
pip 3 install -r requirements.txt

Esse procedimento irá instalar:
Django=1.11
psycopg2=
```

Carregar as fixtures do projeto

```
python manage.py loaddata initial_data.json
```

Para as configurações do banco de dados, acessar o arquivo de settings


### Executando os testes

Os aquivos de settings estão separados. Sendo um para executar a aplicação local e outro apenas para testes, que são executados sqlite3.

```
python manage.py test --settings=seuDireito.settings.teste
```