import tkinter as tk

class StickmanApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # Remove window borders
        self.root.attributes("-toolwindow", True)  # Make it look like a small tool window
        self.root.attributes("-topmost", True)  # Keep it on top
        self.root.attributes("-transparentcolor", "white")  # Make the background transparent

        self.canvas = tk.Canvas(self.root, width=50, height=100, bg='white', highlightthickness=0, bd=0)
        self.canvas.pack()

        self.stickman_frames = [1, 2, 3]
        self.current_frame = 0
        self.position_x = 0
        self.position_y = self.root.winfo_screenheight() - 135  # Initial Y position, respect dragging
        self.direction = 1

        self.animate()
        self.move_stickman()

        # Bind double-click event to close the app
        self.root.bind("<Double-1>", self.close_app)  # Double-click to close

        # Variables for draggable functionality
        self.drag_data = {"x": 0, "y": 0}

        # Bind mouse events to make the window draggable
        self.root.bind("<ButtonPress-1>", self.on_drag_start)
        self.root.bind("<B1-Motion>", self.on_drag_motion)

    def draw_stickman(self, frame):
        color = "#FF6F00"
        width = 5
        self.canvas.delete("all")
        self.canvas.create_oval(15, 10, 35, 30, outline=color, width=width)  # Head
        self.canvas.create_line(25, 30, 25, 70, fill=color, width=width)  # Body
        if frame == 1:
            self.canvas.create_line(25, 30, 10, 50, fill=color, width=width)  # Left arm
            self.canvas.create_line(25, 30, 45, 0, fill=color, width=width)  # Right arm
        elif frame == 2:
            self.canvas.create_line(25, 30, 10, 50, fill=color, width=width)  # Left arm
            self.canvas.create_line(25, 30, 40, 50, fill=color, width=width)  # Right arm
        else:
            self.canvas.create_line(25, 30, 20, 40, fill=color, width=width)  # Left arm
            self.canvas.create_line(25, 30, 40, 40, fill=color, width=width)  # Right arm

        if frame == 1:
            self.canvas.create_line(25, 70, 15, 90, fill=color, width=width)  # Left leg
            self.canvas.create_line(25, 70, 35, 85, fill=color, width=width)  # Right leg
        else:
            self.canvas.create_line(25, 70, 10, 85, fill=color, width=width)  # Left leg
            self.canvas.create_line(25, 70, 30, 90, fill=color, width=width)  # Right leg
        if self.position_x >= self.root.winfo_screenwidth():
            self.position_x = 0

    def animate(self):
        self.current_frame = (self.current_frame + 1) % 3
        self.draw_stickman(self.current_frame + 1)
        self.root.after(1000, self.animate)

    def move_stickman(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.position_x += 5 * self.direction
        self.direction = 1

        # Check if the stickman has moved off the right edge of the screen
        if self.position_x >= screen_width:
            self.position_x = 0
            self.position_y += 100  # Move to the next row of monitors (simulate)

        # Check if the stickman has moved off the bottom edge of the screen
        if self.position_y >= screen_height - 135:
            self.position_y = screen_height - 135  # Stay within the screen limits

        # Ensure the stickman stays within the screen boundaries when dragged
        if self.position_x < 0:
            self.position_x = 0
        if self.position_y < 0:
            self.position_y = 0

        self.root.geometry(f"50x100+{self.position_x}+{self.position_y}")
        self.root.after(1000, self.move_stickman)
        if self.position_y >= screen_height - 135:
            self.position_y = screen_height - 135

    def close_app(self, event):
        """Handle double-click to close the app"""
        self.root.quit()
        self.root.destroy()

    def on_drag_start(self, event):
        """Record the position of the mouse when dragging starts"""
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drag_motion(self, event):
        """Move the window when dragging"""
        delta_x = event.x - self.drag_data["x"]
        delta_y = event.y - self.drag_data["y"]
        new_x = self.root.winfo_x() + delta_x
        new_y = self.root.winfo_y() + delta_y
        self.position_x = new_x  # Update stickman's position
        self.position_y = new_y  # Update stickman's position
        self.root.geometry(f"+{new_x}+{new_y}")

if __name__ == "__main__":
    app = StickmanApp()
    app.root.mainloop()
