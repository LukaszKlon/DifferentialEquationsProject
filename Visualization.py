import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

from solve_part import solver

class App:
    def __init__(self):
        self.root = tk.Tk()

        self.root.minsize(300, 200)
        self.root.maxsize(600, 400)

        self.label = tk.Label(self.root, text="Acoustic vibrations of the material layer", font=('Helvetica', 18))
        self.label.pack(padx=20, pady=40)

        self.label = tk.Label(self.root, text="Elements number:")
        self.label.pack(side='left',padx=10)

        self.entry = tk.Entry(self.root, justify='center')
        self.entry.pack(side='left',padx=10)

        self.button = tk.Button(self.root, justify='center', text="confirm", height=1, width=8, command=self.solve)
        self.button.pack(side = 'left',padx=10)

        self.root.mainloop()

    def show(self,x,y,n):
        plt.style.use('Solarize_Light2')
        ax = plt.subplot()
        ax.set(title='Acoustic vibrations of the material layer', xlabel='n = ' + str(n))
        ax.plot(x, y, color='blue')

        plt.show()
    def solve(self):
        n = int(self.entry.get())
        Q = solver(n)
        x, y = Q.solve()
        print(y)
        if n <= 2:
            messagebox.showinfo(title="info",message="The result isn't precise ")
        self.show(x, y, n)
    
App()