

---

## 📄 File Descriptions

### `graph.py`
- Contains the `ResourceAllocationGraph` class.
- Handles creation of nodes (processes/resources) and directed edges (requests/allocations).
- Includes logic to:
  - Add/remove processes and resources
  - Request and allocate resources
  - Detect cycles (deadlocks)
  - Clear the graph

---

### `graph_utils.py`
- Contains the `draw_graph` function.
- Responsible for visually rendering the graph using NetworkX and Matplotlib.
- Differentiates between:
  - **Request edges** (red, dashed)
  - **Allocation edges** (blue, solid)
- Uses spring layout for clear visualization.

---

### `ui.py`
- Handles the graphical user interface (GUI) built with Tkinter.
- Provides buttons and inputs to:
  - Add/remove processes/resources
  - Request/allocate resources
  - Clear graph
  - Check for deadlocks
- Integrates graph rendering using `Canvas` and Matplotlib.

---

### `main.py`
- Entry point of the application.
- Initializes the main GUI window.
- Connects the GUI logic (`ui.py`) with the graph logic (`graph.py` and `graph_utils.py`).

---

## 🚀 Features
- Add/remove processes and resources
- Request and allocate resources visually
- Detect and highlight deadlocks
- Real-time graph updates
- Color-coded edges for clarity

---

## 🛠 Requirements
- Python 3.x
- `networkx`
- `matplotlib`
- `tkinter` (comes built-in with most Python distributions)

Install dependencies:
```bash
pip install networkx matplotlib
