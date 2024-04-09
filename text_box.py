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
        my_label = qtw.QLabel("Type something into the text box below", self)
        #change widget font size
        my_label.setFont(qtg.QFont('Helvetica', 18))
        #add the text label to the layout
        self.layout().addWidget(my_label)

        # Create a Text box
        my_text = qtw.QTextEdit(self,
                acceptRichText= True,
                lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                lineWrapColumnOrWidth=50,
                placeholderText="Hello World!",
                readOnly=False,
            )

        #add the text label to the layout
        self.layout().addWidget(my_text)

        #create a button
        my_button = qtw.QPushButton("Press Me!",
               #perform an operation onclicked
               clicked = lambda: press_it() 
            )
        #add the button to the layout
        self.layout().addWidget(my_button)


        self.show()

   
        #define the press_it function
        def press_it():
            my_label.setText(f'You typed {my_text.toPlainText()} ')
            
            my_text.setPlainText("You pressed the button")

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
