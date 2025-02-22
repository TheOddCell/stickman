import tkinter as tk

class StickmanApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)  
        self.root.attributes("-topmost", True)  
        self.root.attributes("-transparentcolor", "white")  

        self.canvas = tk.Canvas(self.root, width=50, height=100, bg='white', highlightthickness=0, bd=0)
        self.canvas.pack()

        self.stickman_frames = [1, 2, 3]
        self.current_frame = 0
        self.position_x = 0
        self.direction = 1  

        self.animate()
        self.move_stickman()

    def draw_stickman(self, frame):
        color="#FF6F00"
        width=5
        self.canvas.delete("all")
        self.canvas.create_oval(15, 10, 35, 30, outline=color, width=width)  
        self.canvas.create_line(25, 30, 25, 70, fill=color, width=width)  
        if frame == 1:
            self.canvas.create_line(25, 30, 10, 50, fill=color, width=width)  
            self.canvas.create_line(25, 30, 45, 0, fill=color, width=width)  
        elif frame == 2:
            self.canvas.create_line(25, 30, 10, 50, fill=color, width=width)  
            self.canvas.create_line(25, 30, 40, 50, fill=color, width=width)  
        else:
            self.canvas.create_line(25, 30, 20, 40, fill=color, width=width)  
            self.canvas.create_line(25, 30, 40, 40, fill=color, width=width)  

        if frame == 1:
            self.canvas.create_line(25, 70, 15, 90, fill=color, width=width)  
            self.canvas.create_line(25, 70, 35, 85, fill=color, width=width)  
        else:
            self.canvas.create_line(25, 70, 10, 85, fill=color, width=width)  
            self.canvas.create_line(25, 70, 30, 90, fill=color, width=width)

        if self.position_x >= self.root.winfo_screenwidth():
            self.position_x = 0

    def animate(self):
        self.current_frame = (self.current_frame + 1) % 3
        self.draw_stickman(self.current_frame + 1)
        self.root.after(1000, self.animate)

    def move_stickman(self):
        screen_width = self.root.winfo_screenwidth()
        self.position_x += 5 * self.direction
        self.direction = 3

        self.root.geometry(f"50x100+{self.position_x}+{self.root.winfo_screenheight() - 135}")
        self.root.after(1000, self.move_stickman)

if __name__ == "__main__":
    app = StickmanApp()
    app.root.mainloop()  