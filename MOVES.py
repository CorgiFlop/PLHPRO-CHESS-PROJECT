# Multi-frame tkinter application v2.3
import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="ΑΡΧΗ ΠΑΙΧΝΙΔΙΟΥ").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="ΚΙΝΗΣΗ 1",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="ΚΙΝΗΣΗ 2",
                  command=lambda: master.switch_frame(PageTwo)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="ΚΙΝΗΣΗ 1").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="ΜΕΤΑΒΑΣΗ ΣΤΗΝ ΑΡΧΗ",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="ΚΙΝΗΣΗ 2").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="ΜΕΤΑΒΑΣΗ ΣΤΗΝ ΑΡΧΗ",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
