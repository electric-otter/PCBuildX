import tkinter as tk
import os
import importlib.util

NODES_DIR = "nodes"  # Directory containing .py node files

class Node(tk.Canvas):
    def __init__(self, master, x, y, name="Node"):
        super().__init__(master.canvas, width=100, height=50, bg="lightgray", highlightthickness=0)
        self.x, self.y = x, y
        self.name = name
        self.create_rectangle(2, 2, 98, 48, outline="black")
        self.create_text(50, 25, text=self.name)
        self.pack()
        self.place(x=self.x, y=self.y)
        self.bind("<B1-Motion>", self.move)
        self.bind("<ButtonRelease-1>", self.release)
        self.bind("<ButtonPress-1>", self.press)
        self.is_dragging = False

    def move(self, event):
        if self.is_dragging:
            self.x, self.y = self.x + event.x - self.start_x, self.y + event.y - self.start_y
            self.place(x=self.x, y=self.y)

    def release(self, event):
        self.is_dragging = False

    def press(self, event):
        self.is_dragging = True
        self.start_x, self.start_y = event.x, event.y

class NodeEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Node Editor")
        self.geometry("1000x600")
        
        # Create a frame for the toolbox
        self.toolbox = tk.Frame(self, width=200, height=600, bg="gray")
        self.toolbox.pack(side="left", fill="y")

        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack(side="right", expand=True, fill="both")

        self.nodes = []
        
        self.load_nodes_from_files()

    def add_node(self, name):
        x, y = 250, 100  # Default placement
        node = Node(self, x, y, name)
        self.nodes.append(node)

    def load_nodes_from_files(self):
        """Load node scripts from the nodes/ directory and create toolbox buttons."""
        if not os.path.exists(NODES_DIR):
            os.makedirs(NODES_DIR)

        for filename in os.listdir(NODES_DIR):
            if filename.endswith(".py"):
                node_name = filename[:-3]  # Remove .py extension
                btn = tk.Button(self.toolbox, text=node_name, command=lambda n=node_name: self.add_node(n))
                btn.pack(fill="x", padx=5, pady=5)

if __name__ == "__main__":
    editor = NodeEditor()
    editor.mainloop()
