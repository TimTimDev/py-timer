from playsound import playsound
import tkinter as tk
import tkinter.ttk as ttk


running = False

def get_count():
    global count
    seconds = sec_entry.get()
    minutes = min_entry.get()
    count = int(minutes) * 60 + int(seconds)

def start_counter():
    global running
    running = True
    get_count()

def reset():
    global count
    get_count()
    show_time['text'] = 'Time Left: ' + str(count)
    window.update()

def stop_counter():
    global running
    running = False
        
def counter(): 
    global count
    global running
    if running:
        count -= 1
        show_time['text'] = 'Time Left: ' + str(count)
        window.update()
        if count <= 0:
            playsound("C:/Users/timoo/OneDrive/Töölaud/timer/timer_alarm.mp3")
            reset()
            stop_counter()
    window.after(1000, counter)


window = tk.Tk()
window.title("Timer")
window.geometry("300x200")

window.columnconfigure([0, 1, 2, 3, 4, 5], minsize=50, pad=5)
window.rowconfigure([0, 1, 2, 3], minsize=50, pad=5)

sec_label = tk.Label(text="Sec")
sec_entry = ttk.Entry(width=5)
sec_entry.insert(0, 0)
sec_label.grid(row=0, column=3, columnspan=2)
sec_entry.grid(row=1, column=3, columnspan=2)

min_label = tk.Label(text="Min")
min_entry = ttk.Entry(width=5)
min_entry.insert(0, 0)
min_label.grid(row=0, column=1, columnspan=2)
min_entry.grid(row=1, column=1, columnspan=2)

show_time = tk.Label(text="Time Left: ")
show_time.grid(row=2, column=2, columnspan=2)

start_button = ttk.Button(
    text="Start",
    width=10,
    command=start_counter
)
stop_button = ttk.Button(
    text="Stop",
    width=10, 
    command=stop_counter
)
reset_button = ttk.Button(
    text="Reset",
    width=10, 
    command=reset
)


start_button.grid(row=3, column=0, columnspan=2)
stop_button.grid(row=3, column=2, columnspan=2)
reset_button.grid(row=3, column=4, columnspan=2)

window.after(1000, counter)
window.mainloop()
