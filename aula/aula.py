'''
1. Oracle DB
2.Python lib (bibliotecas Python)
3. DB details
4. Driver - cx_Oracle / oracledb

PEP 249 - Python Database API Specification v2

Modulos
cx_Oracle | oracle - Oracle Databse
pyodbc - Microsoft SQL Sever
pymysql - MySQL
ppsycopg2 - PostgreSQL

Passos:
1.Estabelecer uma conexão entre Python com o DB
        connection = cx_Oracle.connect(database connection string)

2. Obter um cursor (objeto para executar queries e obter resultado apos a execução)
cursor = connection.cursor
'''


import cx_Oracle


#create connection
conn = cx_Oracle.connect(user = 'rm94164', password='200101', host='oracle.fiap.com.br',
                         port= '1521', service_name= 'orcl')

print(conn.version)


#create cursor
cursor = conn.cursor()


sql_create = '''
CREATE TABLE CEO_DETAILS(
    FIRST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    COMPANY VARCHAR2(50),
    AGE NUMBER
);
'''


#execute query
cursor.excute(sql_create)
print('tabela criada!')