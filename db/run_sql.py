import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    result = []

    try:
        conn=psycopg2.connect("dbname='task_manager'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        result = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return result