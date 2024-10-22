from PyQt5.QtWidgets import QApplication, QInputDialog, QMessageBox

def get_user_input():
    text, ok = QInputDialog.getText(None, "Input Dialog", "Enter your text:")

    if ok:
        # Text entered by user
        print(text)
        # Perform task with user input
        perform_task(text)
    else:
        print("User cancelled")

def perform_task(text):
    # Your task logic here
    print(f"Performing task with input: {text}")

if __name__ == "__main__":
    app = QApplication([])
    get_user_input()
    app.exec_()