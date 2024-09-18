import asyncpg

async def get_db_connection():
    try:
        conn = await asyncpg.connect(user='new_user', password='12345678',
                                     database='new_database', host='127.0.0.1')
        print("Соединение с базой данных успешно установлено.")
        return conn
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None

async def insert_in_users(user_id: int,
                          username: str,
                          first_name: str,
                          last_name: str,
                          language_code: str):
    conn = await get_db_connection()  # Получаем соединение через отдельную функцию
    if conn is None:
        print("Не удалось подключиться к базе данных.")
        return False
    
    try:
        # Выполнение запроса
        await conn.execute("""
            INSERT INTO public.users (user_id, username, first_name, last_name, language_code)
            VALUES ($1, $2, $3, $4, $5);
        """, user_id, username, first_name, last_name, language_code)
        
        print("Данные успешно вставлены в таблицу users.")
        return True

    except Exception as e:
        print(f"Ошибка при вставке данных: {e}")
        return False
    finally:
        await conn.close()
        print("Соединение с базой данных закрыто.")

async def update_profiles(user_id: int,
                        #   expectations: str,
                        #   city: str,
                        #   ages:str,
                        #   position:str,
                        #   outcome:str,
                          is_active: bool,
                          date_modified:int):
    conn = await get_db_connection()  # Получаем соединение через отдельную функцию
    if conn is None:
        print("Не удалось подключиться к базе данных.")
        return False

    try:
        conn = await asyncpg.connect(user='new_user', password='12345678',
                                    database='new_database', host='127.0.0.1')
        print("Соединение с базой данных успешно установлено.")
        
        # Выполнение запроса и получение данных
        await conn.execute("""UPDATE public.profiles
                            SET date_modified = $1, is_active = $2
                            WHERE user_id = $3;""", date_modified, is_active, user_id)
        
        print("Данные успешно вставлены в таблицу profiles.")    
        return True

    except Exception as e:
        print(f"Ошибка при вставке данных: {e}")
        return False
    finally:
        await conn.close()
        print("Соединение с базой данных закрыто.")