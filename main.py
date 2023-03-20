import tkinter as tk
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

class CreditCheckerGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Credit Checker")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Enter k value:").grid(row=0, column=0)
        self.k_entry = tk.Entry(self.master)
        self.k_entry.grid(row=0, column=1)
        tk.Label(self.master, text="Enter sex (0 for female, 1 for male):").grid(row=1, column=0)
        self.sex_entry = tk.Entry(self.master)
        self.sex_entry.grid(row=1, column=1)
        tk.Label(self.master, text="Enter age (years old):").grid(row=2, column=0)
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=2, column=1)
        tk.Label(self.master, text="Enter salary (baht):").grid(row=3, column=0)
        self.salary_entry = tk.Entry(self.master)
        self.salary_entry.grid(row=3, column=1)
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_credit)
        self.submit_button.grid(row=4, column=0, columnspan=2)

    def check_credit(self):
        X = pd.DataFrame({
            'age': [27, 51, 52, 33, 45],
            'sex': [0, 1, 1, 0, 1],
            'salary': [19000, 64000, 105000, 55000, 45000],
        })
        y = pd.Series(['F', 'T', 'T', 'T', 'F'])
        knn = KNeighborsClassifier(n_neighbors=int(self.k_entry.get()))
        knn.fit(X, y)
        test_data = pd.DataFrame({
            'age': [int(self.age_entry.get())],
            'sex':[int(self.sex_entry.get())],
            'salary': [int(self.salary_entry.get())]
        })
        prediction = knn.predict(test_data)
        result_str = f"The credit is: {prediction[0]}"
        self.result_label = tk.Label(self.master, text=result_str)
        self.result_label.grid(row=5, column=0, columnspan=2)

root = tk.Tk()
app = CreditCheckerGUI(master=root)
app.mainloop()

