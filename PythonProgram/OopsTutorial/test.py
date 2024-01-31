import tkinter as tk

class ActionModel:
    def __init__(self):
        self.button = tk.Button(text="Click me!")
        self.button.pack()

        self.button.bind("<Button-1>", self.on_button_click)

    def on_button_click(self, event):
        print("Button clicked!")

if __name__ == "__main__":
    action_model = ActionModel()
    action_model.button.mainloop()