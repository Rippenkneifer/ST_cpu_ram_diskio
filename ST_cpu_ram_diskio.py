import threading as X, psutil as Y, tkinter as Z, time as Q;A, B, C, D, E, F, G = 160, 80, 10, 25, 0, 0, 0
def confusion():global E, F, G;H, I, J = Y.cpu_percent(None), Y.virtual_memory().percent, Y.disk_io_counters();K, L, M = J.read_time / 1000, J.write_time / 1000, Q.time();N = M - G or 1;O = ((K - E) + (L - F)) / N * 100;E, F, G = K, L, M;return H, I, O
def chaos():
    Y.cpu_percent(1)
    while 1:H, I, O = confusion();a.config(text=f"CPU: {H:.1f}%", fg="red" if H > 90 else "darkorange" if H > 75 else "green");b.config(text=f"RAM: {I:.1f}%", fg="red" if I > 90 else "darkorange" if I > 75 else "green");c.config(text=f"Disk I/O: {O:.1f}%", fg="red" if O > 90 else "darkorange" if O > 75 else "green");Q.sleep(1)
def zzz(e):global P, R;P, R = e.x, e.y
def confused_move(e):root.geometry(f"+{root.winfo_x()+(e.x-P)}+{root.winfo_y()+(e.y-R)}")
def resize_thingy(e):global A, B, C, D;A, B, C, D = (A + 20, B + 10, C + 1, D + 2) if e.state & 0x0004 and e.delta > 0 else (A - 20, B - 10, C - 1, D - 2);A, B, C, D = max(100, A), max(50, B), max(8, C), max(20, D);root.geometry(f"{A}x{B}");font_changer()
def font_changer():[thing.config(font=("Arial", C)) for thing in [a, b, c]];d.config(font=("Arial", C));d.place(x=A-D, y=0, width=D, height=D)
def GUI_of_confusion():global root, a, b, c, d;root = Z.Tk();root.geometry(f"{A}x{B}");root.overrideredirect(1);root.attributes("-topmost", 1, "-alpha", 0.6);a, b, c = [Z.Label(root, text=f"{X}: 0%", fg="green", bg="#BDBDFD", font=("Arial", C)) for X in ["CPU", "RAM", "Disk I/O"]];[thing.pack() for thing in [a, b, c]];d = Z.Button(root, text="X", command=root.quit, bg="red", fg="white", font=("Arial", C));d.place(x=A-D, y=0, width=D, height=D);root.bind("<Button-1>", zzz);root.bind("<B1-Motion>", confused_move);root.bind("<MouseWheel>", resize_thingy);root.mainloop()
X.Thread(target=GUI_of_confusion).start();X.Thread(target=chaos, daemon=1).start()