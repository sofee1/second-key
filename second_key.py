import tkinter as tk
from datetime import datetime

LOG_FILE = "keylog.txt"

# أسماء المفاتيح الخاصة بالعربي
KEY_NAMES = [
    "space",
    "BackSpace",
    "Return",
    "Tab",
    "Escape",
    "Delete",
    "Up",
    "Down",
    "Left",
    "Right",
    "Shift_L",
    "Shift_R",
    "Control_L",
    "Control_R",
    "Alt_L",
    "Alt_R",
    "caps_lock",
    "Home",
    "End",
    "Prior",
    "Next",
    "Insert",
]

def record_key(event):
    char = event.char
    keysym = event.keysym
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # تحديد الاسم المعروض
    if keysym in KEY_NAMES:
        display = f"[{keysym}]"
    elif char and char.isprintable():
        display = char  # حرف عادي أو عربي
    else:
        display = f"[{keysym}]"  # أي مفتاح آخر

    entry = f"[{timestamp}]  {display}"

    log.insert(tk.END, entry)
    log.see(tk.END)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

# ── الواجهة ──────────────────────────────────────────
window = tk.Tk()
window.title("Key Logger - Educational Demo")
window.geometry("520x480")

tk.Label(
    window,
    text="key logger",
    font=("Arial", 14)
).pack(pady=10)

text_box = tk.Entry(window, width=50, font=("Arial", 14))
text_box.pack(pady=10)
text_box.focus()

log = tk.Listbox(window, width=65, height=16, font=("Courier", 10))
log.pack(pady=10)

tk.Label(
    window,
    text=f" saved in: {LOG_FILE}",
    font=("Arial", 10),
    fg="gray"
).pack()

text_box.bind("<KeyPress>", record_key)

window.mainloop()