import PyQt5.QtWidgets as qtw
#changing size and fonts of label
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #add a title
        self.setWindowTitle("My First App")

        #Set Layout
        self.setLayout(qtw.QVBoxLayout())

        #create a label
        my_label = qtw.QLabel("Hello World!")
        #change widget font size
        my_label.setFont(qtg.QFont('Helvetica', 18))
        #add the text label to the layout
        self.layout().addWidget(my_label)

        #create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        #add the entry box to the layout
        self.layout().addWidget(my_entry)

        #create a button
        my_button = qtw.QPushButton("Press Me!",
               #perform an operation onclicked
               clicked = lambda: press_it() 
            )
        #add the button to the layout
        self.layout().addWidget(my_button)

        # #create a date widget
        # date_box = qtw.QDateEdit()
        # self.layout().addWidget(date_box)

        self.show()

        #define the press_it function
        def press_it():
            my_label.setText(f'Hello {my_entry.text()}')
            my_entry.setText("")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()

        