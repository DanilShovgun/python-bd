import psycopg2

conn = psycopg2.connect(database="mydatabase", user="myusername", password="mypassword", host="localhost", port="5432")
print("Database opened successfully")

def create_table():
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS clients
                   (id SERIAL PRIMARY KEY,
                   first_name TEXT,
                   last_name TEXT,
                   email TEXT,
                   phone TEXT)''')
    print("Table created successfully")
    conn.commit()

# Добавление нового клиента
def add_client(first_name, last_name, email, phone):
    cur = conn.cursor()
    cur.execute('''INSERT INTO clients (first_name, last_name, email, phone)
                   VALUES (%s, %s, %s, %s)''', (first_name, last_name, email, phone))
    print("Client added successfully")
    conn.commit()

# Обновление информации о клиенте
def update_client(client_id, first_name, last_name, email, phone):
    cur = conn.cursor()
    cur.execute('''UPDATE clients SET first_name = %s, last_name = %s, email = %s, phone = %s WHERE id = %s''', (first_name, last_name, email, phone, client_id))
    print("Client updated successfully")
    conn.commit()

# Поиск клиента по имени, фамилии, email или телефону
def find_client(search_value):
    cur = conn.cursor()
    cur.execute('''SELECT * FROM clients WHERE first_name LIKE %s OR last_name LIKE %s OR email LIKE %s OR phone LIKE %s''', (f'%{search_value}%', f'%{search_value}%', f'%{search_value}%', f'%{search_value}%'))
    result = cur.fetchall()
    return result

# Закрытие соединения с базой данных
conn.close()
print("Connection closed")
