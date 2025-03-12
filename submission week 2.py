import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QRadioButton,
                             QComboBox, QFormLayout, QVBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt

class RegistrationForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Week 2 : Layout - User Registration Form")

        self.createIdentitasGroupBox()
        self.createNavigationLayout()
        self.createUserRegistrationGroupBox()
        self.createActionsLayout()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.identitasGroupBox)
        mainLayout.addWidget(self.navigationGroupBox)
        mainLayout.addWidget(self.userRegistrationGroupBox)
        mainLayout.addLayout(self.actionsLayout)

        self.setLayout(mainLayout)

    def createIdentitasGroupBox(self):
        self.identitasGroupBox = QGroupBox("Identitas")

        namaLabel = QLabel("Nama: Rizki Rahman Maulana")
        nimLabel = QLabel("NIM: F1D022093")
        kelasLabel = QLabel("Kelas: D")

        layout = QVBoxLayout()
        layout.addWidget(namaLabel)
        layout.addWidget(nimLabel)
        layout.addWidget(kelasLabel)

        self.identitasGroupBox.setLayout(layout)

    def createNavigationLayout(self):
        self.navigationGroupBox = QGroupBox("Navigation (horizontal box layout)")
        layout = QHBoxLayout()
        self.homeButton = QPushButton("Home")
        self.aboutButton = QPushButton("About")
        self.contactButton = QPushButton("Contact")

        layout.addWidget(self.homeButton)
        layout.addWidget(self.aboutButton)
        layout.addWidget(self.contactButton)
        layout.addStretch()

        self.navigationGroupBox.setLayout(layout)

    def createUserRegistrationGroupBox(self):
        self.userRegistrationGroupBox = QGroupBox("User Registration (form layout)")

        fullNameLabel = QLabel("Full Name:")
        self.fullNameLineEdit = QLineEdit()

        emailLabel = QLabel("Email:")
        self.emailLineEdit = QLineEdit()

        phoneLabel = QLabel("Phone:")
        self.phoneLineEdit = QLineEdit()

        genderLabel = QLabel("Gender:")
        self.maleRadioButton = QRadioButton("Male")
        self.femaleRadioButton = QRadioButton("Female")
        self.maleRadioButton.setChecked(True)

        genderLayout = QHBoxLayout()
        genderLayout.addWidget(self.maleRadioButton)
        genderLayout.addWidget(self.femaleRadioButton)

        countryLabel = QLabel("Country:")
        self.countryComboBox = QComboBox()
        self.countryComboBox.addItems(["Select country", "Indonesia", "America", "Japan", "Australia"])

        formLayout = QFormLayout()
        formLayout.addRow(fullNameLabel, self.fullNameLineEdit)
        formLayout.addRow(emailLabel, self.emailLineEdit)
        formLayout.addRow(phoneLabel, self.phoneLineEdit)
        formLayout.addRow(genderLabel, genderLayout)
        formLayout.addRow(countryLabel, self.countryComboBox)

        self.userRegistrationGroupBox.setLayout(formLayout)

    def createActionsLayout(self):
        self.actionsLayout = QHBoxLayout()
        self.submitButton = QPushButton("Submit")
        self.cancelButton = QPushButton("Cancel")

        self.submitButton.clicked.connect(self.onSubmit)
        self.cancelButton.clicked.connect(self.onCancel)

        self.actionsLayout.addWidget(self.submitButton)
        self.actionsLayout.addWidget(self.cancelButton)
        self.actionsLayout.addStretch()

    def onSubmit(self):
        QMessageBox.information(self, "Form Submitted", "Your form was submitted successfully!")

    def onCancel(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())
