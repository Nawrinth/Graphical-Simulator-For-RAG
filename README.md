Graphical Simulator for Resource Allocation Graph (RAG)
A Python-based graphical simulator designed to visualize Resource Allocation Graphs (RAG) and analyze deadlock scenarios. This tool provides an intuitive GUI using Tkinter to help understand how processes and resources interact in a system and whether a deadlock has occurred.

🧠 Features
Create and visualize Resource Allocation Graphs.

Add and remove Processes and Resources.

Create Request and Assignment edges.

Visual feedback for possible Deadlock Detection.

Interactive GUI with drag-and-drop or button-based controls.

Option to reset and rebuild the graph.

🛠️ Technologies Used
Python 3

Tkinter for GUI

NetworkX (optional) for graph management and deadlock detection

Matplotlib (optional) for advanced visualization


⚙️ How It Works
Processes (P1, P2, …) and Resources (R1, R2, …) are represented as nodes.

Request Edges (P → R) indicate a process is requesting a resource.

Assignment Edges (R → P) show that a resource has been allocated to a process.

The simulator analyzes the graph to detect cycles, which may indicate deadlocks.

🧪 Example Scenario
Add Process P1 and Resource R1.

Add a request edge from P1 to R1.

Assign R1 to another process P2.

If P2 also requests R1, the simulator will detect a deadlock.
