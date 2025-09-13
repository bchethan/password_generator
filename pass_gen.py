import sys, random, pyperclip
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from word_list import words_list

class sample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password generator App")
        self.setGeometry(500,300,500,500)
        self.input_box = QLineEdit(self)
        self.text_label = QLabel("Welcome to password generator",self)
        self.copy_button = QPushButton("Copy",self)
        self.generate_password = QPushButton("Generate Password",self)
        self.initUI()
        
    def initUI(self):
        self.text_label.setObjectName("text_label")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_label)
        vbox.addWidget(self.copy_button)
        vbox.addWidget(self.generate_password)
        vbox.addWidget(self.input_box)

        self.setLayout(vbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.text_label)
        hbox.addWidget(self.copy_button)
        
        vbox.addLayout(hbox)
        
        self.input_box.setPlaceholderText("Enter your Email/Username")
        self.generate_password.clicked.connect(self.generate_pass)
        self.copy_button.clicked.connect(self.copy_text)
    
    def generate_text(self):
        word = ""
        self.copy_button.setText("Copy")

        for i in range(4):
            word += random.choice(words_list)
            word += f"{random.randint(0,9)}" if i == 3 else f"{random.randint(0,9)}-"
        return word
    
    def copy_text(self):
        self.copy_button.setText("Copied to Clipboard")

        with open("generated_list.txt","a") as text_file:
            text_file.write(f"{self.input_box.text()} : {self.text_label.text()}\n")
        
        return pyperclip.copy(self.text_label.text())

    def generate_pass(self):
        self.text_label.setText(self.generate_text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sample1 = sample()
    sample1.show()

    sys.exit(app.exec_())