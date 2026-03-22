from database_connection import get_db_conn


def create_invoice(user_id:int,amount:float,description):
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            INSERT INTO invoices user_id,amount,description
            VALUES (%S, %S, %,s)
            RETURNING id,user_id, amount, description ,created_at 
            """,(user_id,amount,description))

            return cursor.fetchone()


def get_invoices():
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, user_id, amount ,description,created_at FROM invoices ORDER by id")

            return cursor.fetchall()

def get_invoice(invoice_id:int):
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(

                "SELECT id, user_id, amount ,description,created_at FROM invoices WHERE id=%s",
                (invoice_id,)
            )
            return cursor.fetchone()


def delete_invoice(invoice_id:int):
    with get_db_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM invoices WHERE id=%s",
                (invoice_id,)
            )





