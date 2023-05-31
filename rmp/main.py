import os
import threading
import tkinter as tk
from django.core.management import execute_from_command_line
from rmp import settings
from house.config import *


def run_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rmp.settings')
    execute_from_command_line(["manage.py", "runserver", "--noreload", "8080"])


def run_tkinter():
    root = tk.Tk()
    root.geometry("650x500")

    def update_threshold(*args):
        global low_threshold, high_threshold
        config_file_path = "D:/pythonProject/rmp/house/config.py"
        low_threshold = low_threshold_l.get()
        high_threshold = high_threshold_l.get()
        with open(config_file_path, 'r') as config_file:
            config_data = config_file.read()
            config_data = config_data.replace(f"LOWTHRESHOLD = {LOWTHRESHOLD}", f"LOWTHRESHOLD = {low_threshold}")
            config_data = config_data.replace(f"HIGHTHRESHOLD = {HIGHTHRESHOLD}",
                                              f"HIGHTHRESHOLD = {high_threshold}")
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_data)

    low_threshold_l = tk.Entry()
    high_threshold_l = tk.Entry()
    low_threshold_l.insert(0, str(LOWTHRESHOLD))
    high_threshold_l.insert(1, str(HIGHTHRESHOLD))
    btn1 = tk.Button(text="change_value", command=update_threshold)
    btn1.pack()
    low_threshold_l.pack()
    high_threshold_l.pack()
    low_threshold = 24.2
    high_threshold = 25.1

    root.mainloop()


if __name__ == "__main__":
    django_thread = threading.Thread(target=run_django)
    tkinter_thread = threading.Thread(target=run_tkinter, daemon=True)

    tkinter_thread.start()
    django_thread.start()

    tkinter_thread.join()
    django_thread.join()

