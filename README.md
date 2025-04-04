# Graphical Simulator for Resource Allocation Graph (RAG)

A Python-based graphical simulator to visualize Resource Allocation Graphs (RAG) and analyze deadlock scenarios. This tool provides an intuitive GUI using Tkinter to model the interaction between processes and resources.

## 🧠 Features

- Create and visualize Resource Allocation Graphs.
- Add and remove Processes and Resources.
- Create Request and Assignment edges.
- Detect deadlocks via graph cycle detection.
- Interactive GUI with visual feedback.
- Reset and rebuild the graph easily.

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- NetworkX (optional, for graph operations)
- Matplotlib (optional, for visualization)

## ⚙️ How It Works

- **Processes (P1, P2, …)** and **Resources (R1, R2, …)** are represented as nodes.
- Request Edges (P → R) indicate that a process is requesting a resource.
- Assignment Edges (R → P) indicate that a resource is assigned to a process.
- The simulator checks for cycles in the graph to detect deadlocks.

## 🧪 Example Scenario

1. Add Process `P1` and Resource `R1`.
2. Create a request edge from `P1` to `R1`.
3. Assign `R1` to `P2` instead.
4. If `P2` also requests `R1`, a deadlock is detected.
