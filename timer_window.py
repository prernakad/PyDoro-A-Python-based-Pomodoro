"""
Pydoro HUD: A lightweight, always-on-top Tkinter window for the countdown timer.
"""
import tkinter as tk
class TimerHUD:
    def __init__(self):
        self.root = None
        self.seconds_left = 0
    def run_countdown(self, seconds, status_text):
        self.root = tk.Tk()
        self.root.title("Pydoro")
        self.root.geometry("260x140")
        self.root.attributes("-topmost", True) # Stays above other windows
        self.root.resizable(False, False)
        tk.Label(self.root, text=status_text, font=("Arial", 10), wraplength=240).pack(pady=10)
        lbl_timer = tk.Label(self.root, text="00:00", font=("Arial", 36, "bold"))
        lbl_timer.pack(pady=5)
        self.seconds_left = seconds
        def tick():
            if self.seconds_left < 0:
                self.root.destroy() # Close window when timer hits 0
                return
            mins, secs = divmod(self.seconds_left, 60)
            lbl_timer.config(text=f"{mins:02d}:{secs:02d}")
            self.seconds_left -= 1
            self.root.after(1000, tick) # Wait 1 second, then run tick() again
        tick()
        self.root.mainloop()