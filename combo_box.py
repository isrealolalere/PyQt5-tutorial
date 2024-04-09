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
        my_label = qtw.QLabel("Pick something from the list below")
        #change widget font size
        my_label.setFont(qtg.QFont('Helvetica', 18))
        #add the text label to the layout
        self.layout().addWidget(my_label)

        #create an Combo box
        my_combo = qtw.QComboBox(self,
                #This is to make it editable
                editable=True,
                insertPolicy=qtw.QComboBox.InsertAtTop
            )
        # Add items to the combo box
        my_combo.addItem("Pepperoni", "Something")
        my_combo.addItem("Cheese", 2)
        my_combo.addItem("Mushroom", qtw.QWidget)
        #alternatively
        # my_combo.addItems(["One", "Two", "Three"])
        
        #add the text label to the layout
        self.layout().addWidget(my_combo)
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
            my_label.setText(f'You picked {my_combo.currentText()}')
            # my_label.setText(f'You picked {my_combo.currentData()}')
            # my_label.setText(f'You picked {my_combo.currentIndex()}')
            


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()

        