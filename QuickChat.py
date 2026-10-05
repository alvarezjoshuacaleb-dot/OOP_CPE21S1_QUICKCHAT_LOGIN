import tkinter as tk

# ---------- Theme ----------
BG = "#000000"
CARD = "#111111"
FIELD_BG = "#1c1c1c"
TEXT = "#ffffff"
MUTED = "#999999"
PRIMARY = "#ffffff"
PRIMARY_TEXT = "#000000"
ERROR = "#ff5555"
SUCCESS = "#55cc55"
ACCENT = "#00d084"
BORDER = "#222222"

FONT = "Segoe UI"

# QuickChat icon (embedded, no image file needed)
ICON_B64 = (
    "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"
)

# ---------- Demo Database ----------
USERS = {"alex123": "password123"}


# ---------- Input Field ----------
class Field(tk.Frame):
    def __init__(self, parent, label, secret=False):
        super().__init__(parent, bg=CARD)

        tk.Label(self, text=label, bg=CARD, fg=MUTED,
                 font=(FONT, 9)).pack(anchor="w", pady=(0, 4))

        self.entry = tk.Entry(
            self, relief="flat", bd=0, bg=FIELD_BG, fg=TEXT,
            insertbackground=TEXT, font=(FONT, 10),
            show="*" if secret else ""
        )
        self.entry.pack(fill="x", ipady=10)

    def get(self):
        return self.entry.get()


