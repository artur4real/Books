import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="esayan")

def get_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books join author on author.id_author = books.id_books "
                   "join basket on books.id_books = basket.id_basket")
    res = cursor.fetchall()
    print(res)
    return res







