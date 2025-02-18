import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu

class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target

    def bfs(self):
        from collections import deque

        visited = set()
        queue = deque([(0, 0)])  # Start with both jugs empty
        steps = []

        while queue:
            jug1, jug2 = queue.popleft()
            steps.append((jug1, jug2))

            if jug1 == self.target or jug2 == self.target:
                return steps

            if (jug1, jug2) in visited:
                continue
            visited.add((jug1, jug2))

            # Possible actions
            actions = [
                (self.jug1_capacity, jug2),  # Fill Jug 1
                (jug1, self.jug2_capacity),  # Fill Jug 2
                (0, jug2),                    # Empty Jug 1
                (jug1, 0),                    # Empty Jug 2
                (max(0, jug1 - (self.jug2_capacity - jug2)), min(self.jug2_capacity, jug1 + jug2)),  # Pour Jug 1 to Jug 2
                (min(self.jug1_capacity, jug1 + jug2), max(0, jug2 - (self.jug1_capacity - jug1)))   # Pour Jug 2 to Jug 1
            ]

            for action in actions:
                if action not in visited:
                    queue.append(action)

        return steps

    def dfs(self):
        visited = set()
        stack = [(0, 0)]  # Start with both jugs empty
        steps = []

        while stack:
            jug1, jug2 = stack.pop()
            steps.append((jug1, jug2))

            if jug1 == self.target or jug2 == self.target:
                return steps

            if (jug1, jug2) in visited:
                continue
            visited.add((jug1, jug2))

            # Possible actions
            actions = [
                (self.jug1_capacity, jug2),  # Fill Jug 1
                (jug1, self.jug2_capacity),  # Fill Jug 2
                (0, jug2),                    # Empty Jug 1
                (jug1, 0),                    # Empty Jug 2
                (max(0, jug1 - (self.jug2_capacity - jug2)), min(self.jug2_capacity, jug1 + jug2)),  # Pour Jug 1 to Jug 2
                (min(self.jug1_capacity, jug1 + jug2), max(0, jug2 - (self.jug1_capacity - jug1)))   # Pour Jug 2 to Jug 1
            ]

            for action in actions:
                if action not in visited:
                    stack.append(action)

        return steps

class WaterJugGUI:
    def __init__(self, master):
        self.master = master
        master.title("Water Jug Problem")

        self.jug1_capacity_label = tk.Label(master, text="Jug 1 Capacity:")
        self.jug1_capacity_label.pack()
        self.jug1_capacity_entry = tk.Entry(master)
        self.jug1_capacity_entry.pack()

        self.jug2_capacity_label = tk.Label(master, text="Jug 2 Capacity:")
        self.jug2_capacity_label.pack()
        self.jug2_capacity_entry = tk.Entry(master)
        self.jug2_capacity_entry.pack()

        self.target_label = tk.Label(master, text="Target Amount:")
        self.target_label.pack()
        self.target_entry = tk.Entry(master)
        self.target_entry.pack()

        self.algorithm_label = tk.Label(master, text="Select Algorithm:")
        self.algorithm_label.pack()
        self.algorithm_var = StringVar(master)
        self.algorithm_var.set("BFS")  # Default value
        self.algorithm_menu = OptionMenu(master, self.algorithm_var, "BFS", "DFS")
        self.algorithm_menu.pack()

        self.solve_button = tk.Button(master, text="Solve", command=self.solve)
        self.solve_button.pack()

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack()

    def solve(self):
        try:
            jug1_capacity = int(self.jug1_capacity_entry.get())
            jug2_capacity = int(self.jug2_capacity_entry.get())
            target = int(self.target_entry.get())

            if target > max(jug1_capacity, jug2_capacity):
                messagebox.showerror("Error", "Target amount exceeds jug capacities.")
                return

            problem = WaterJugProblem(jug1_capacity, jug2_capacity, target)

            # Select the algorithm based on user input
            if self.algorithm_var.get() == "BFS":
                steps = problem.bfs()
            else:  # DFS
                steps = problem.dfs()

            self.result_text.delete(1.0, tk.END)
            for step in steps:
                self.result_text.insert(tk.END, f"Jug 1: {step[0]}, Jug 2: {step[1]}\n")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = WaterJugGUI(root)
    root.mainloop()
