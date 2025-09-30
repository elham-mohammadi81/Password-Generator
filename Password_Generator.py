from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QFrame,QPushButton,QCheckBox,QSpinBox,QSlider,QRadioButton,QMessageBox
from PyQt5 import uic
import sys 
import random

class Password_Generator(QMainWindow):
    def __init__(self):
        super(Password_Generator,self).__init__()

        # Load the Ui file 
        uic.loadUi("Password_Generator.ui",self)

        # Define All Widgets 
        self.AppTitel = self.findChild(QLabel,"PasswordGenerator_label")
        self.CustomizeTitle = self.findChild(QLabel,"CustomPass")

        self.Qframe_1 = self.findChild(QFrame,"frame")
        self.Qframe_2 = self.findChild(QFrame,"frame_2")
        self.Qframe_3 = self.findChild(QFrame,"frame_3")
        self.Qframe_4 = self.findChild(QFrame,"frame_4")

        # Radio buttons (password type options)
        self.EasyToSayRB = self.findChild(QRadioButton,"EasyToSayRB")
        self.EasyToReadRB = self.findChild(QRadioButton,"EasyToReadRB")
        self.AllCharacters = self.findChild(QRadioButton,"AllChaRB")

        # Checkboxes (character set options)
        self.LowerCaseChB = self.findChild(QCheckBox,"LowerCaseChB")
        self.UpperCaseChB = self.findChild(QCheckBox,"UpperCaseChB")
        self.NumbersChB = self.findChild(QCheckBox,"NumberChB")
        self.SymbolsChB = self.findChild(QCheckBox,"SymbolChB")

        # SpinBox and Slider for password length
        self.SpinBox = self.findChild(QSpinBox,"spinBox")
        self.Slider = self.findChild(QSlider,"horizontalSlider")

        # Buttons
        self.GeneratorButton = self.findChild(QPushButton,"GenerateButton")
        self.CopyButton_1 = self.findChild(QPushButton,"Copy_1")
        self.CopyButton_2 = self.findChild(QPushButton,"Copy_2")
        self.CopyButton_3 = self.findChild(QPushButton,"Copy_3")
        self.CopyButton_4 = self.findChild(QPushButton,"Copy_4")

        # Labels for generated passwords
        self.Password_1 = self.findChild(QLabel,"Password_1")
        self.Password_2 = self.findChild(QLabel,"Password_2")
        self.Password_3 = self.findChild(QLabel,"Password_3")
        self.Password_4 = self.findChild(QLabel,"Password_4")

        # Connect radio buttons to enabling/disabling checkboxes 
        self.EasyToSayRB.toggled.connect(self.setEnabel_)   
        self.EasyToReadRB.toggled.connect(self.setEnabel_)
        self.AllCharacters.toggled.connect(self.setEnabel_)

        # Sync SpinBox and Slider values
        self.SpinBox.setValue(12)
        self.SpinBox.valueChanged.connect(self.Slider.setValue)
        self.Slider.setValue(12)
        self.Slider.valueChanged.connect(self.SpinBox.setValue)

        # Generate password when button is clicked
        self.GeneratorButton.clicked.connect(self.customize_password)

        # Connect copy buttons
        self.CopyButton_1.clicked.connect(lambda : self.copy_password(1))
        self.CopyButton_2.clicked.connect(lambda : self.copy_password(2))
        self.CopyButton_3.clicked.connect(lambda : self.copy_password(3))
        self.CopyButton_4.clicked.connect(lambda : self.copy_password(4))

        # Default: all options enabled
        self.AllCharacters.setChecked(True)
        self.LowerCaseChB.setChecked(True)
        self.UpperCaseChB.setChecked(True)
        self.NumbersChB.setChecked(True)
        self.SymbolsChB.setChecked(True)
        self.customize_password()


        self.show()
    
    def setEnabel_(self):
        '''Enable/disable checkboxes based on selected radio button'''
        if self.EasyToSayRB.isChecked():
            self.NumbersChB.setEnabled(False)
            self.SymbolsChB.setEnabled(False)

        elif self.EasyToReadRB.isChecked():
            self.NumbersChB.setEnabled(True)
            self.SymbolsChB.setEnabled(True)

        elif self.AllCharacters.isChecked():
            self.NumbersChB.setEnabled(True)
            self.SymbolsChB.setEnabled(True)
    
    
    def customize_password(self):
        '''Prepare character sets based on user selection'''
        password_length = self.SpinBox.value()
        
        if self.EasyToSayRB.isChecked():
            password_includ = {
            "LowerCaseChB" : [chr(i) for i in range(97,123)] if self.LowerCaseChB.isChecked() else False ,
            "UpperCaseChB": [chr(i) for i in range(65,91)] if self.UpperCaseChB.isChecked() else False
            }
            self.generate_password(password_includ,password_length)
            

        elif self.EasyToReadRB.isChecked():
            password_includ = {
            "LowerCaseChB" : [chr(i) for i in range(97,123)] if self.LowerCaseChB.isChecked() else False ,
            "UpperCaseChB": [chr(i) for i in range(65,91)] if self.UpperCaseChB.isChecked() else False ,
            "NumbersChB" : [str(num) for num in range(9)] if self.NumbersChB.isChecked() else False ,
            "SymbolsChB" : list("!@#$%^&*_|<>?") if self.SymbolsChB.isChecked() else False
            }
            self.generate_password(password_includ,password_length)
            
        elif self.AllCharacters.isChecked():
            password_includ = {
            "LowerCaseChB" : [chr(i) for i in range(97,123)] if self.LowerCaseChB.isChecked() else False ,
            "UpperCaseChB": [chr(i) for i in range(65,91)] if self.UpperCaseChB.isChecked() else False,
            "NumbersChB" : [str(num) for num in range(9)] if self.NumbersChB.isChecked() else False ,
            "SymbolsChB" : list("!@#$%^&*_|<>?") if self.SymbolsChB.isChecked() else False 
            }
            self.generate_password(password_includ,password_length)
            
    
    def generate_password(self,pas_include , length):
        '''Generate 4 random passwords based on selected character sets'''

        noChar = ['i', 'I', 'l', 'L', '1', 'o', 'O', '0']
        password_chars = []
        # Collect all selected characters
        for pass_incl , check_ in pas_include.items():
            if check_ != False :
                for item in check_:
                    password_chars.append(item)
        try: 
            # Generate 4 passwords
            passwords = []
            for _ in range(4):
                password = ''
                while len(password) < length:
                    choice_item = random.choice(password_chars)
                    # EasyToRead: avoid confusing characters and duplicates
                    if self.EasyToReadRB.isChecked():
                        if choice_item not in noChar and choice_item not in password:
                            password += choice_item
                    else:
                        password += choice_item

                passwords.append(password)

            # Display passwords in labels
            self.Password_1.setText(passwords[0])
            self.Password_2.setText(passwords[1])
            self.Password_3.setText(passwords[2])
            self.Password_4.setText(passwords[3])
        # If no characters were selected, show error
        except:
            self.Password_1.setText("")
            self.Password_2.setText("")
            self.Password_3.setText("")
            self.Password_4.setText("")
            QMessageBox.about(self,"Error","At least one option must be selected to generate a password.")

 
    def copy_password(self,witch):
        '''Copy/save selected password into file'''
        if witch == 1 :
            text = self.Password_1.text()
            QApplication.clipboard().setText(text)

        elif witch == 2 :
            text = self.Password_2.text()
            QApplication.clipboard().setText(text)

        elif witch == 3 :
            text = self.Password_3.text()
            QApplication.clipboard().setText(text)

        elif witch == 4 :
            text = self.Password_4.text()
            QApplication.clipboard().setText(text)

        
        # Save the password into a text file (append mode)
        try:
            with open("save_passwords.csv" , "r") as reader : 
                exist_pass = [line.strip() for line in reader.readlines()]
        except FileNotFoundError:
            exist_pass = []

        if text not in exist_pass :
            with open("save_passwords.csv" , "a") as writer:
                writer.write(text + "\n")
        
# Run the application
app = QApplication(sys.argv)
window = Password_Generator()
app.exec_()