# ---------- Main App ----------
class QuickChat(tk.Tk):
    W = 400
    H = 720

    def __init__(self):
        super().__init__()

        self.title("QuickChat")
        self.configure(bg=BORDER)

        # Remove the default white Windows title bar
        self.overrideredirect(True)

        x = (self.winfo_screenwidth() - self.W) // 2
        y = (self.winfo_screenheight() - self.H) // 2
        self.geometry(f"{self.W}x{self.H}+{x}+{max(y, 0)}")

        self.on_submit = lambda: None
        self.bind("<Return>", lambda e: self.on_submit())
        self.bind("<Escape>", lambda e: self.destroy())

        self._drag_x = 0
        self._drag_y = 0
        self._minimized = False

        # 1px border around the whole window
        self.shell = tk.Frame(self, bg=BG)
        self.shell.pack(fill="both", expand=True, padx=1, pady=1)

        self.build_titlebar()

        # Everything that changes (login/signup) lives in the body
        self.body = tk.Frame(self.shell, bg=BG)
        self.body.pack(fill="both", expand=True)

        self.logo_image = self.load_logo_image()

        self.show_login()

        # Keep taskbar icon + restore after minimize
        self.after(100, self.enable_taskbar_icon)
        self.bind("<Map>", self.on_restore)

    # ---------- Custom Title Bar (black, inside the app) ----------
    def build_titlebar(self):
        bar = tk.Frame(self.shell, bg=BG, height=36)
        bar.pack(fill="x")
        bar.pack_propagate(False)

        title = tk.Label(bar, text="  QuickChat", bg=BG, fg=MUTED,
                         font=(FONT, 9))
        title.pack(side="left")

        close = self.title_button(bar, "✕", self.destroy, hover="#e81123")
        close.pack(side="right", fill="y")

        mini = self.title_button(bar, "—", self.minimize, hover="#2a2a2a")
        mini.pack(side="right", fill="y")

        # Drag the window by the bar
        for w in (bar, title):
            w.bind("<ButtonPress-1>", self.start_move)
            w.bind("<B1-Motion>", self.do_move)

        tk.Frame(self.shell, bg=BORDER, height=1).pack(fill="x")

    def title_button(self, parent, text, command, hover):
        btn = tk.Label(parent, text=text, bg=BG, fg=TEXT,
                       font=(FONT, 10), width=5, cursor="hand2")
        btn.bind("<Button-1>", lambda e: command())
        btn.bind("<Enter>", lambda e: btn.config(bg=hover))
        btn.bind("<Leave>", lambda e: btn.config(bg=BG))
        return btn

    def start_move(self, event):
        self._drag_x = event.x_root - self.winfo_x()
        self._drag_y = event.y_root - self.winfo_y()

    def do_move(self, event):
        self.geometry(f"+{event.x_root - self._drag_x}+{event.y_root - self._drag_y}")

    # ---------- Minimize support for borderless window ----------
    def minimize(self):
        self._minimized = True
        self.overrideredirect(False)
        self.iconify()

    def on_restore(self, event):
        # Only react when the window comes back from being minimized
        if event.widget is self and self._minimized and self.state() == "normal":
            self._minimized = False
            self.after(10, lambda: self.overrideredirect(True))

    def enable_taskbar_icon(self):
        # Windows only: show the app in the taskbar even without a title bar
        try:
            import ctypes
            GWL_EXSTYLE = -20
            WS_EX_APPWINDOW = 0x00040000
            WS_EX_TOOLWINDOW = 0x00000080
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            style = (style & ~WS_EX_TOOLWINDOW) | WS_EX_APPWINDOW
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
        except Exception:
            pass

    # ---------- Logo ----------
    def load_logo_image(self):
        try:
            return tk.PhotoImage(data=ICON_B64)
        except Exception:
            return None

    def add_logo(self):
        holder = tk.Frame(self.body, bg=BG)
        holder.pack(pady=(14, 0))

        if self.logo_image:
            tk.Label(holder, image=self.logo_image, bg=BG).pack()

        # Wordmark: "Quick" in white + "Chat" in green
        word = tk.Frame(holder, bg=BG)
        word.pack(pady=(0, 0))
        tk.Label(word, text="Quick", bg=BG, fg=TEXT, padx=0, bd=0,
                 font=(FONT, 22, "bold")).pack(side="left")
        tk.Label(word, text="Chat", bg=BG, fg=ACCENT, padx=0, bd=0,
                 font=(FONT, 22, "bold")).pack(side="left")

    # ---------- Helpers ----------
    def clear_window(self):
        for widget in self.body.winfo_children():
            widget.destroy()

    def header(self, title, subtitle):
        tk.Label(self.body, text=title, bg=BG, fg=TEXT,
                 font=(FONT, 18, "bold")).pack(pady=(10, 5))
        tk.Label(self.body, text=subtitle, bg=BG, fg=MUTED,
                 font=(FONT, 9)).pack(pady=(0, 20))

    def make_card(self):
        card = tk.Frame(self.body, bg=CARD, padx=30, pady=25)
        card.pack(padx=40, fill="x")
        return card

    def make_button(self, parent, text, command):
        btn = tk.Button(
            parent, text=text, command=command, bg=PRIMARY,
            fg=PRIMARY_TEXT, activebackground="#dddddd",
            activeforeground="#000000", relief="flat", bd=0,
            font=(FONT, 10, "bold"), cursor="hand2"
        )
        btn.pack(fill="x", ipady=8, pady=(5, 20))
        return btn

    def switch_link(self, parent, text, link_text, command):
        row = tk.Frame(parent, bg=CARD)
        row.pack()
        tk.Label(row, text=text, bg=CARD, fg=MUTED,
                 font=(FONT, 9)).pack(side="left")
        link = tk.Label(row, text=" " + link_text, bg=CARD, fg=ACCENT,
                        font=(FONT, 9, "bold"), cursor="hand2")
        link.pack(side="left")
        link.bind("<Button-1>", lambda e: command())

    # ---------- Login Screen ----------
    def show_login(self):
        self.clear_window()
        self.add_logo()
        self.header("Welcome Back", "Log in to continue")

        card = self.make_card()

        self.user = Field(card, "Username")
        self.user.pack(fill="x", pady=(0, 15))

        self.pw = Field(card, "Password", secret=True)
        self.pw.pack(fill="x", pady=(0, 10))

        self.msg = tk.Label(card, text="", bg=CARD, fg=ERROR,
                            font=(FONT, 9), wraplength=280)
        self.msg.pack(pady=5)

        self.make_button(card, "Log In", self.do_login)
        self.switch_link(card, "Don't have an account?", "Sign Up",
                         self.show_signup)

        self.on_submit = self.do_login
        self.user.entry.focus_set()

    def do_login(self):
        username = self.user.get().strip()
        password = self.pw.get()

        if not username or not password:
            self.msg.config(text="Please enter your username and password.",
                            fg=ERROR)
            return

        if USERS.get(username) == password:
            self.msg.config(text=f"Welcome back, {username}!", fg=SUCCESS)
        else:
            self.msg.config(text="Incorrect username or password.", fg=ERROR)

    # ---------- Sign Up Screen ----------
    def show_signup(self):
        self.clear_window()
        self.add_logo()
        self.header("Create Account", "Create your QuickChat account")

        card = self.make_card()

        self.user = Field(card, "Username")
        self.user.pack(fill="x", pady=(0, 15))

        self.pw = Field(card, "Password", secret=True)
        self.pw.pack(fill="x", pady=(0, 15))

        self.pw2 = Field(card, "Confirm Password", secret=True)
        self.pw2.pack(fill="x", pady=(0, 10))

        self.msg = tk.Label(card, text="", bg=CARD, fg=ERROR,
                            font=(FONT, 9), wraplength=280)
        self.msg.pack(pady=5)

        self.make_button(card, "Sign Up", self.do_signup)
        self.switch_link(card, "Already have an account?", "Log In",
                         self.show_login)

        self.on_submit = self.do_signup
        self.user.entry.focus_set()

    def do_signup(self):
        username = self.user.get().strip()
        password = self.pw.get()
        confirm = self.pw2.get()

        if len(username) < 3:
            error = "Username must be at least 3 characters."
        elif username in USERS:
            error = "That username is already taken."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        elif password != confirm:
            error = "Passwords don't match."
        else:
            USERS[username] = password
            self.msg.config(text="Account created! You can now log in.",
                            fg=SUCCESS)
            self.on_submit = lambda: None
            self.after(1000, self.show_login)
            return

        self.msg.config(text=error, fg=ERROR)


# ---------- Run ----------
if __name__ == "__main__":
    QuickChat().mainloop()
