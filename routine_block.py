import tkinter as tk

class BlockButton:
    def __init__(self, master, text, width, height, font_size=12):
        self.master = master
        self.text = text
        self.state = False
        self.font_size = font_size
        self.width = width
        self.height = height
        self.button = tk.Button(master, text=text, width=width, height=height, command=self.toggle_state, bg="white", font=("Helvetica", self.font_size))
    
    def toggle_state(self):
        self.state = not self.state
        if self.state:
            self.button.config(bg="#8DB600")  # Light green color
        else:
            self.button.config(bg="white")

class Application:
    def __init__(self, master):
        self.master = master
        self.blocks = ['3km Run', 'Lee 30x5set', 'biceps 3set', 'push up 20x3set','embedded 1','Maple','Water Bottle x 4 ', 'Face wash' ]
        self.block_width = 14
        self.block_height = 4
        self.create_blocks()
        self.create_refresh_button()

    def create_blocks(self):
        self.block_buttons = []
        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                if index < len(self.blocks):
                    block_text = self.blocks[index]
                    block = BlockButton(self.master, block_text, self.block_width, self.block_height)
                    block.button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
                    self.block_buttons.append(block)

    def create_refresh_button(self):
        self.refresh_button = tk.Button(self.master, text="Refresh", command=self.refresh_blocks)
        self.refresh_button.grid(row=3, column=0, columnspan=3, pady=10, sticky="nsew")

    def refresh_blocks(self):
        for block_button in self.block_buttons:
            block_button.state = False
            block_button.button.config(bg="white")

def main():
    root = tk.Tk()
    root.title("Block Buttons")
    # Set window size with 3:2 aspect ratio
    width = 250
    height = 180
    root.geometry(f"{width*2}x{height*2}")

    app = Application(root)
    
    # Configure block sizes based on window size
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    app.refresh_button.grid(sticky="nsew")
    for block in app.block_buttons:
        block.button.grid_configure(sticky="nsew")

    root.mainloop()

if __name__ == "__main__":
    main()
