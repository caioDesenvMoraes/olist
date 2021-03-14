# importando as bibliotecas
import os
import pandas as pd
import sqlalchemy

# achando o caminho do projeto e dos dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# mostrando o caminho do projeto e dos dados
# print(f"Meu diretório do projeto é: {BASE_DIR}")
# print(f"Meu diretório dos dados é: {DATA_DIR}")

# listando os arquivos dentro do diretório de dados
# files_names = os.listdir(DATA_DIR)

# mostrando a lista com os arquivos dentro do diretório de dados
# print(files_names)

# pegando apenas os arquivos csv

"""
# forma não pythonica (for)
files_names = os.listdir(DATA_DIR)
correct_files = []
for i in files_names:
    if i.endswith(".csv"):
        correct_files.append(i)
"""

# forma pythonica (comprehensions)
files_names = [i for i in os.listdir(DATA_DIR) if i.endswith(".csv")]

# mostrando os arquivos csv do diretório data. Os dois são iguais.
# print(correct_files)
# print(files_names)

"""
# dados para conectar com o banco da amazon
user = "twitch"  # login
pswd = "teodoroc"  # senha
host = "database-1.cjyp1fkhums7.us-east-2.rds.amazonaws.com"  # ip/host/dns
port = "3306"  # porta

# criando a conexão do banco da amazon
str_connection = "mysql+pymysql:///{user}:{pswd}@{host}:{port}"
str_connection = str_connection.format(user=user, pswd=pswd, host=host, port=port)
connection = sqlalchemy.create_engine(str_connection)

# percorrendo por cada arquivo .csv do diretório data
for i in files_names:
    # print(i)  # mostrando o nome de cada arquivo .csv
    df_tmp = pd.read_csv(os.path.join(DATA_DIR, i))  # lendo cada um dos arquivos .csv
    table_name = "tb_" + i.strip(".csv").replace("olist_", "").replace("_dataset", "")  # definindo o nome das tabelas
    df_tmp.to_sql(table_name, connection, schema="analytics", if_exists="replace", index=False)  # criando as tabelas no banco de dados
    # print(table_name)  # mostrando o nome das tabelas
"""

# criando a conexão do banco local
str_connection = "sqlite:///{path}"
str_connection = str_connection.format(path=os.path.join(DATA_DIR, "olist.db"))
connection = sqlalchemy.create_engine(str_connection)

# percorrendo por cada arquivo .csv do diretório data
for i in files_names:
    df_temp = pd.read_csv(os.path.join(DATA_DIR, i))  # lendo cada um dos arquivos csv
    table_name = "tb_" + i.strip(".csv").replace("olist_", "").replace("_dataset", "")  # definindo o nome da tabelas  
    df_temp.to_sql(table_name, connection)  # criando as tabelas no banco de dados
    # print(table_name)  # mostrando o nome das tabelas
