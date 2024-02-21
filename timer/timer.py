from playsound import playsound
import tkinter as tk
import tkinter.ttk as ttk

count = 60
running = False

def reset():
    global count
    count = 60
    sec_label['text'] = 'Time Left: ' + str(count)
    window.update()

def start_counter():
    global running
    running = True
        
def counter(): 
    global count
    global running
    if running:
        count -= 1
        sec_label['text'] = 'Time Left: ' + str(count)
        window.update()
        if count == 0:
            playsound("C:/Users/timoo/OneDrive/Töölaud/timer/timer_alarm.mp3")
            reset()
            stop_counter()
    window.after(1000, counter)

def stop_counter():
    global running
    running = False


window = tk.Tk()
sec_label = tk.Label(text="Sec")
sec_entry = ttk.Entry(width=5)
min_label = tk.Label(text="Min")
min_entry = ttk.Entry(width=5)
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
sec_label.pack()
sec_entry.pack()
min_label.pack()
min_entry.pack()
start_button.pack()
stop_button.pack()
reset_button.pack()
seconds = sec_entry.get()
minutes = min_entry.get()
window.after(1000, counter)
window.mainloop()
