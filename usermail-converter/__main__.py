import sys
import webbrowser
from . import converters
from pyautogui import hotkey
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from .UI import Ui_MainWindow

class App(QMainWindow, Ui_MainWindow):
    # Init the App
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self) # Preload the UI
        self.initWatchers() # Start the watchers/listners (howerver you call it :D)
        self.show() # Show the UI once everything is ready


    #Manages the Watchers/Listners for Different Buttons and Events Triggers
    def initWatchers(self):
        # Placeholders for variables
        self.version = "1.0"
        self.radioChecked = False
        self.radioBtns = [self.radioE2U, self.radioEP2UP, self.radioU2E, self.radioUP2EP]

        # Watchers/Listners for Events Triggers
        self.importBtn.clicked.connect(self.importFile)

        self.textArea.textChanged.connect(self.textAreaWatcher)

        self.copyTxtBtn.clicked.connect(lambda:self.textAreaBtnsManager("copy"))
        self.clearTxtBtn.clicked.connect(lambda:self.textAreaBtnsManager("clear"))
        self.saveTxtBtn.clicked.connect(lambda:self.textAreaBtnsManager("save"))

        for radio in self.radioBtns:
            radio.clicked.connect(lambda: self.btnsManager("convertOn"))

        self.convertBtn.clicked.connect(self.doConvert)

        self.mb_import.triggered.connect(self.importFile)
        self.mb_save.triggered.connect(self.saveFile)

        self.mb_cut.triggered.connect(lambda:hotkey("ctrl", "x"))
        self.mb_copy.triggered.connect(lambda:hotkey("ctrl", "c"))
        self.mb_paste.triggered.connect(lambda:hotkey("ctrl", "v"))

        self.mb_undo.triggered.connect(self.textArea.undo)
        self.mb_redo.triggered.connect(self.textArea.redo)

        self.mb_report.triggered.connect(lambda: webbrowser.open("https://github.com/ThamiMemel/UserMail_Converter/issues", 2, True))
        self.mb_howto.triggered.connect(lambda: self.popup("Help", "1- Past or Import a list to convert\n2-Select the conversion mode\n3- Enter the mail domain if converting usernames to emails\n4-Press convert", "info"))
        self.mb_about.triggered.connect(lambda: self.popup("About", f"UserMail Converter\nMade By: Thami Memel\nmemelthami@gmail.com\n\nversion: {self.version}\nLisence: GPLv3","info"))
    
    # Open the file selected by "openFileNameDialog" and set it's content to textArea if possible
    def importFile(self):
        filepath = self.openFileNameDialog()
        if filepath:
            try:
                with open(filepath) as f:
                    result = ""
                    for line in f:
                        result += line
                self.textArea.setPlainText(result)
            except Exception:
                # Popup error if it cannot read the file
                self.popup("Error", "Couldn't Import the File", "crit")


    # Save the content of textArea to a file
    def saveFile(self, data):
        filepath = self.saveFileDialog()
        if filepath:
            try:
                with open(filepath, "w") as f:
                    f.write(data)
                f.close()
                self.popup("Success", "File saved successfully", "info")
            except Exception:
                # Popup error if it cannot save the file
                self.popup("Error", "Couldn't save the file", "crit")
    

    #  Popup a message "QMessageBox"-
    def popup(self, title, message, mode):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        if mode == "info": msg.setIcon(QMessageBox.Information)
        elif mode == "warn": msg.setIcon(QMessageBox.Warning)
        elif mode == "crit": msg.setIcon(QMessageBox.Critical)
        msg.exec_()


    # Open the file selection dialog and return the path to the file selected
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path, _ = QFileDialog.getOpenFileName(None, "Import a File", "","All Files (*);;Text Files (*.txt)", "/home", options=options)
        if path: return path


    # Open the file save dialog and return the path to save
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path, ext = QFileDialog.getSaveFileName(self,"Save to a File","","Text Files (*.txt);;All Files (*)", options=options)
        if path:
            ext = ext[ext.index("*") + 1:len(ext) - 1]
            return path + ext


    # Enables and Disables the radio and toolbar import buttons based on if there is a text or not
    def textAreaWatcher(self):
        if self.textArea.toPlainText():
            self.btnsManager("radioOn")
            self.mb_save.setEnabled(True)
        else:
            self.btnsManager("radioOff")
            self.mb_save.setEnabled(False)


    # Manages the textArea buttons (copy, clear and select all)
    def textAreaBtnsManager(self, action):
        if self.textArea.toPlainText(): # Make sure the text Area isn't empty
            if action == "copy":
                self.textArea.selectAll()
                self.textArea.copy()
                self.popup("copied", "text copied", "info")
            elif action == "save":
                self.saveFile(self.textArea.toPlainText())
            elif action == "clear":
                self.textArea.clear()
   

    # Manages enabling and disabling buttons 
    def btnsManager(self, mode):
        # Switching Mail Domain Input On and Off Depending On The Radio Button Checked
        def checkMailInput():
            # Enables mailDomainInput if user to email mode is selected
            if self.radioU2E.isChecked() or self.radioUP2EP.isChecked(): 
                self.mailDomainInput.setEnabled(True)
            # Disables mailDomainInput if not
            else: self.mailDomainInput.setEnabled(False)
        
        # Enables all radio buttons if n == 1, Disables them if n == 0
        def switchRadio(n):
            if n == 0: 
                self.convertBtn.setEnabled(False)
                self.mailDomainInput.setEnabled(False)
                # Disable all radio
                for radio in self.radioBtns:
                    radio.setEnabled(False)
            else:
                if self.radioChecked: self.convertBtn.setEnabled(True)
                checkMailInput() # Check if mailDomainInput should be enabled
                # Enable all radio
                for radio in self.radioBtns:
                    radio.setEnabled(True) 
        
        if mode == "radioOn": switchRadio(1)
        elif mode == "radioOff": switchRadio(0)
        elif mode == "convertOn":
            self.convertBtn.setEnabled(True)
            self.radioChecked = True # Set the glbal variable to be used by switchRadio(1)|btnsManager("radioOn")
            checkMailInput() # Check if mailDomainInput should be enabled
    

    # Simply convert :D
    def doConvert(self):
        # Make sure a domain is specified if required
        if not ((self.radioU2E.isChecked() or self.radioUP2EP.isChecked()) and self.mailDomainInput.text()):
            self.popup("Error", "Please enter a domain \n eg: gmail.com", "warn")
            return
        
        domain = self.mailDomainInput.text()
        converted = ""
        toConv = self.textArea.toPlainText()
        lines = toConv.split("\n") # Split text to lines list

        for line in lines:
            if line: # Get rid of emty line
                if self.radioE2U.isChecked():
                    converted += converters.mail_user(line)
                elif self.radioEP2UP.isChecked():
                    converted += converters.mailpass_userpass(line)
                elif self.radioU2E.isChecked():
                    converted += converters.user_mail(line, domain)
                elif self.radioUP2EP.isChecked():
                    converted += converters.userpass_mailpass(line, domain)
                converted += "\n" # New Line
        
        self.textArea.setPlainText(converted) # Update text area
        self.popup("Done", "Converted", "info")
                
def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

