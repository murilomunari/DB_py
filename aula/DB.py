import cx_Oracle


def create_table():
    try:
        conn = getConnection
        cursor = conn.cursor
        sql_query = """ CREATE TABLE CEO_DATAILS(
        FIRST_NAME VARCHAR2(50),
        LAST_NAME VARCHAR2(50),
        COMPANY VARCHAR2(50)
        AGE NUMBER
        ) """
        cursor.execute(sql_query)
        print("Table created successfully")
    except Exception as e:
        print("eror occurred while creating the table", e)
    finally:
        if (conn):
            closeConnection(conn, cursor)


# criar uma conexão com o BD Oracle
def getConnection():
    try:
        connection = cx_Oracle.connect('rm94164', '200101', 'oracle.fiap.com.br/orcl')
        print('conexão: ', connection.version)
    except Exception as e:
        print(f'Erro os ao obter conexão: {e}')
        return connection


def insert():
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO CEO_DETAILS values('Steve', 'jobs', 'Apple', '50')"
    try:
        cursor.execute(sql_query)
        conn.commit()
        print("Resgisto inserido")
    except Exception as e:
        print(f'Erro ao inserir o registro: {e}')
    finally:
        cursor.close()
        conn.close()


def insertParemetros(first_name, last_name, company, age):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO CEO_DETAILS (first_name, last_name, company, age) VALUES({first_name}, {last_name}, {comoany},{age})"

    data = (
        first_name,
        last_name,
        company,
        age
    )
    try:
        cursor.execute(sql_query, data)
        conn.commit()
        print("registro inserido")
    finally:
        cursor.close()
        conn.close()


def select():
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "SELECT * FROM CEO_DETILS WHERE NAME='Steve'"
    try:
        cursor.execute(sql_query)
        for result in cursor:
            print(result)
    except Exception as e:
        print(f"Erro ao obter o registro: {e}")
    finally:
        cursor.close()
        conn.close()


def update():
    conn = getConnection()
    cursor = conn.cursor()
    sql_update = "UPDATE CRO_DATEILS SET COMPANY='Microsoft' WHERE NAME='Steve'"


def delete():
    conn = getConnection()
    cursor = conn.cursor()
    sql_delete = "DELETE FROM CEO_DETAILS WHERE FIRST_NAME='Steve'"
    try:
        cursor.execute(sql_delete)
        conn.commit()
        print("registro deletado")
    except Exception as e:
        conn.rollback()
        print(f'Erro ao deletar o registro {e}')
    finally:
        cursor.close()
        conn.close()


# pricipal
select()
insert()
select()
update()
select()
delete()