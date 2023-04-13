from PyQt5.QtWidgets import QApplication
from App import App
import sys

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    # sys.exit(app.exec_())
    print(app.exec_())
