#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser, Menu, Spinbox, scrolledtext, messagebox as mb, filedialog as fd

import webbrowser

checked = []

class Check:
    """create checkbuttons for links."""
    def __init__(self, parent, site):
        self.var = tk.IntVar()
        self.site = site

        self = ttk.Checkbutton(parent, text=self.site, variable=self.var, command=self.check)
        self.pack(anchor=tk.W, padx=5, pady=5)

    def check(self):
        v = self.var.get() # 1 checked 0 unchecked
        if v:
            checked.append(self.site)
        else:
            if self.site in checked:
                checked.remove(self.site)

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""
    #===========================================
    def __init__(self, title, icon, theme, sites):
        super().__init__()
        self.style = ttk.Style(self)
        self.resizable(False, False)
        self.title(title)
        self.iconbitmap(icon)
        self.style.theme_use(theme)
        self.sites = sites
        self.c = []

        self.init_UI()

    # INITIALIZER ==============================
    @classmethod
    def create_app(cls, app):
        return cls(app['title'], app['icon'], app['theme'], app['sites'])

    #===========================================
    def init_UI(self):
        self.main = ttk.Frame(self)
        self.main.pack(fill=tk.BOTH, expand=True)

        for site in self.sites:
            self.c.append(Check(self.main, site))

        self.button = ttk.Button(self.main, text='Launch', command=self.start)
        self.button.pack(side=tk.TOP, fill=tk.X, anchor=tk.W, padx=10, pady=10)

    # METHODS -----------------------------------
    def start(self):
        # firefox = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        # w = webbrowser.get(firefox)
        for checked_site in checked:
            webbrowser.open(checked_site)

#===========================
# Start GUI
#===========================

def main(config):
    app = App.create_app(config)
    app.mainloop()

if __name__ == '__main__':
    main({
        'title' : 'Open Browser Version 1.0',
        'icon' : 'python.ico',
        'theme' : 'clam',
        'sites' : [
            'https://github.com/mercado-joshua',
            'https://mercado-joshua.github.io/'
            ]
        })