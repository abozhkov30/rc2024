import asyncpg

async def insert_in_users(user_id: int,
                          username: str,
                          first_name: str,
                          last_name: str,
                          language_code: str):
    try:
        conn = await asyncpg.connect(user='new_user', password='12345678',
                                     database='new_database', host='127.0.0.1')
        print("Соединение с базой данных успешно установлено.")
        
        # Выполнение запроса и получение данных
        await conn.execute("""INSERT INTO public.users(
  user_id, username, first_name, last_name, language_code)
  VALUES ($1, $2, $3, $4, $5);""", user_id, username, first_name, last_name, language_code)
        
        print("Данные успешно вставлены в таблицу users.")

        # Закрытие транзакции
        # conn.commit()

        # Закрытие соединения
        await conn.close()
        print("Соединение с базой данных закрыто.")
        
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")


async def run_connect():
    try:
        conn = await asyncpg.connect(user='new_user', password='12345678',
                                     database='new_database', host='127.0.0.1')
        print("Соединение с базой данных успешно установлено.")
        
        # Выполнение запроса и получение данных
        values = await conn.execute("""INSERT INTO public.users(
  user_id, username, first_name, last_name, language_code)
  VALUES ($1, $2, $3, $4, $5);""")
        
        # Вывод результата запроса
        for record in values:
            print(record)
        
        # Закрытие соединения
        await conn.close()
        print("Соединение с базой данных закрыто.")
        
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")