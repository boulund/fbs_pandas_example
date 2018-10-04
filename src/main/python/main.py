from fbs_runtime.application_context import ApplicationContext, cached_property
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout

import sys

import pandas as pd

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):                              # 2. Implement run()
        self.window.setWindowTitle('Hello World!')
        self.window.resize(250, 150)
        self.window.show()
        return self.app.exec_()                 # 3. End run() with this line

    @cached_property
    def window(self):
        return MainWindow()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        df_label = QLabel()
        df_summary = QLabel()

        d = {'col1': [1, 2], 'col2': [3, 4]}
        df = pd.DataFrame(data=d)
        
        df_label.setText(str(df))
        df_summary.setText(str(df.describe()))

        layout = QGridLayout()
        layout.addWidget(df_label)
        layout.addWidget(df_summary)
        self.setLayout(layout)


if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)