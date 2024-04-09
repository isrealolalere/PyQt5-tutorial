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

        #1 create an Spin box for a whole NO
        my_spin = qtw.QSpinBox(self, 
                value=10,
                maximum=100,
                minimum=0,
                singleStep=5,
                prefix="# ",
                suffix=" order"
            )
        #change widget font size
        my_spin.setFont(qtg.QFont('Helvetica', 18))
        #add the text label to the layout
        self.layout().addWidget(my_spin)

        #create a button
        my_button = qtw.QPushButton("Press Me!",
               #perform an operation onclicked
               clicked = lambda: press_it() 
            )
        #add the button to the layout
        self.layout().addWidget(my_button)
        
        #2 create an doubleSpin box for a decimal No
        my_double_spin = qtw.QDoubleSpinBox(self, 
                value=10,
                maximum=100,
                minimum=0,
                singleStep=5.5,
                prefix="# ",
                suffix=" order"
            )
        #change widget font size
        my_double_spin.setFont(qtg.QFont('Helvetica', 18))
        #add the text label to the layout
        self.layout().addWidget(my_double_spin)

        #create a button
        my_button = qtw.QPushButton("Press Me!",
               #perform an operation onclicked
               clicked = lambda: float_press_it() 
            )
        #add the button to the layout
        self.layout().addWidget(my_button)


        self.show()

        #define the press_it function
        def press_it():
            my_label.setText(f'You picked # {my_spin.value()} Order')
            # my_label.setText(f'You picked {my_combo.currentData()}')
            # my_label.setText(f'You picked {my_combo.currentIndex()}')
            
        #define the press_it function
        def float_press_it():
            my_label.setText(f'You picked # {my_double_spin.value()} Order')
            # my_label.setText(f'You picked {my_combo.currentData()}')
            # my_label.setText(f'You picked {my_combo.currentIndex()}')
            


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()

        