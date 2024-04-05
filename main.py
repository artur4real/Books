import pymysql
from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QFont, QImage, QPixmap
from PyQt5 import QtWidgets
from form import Ui_MainWindow

conn = pymysql.connect(host="localhost", user="root", password="", database="esayan")


def get_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books join author on author.id_author = books.id_author "
                   "join basket on books.id_books = basket.id_books")
    res = cursor.fetchall()
    print(res)
    return res


class Artur(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Artur, self).__init__(parent)
        self.setupUi(self)
        res_qw = get_data()
        print(res_qw)
        self.add_images(res_qw)

        self.add_labels(res_qw)

    def add_labels(self, data):
        height = 0
        for i, row in enumerate(data):
            height += 220
            font = QFont()
            font.setPointSize(12)
            font.setBold(True)

            label = QtWidgets.QLabel(self)
            label.setGeometry(20, height, 700, 100)
            label.setObjectName(f"label_{row[0]}")
            label.setFont(font)
            label.setText(f"{row[13]}:\n\n  {row[0]}. {row[1]}, {row[2]}, {row[7]} {row[8]}, {row[11]} ")

        font_label_2 = QFont()
        font_label_2.setPointSize(20)
        font_label_2.setBold(True)

        label_2 = QtWidgets.QLabel(self)
        label_2.setGeometry(320, 100, 200, 90)
        label_2.setObjectName("label_2")
        label_2.setFont(font_label_2)
        label_2.setText("Корзина")

    def add_images(self, data):
        height = 0
        for i, row in enumerate(data):
            height += 200
            qimg = QImage.fromData(QByteArray(row[3]))
            pixmap = QPixmap.fromImage(qimg)

            label = QtWidgets.QLabel(self)
            label.setGeometry(600, height, 700, 200)
            label.setPixmap(pixmap.scaledToWidth(100))
            label.setObjectName(f"label_{row[0]}")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = Artur()
    form.show()
    sys.exit(app.exec_())
