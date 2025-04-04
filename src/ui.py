# ui.py
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph import ResourceAllocationGraph
import networkx as nx
from graph_utils import draw_graph

class ResourceAllocationGraphUI:
    def __init__(self, root):
        self.graph = ResourceAllocationGraph()
        self.root = root
        self.root.title("Resource Allocation Graph Simulator")
        self.root.configure(bg='#2C2F33')

        self.figure, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.controls_frame = tk.Frame(root, bg='#2C2F33')
        self.controls_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        for i in range(6):
            self.controls_frame.grid_columnconfigure(i, weight=1)

        btn_style = {'fg': 'white', 'padx': 10, 'pady': 5, 'font': ('Arial', 10, 'bold')}

        # Process controls
        tk.Label(self.controls_frame, text="Process:", bg='#2C2F33', font=("Arial", 12), fg='white').grid(row=0, column=0, padx=5, pady=5)
        self.process_entry = tk.Entry(self.controls_frame, width=15, font=("Arial", 12))
        self.process_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.controls_frame, text="Add", bg='#7289DA', **btn_style, command=self.add_process).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(self.controls_frame, text="Remove", bg='#E74C3C', **btn_style, command=self.remove_process).grid(row=0, column=3, padx=5, pady=5)

        # Resource controls
        tk.Label(self.controls_frame, text="Resource:", bg='#2C2F33', font=("Arial", 12), fg='white').grid(row=1, column=0, padx=5, pady=5)
        self.resource_entry = tk.Entry(self.controls_frame, width=15, font=("Arial", 12))
        self.resource_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.controls_frame, text="Add", bg='#7289DA', **btn_style, command=self.add_resource).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(self.controls_frame, text="Remove", bg='#E74C3C', **btn_style, command=self.remove_resource).grid(row=1, column=3, padx=5, pady=5)

        # Request edge controls
        tk.Label(self.controls_frame, text="Request Edge (P → R):", bg='#2C2F33', font=("Arial", 12), fg='white').grid(row=2, column=0, padx=5, pady=5)
        self.request_p_entry = tk.Entry(self.controls_frame, width=10, font=("Arial", 12))
        self.request_p_entry.grid(row=2, column=1, padx=5, pady=5)
        self.request_r_entry = tk.Entry(self.controls_frame, width=10, font=("Arial", 12))
        self.request_r_entry.grid(row=2, column=2, padx=5, pady=5)
        tk.Button(self.controls_frame, text="Add", bg='#7289DA', **btn_style, command=self.request_resource).grid(row=2, column=3, padx=5, pady=5)

        # Allocation edge controls
        tk.Label(self.controls_frame, text="Allocation Edge (R → P):", bg='#2C2F33', font=("Arial", 12), fg='white').grid(row=3, column=0, padx=5, pady=5)
        self.allocate_r_entry = tk.Entry(self.controls_frame, width=10, font=("Arial", 12))
        self.allocate_r_entry.grid(row=3, column=1, padx=5, pady=5)
        self.allocate_p_entry = tk.Entry(self.controls_frame, width=10, font=("Arial", 12))
        self.allocate_p_entry.grid(row=3, column=2, padx=5, pady=5)
        tk.Button(self.controls_frame, text="Add", bg='#7289DA', **btn_style, command=self.allocate_resource).grid(row=3, column=3, padx=5, pady=5)

        # Control buttons
        tk.Button(self.controls_frame, text="Clear Graph", bg='#F39C12', **btn_style, command=self.clear_graph).grid(row=4, column=1, columnspan=2, pady=10)
        tk.Button(self.controls_frame, text="Check Deadlock", bg='#E74C3C', **btn_style, command=self.check_deadlock).grid(row=5, column=1, columnspan=2, pady=10)

        self.draw_graph()

    def draw_graph(self):
        draw_graph(self.graph.get_graph(), self.ax, self.canvas)
    

    def add_process(self):
        process = self.process_entry.get().strip()
        self.graph.add_process(process)
        self.draw_graph()

    def remove_process(self):
        process = self.process_entry.get().strip()
        self.graph.remove_process(process)
        self.draw_graph()

    def add_resource(self):
        resource = self.resource_entry.get().strip()
        self.graph.add_resource(resource)
        self.draw_graph()

    def remove_resource(self):
        resource = self.resource_entry.get().strip()
        self.graph.remove_resource(resource)
        self.draw_graph()

    def request_resource(self):
        process = self.request_p_entry.get().strip()
        resource = self.request_r_entry.get().strip()
        self.graph.request_resource(process, resource)
        self.draw_graph()

    def allocate_resource(self):
        resource = self.allocate_r_entry.get().strip()
        process = self.allocate_p_entry.get().strip()
        self.graph.allocate_resource(resource, process)
        self.draw_graph()

    def clear_graph(self):
        self.graph.clear_graph()
        self.draw_graph()

    def check_deadlock(self):
        cycle = self.graph.check_deadlock()
        if cycle:
            messagebox.showwarning("Deadlock Detected", f"Deadlock found in cycle: {cycle}")
        else:
            messagebox.showinfo("No Deadlock", "The system is deadlock-free")

    