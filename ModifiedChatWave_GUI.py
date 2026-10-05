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

FONT = "Segoe UI"


# ---------- Demo Database ----------
USERS = {
    "alex123": "password123"
}


# ---------- Input Field ----------
class Field(tk.Frame):

    def __init__(self, parent, label, secret=False):
        super().__init__(parent, bg=CARD)

        tk.Label(
            self,
            text=label,
            bg=CARD,
            fg=MUTED,
            font=(FONT, 9)
        ).pack(anchor="w", pady=(0, 4))

        self.entry = tk.Entry(
            self,
            relief="flat",
            bd=0,
            bg=FIELD_BG,
            fg=TEXT,
            insertbackground=TEXT,
            font=(FONT, 10),
            show="*" if secret else ""
        )

        self.entry.pack(
            fill="x",
            ipady=10
        )

    def get(self):
        return self.entry.get()


# ---------- Main App ----------
class QuickChat(tk.Tk):

    W = 400
    H = 650

    def __init__(self):
        super().__init__()

        self.title("QuickChat")
        self.configure(bg=BG)
        self.resizable(False, False)

        x = (self.winfo_screenwidth() - self.W) // 2
        y = (self.winfo_screenheight() - self.H) // 2

        self.geometry(
            f"{self.W}x{self.H}+{x}+{max(y, 0)}"
        )

        self.on_submit = lambda: None

        self.bind(
            "<Return>",
            lambda e: self.on_submit()
        )

        self.load_logo()
        self.show_login()

    # ---------- Logo ----------
    def load_logo(self):

        try:
            self.logo_image = tk.PhotoImage(
                file="quickchat_logo.png"
            )

            # Resize logo if it is too large
            width = self.logo_image.width()
            height = self.logo_image.height()

            if width > 130 or height > 100:
                self.logo_image = self.logo_image.subsample(
                    max(1, width // 120),
                    max(1, height // 90)
                )

            tk.Label(
                self,
                image=self.logo_image,
                bg=BG
            ).pack(pady=(30, 5))

        except Exception:
            # If logo file is missing
            tk.Label(
                self,
                text="QuickChat",
                bg=BG,
                fg="#00d084",
                font=(FONT, 24, "bold")
            ).pack(pady=(45, 20))

    # ---------- Clear Window ----------
    def clear_window(self):

        for widget in self.winfo_children():
            widget.destroy()

    # ---------- Header ----------
    def header(self, title, subtitle):

        tk.Label(
            self,
            text=title,
            bg=BG,
            fg=TEXT,
            font=(FONT, 18, "bold")
        ).pack(pady=(15, 5))

        tk.Label(
            self,
            text=subtitle,
            bg=BG,
            fg=MUTED,
            font=(FONT, 9)
        ).pack(pady=(0, 20))

    # ---------- Login ----------
    def show_login(self):

        self.clear_window()

        self.load_logo()

        self.header(
            "Welcome Back",
            "Log in to continue"
        )

        self.card = tk.Frame(
            self,
            bg=CARD,
            padx=30,
            pady=25
        )

        self.card.pack(
            padx=40,
            fill="x"
        )

        self.user = Field(
            self.card,
            "Username"
        )

        self.user.pack(
            fill="x",
            pady=(0, 15)
        )

        self.pw = Field(
            self.card,
            "Password",
            secret=True
        )

        self.pw.pack(
            fill="x",
            pady=(0, 10)
        )

        self.msg = tk.Label(
            self.card,
            text="",
            bg=CARD,
            fg=ERROR,
            font=(FONT, 9)
        )

        self.msg.pack(pady=5)

        self.login_btn = tk.Button(
            self.card,
            text="Log In",
            command=self.do_login,
            bg=PRIMARY,
            fg=PRIMARY_TEXT,
            activebackground="#dddddd",
            activeforeground="#000000",
            relief="flat",
            bd=0,
            font=(FONT, 10, "bold"),
            cursor="hand2"
        )

        self.login_btn.pack(
            fill="x",
            ipady=8,
            pady=(5, 20)
        )

        bottom = tk.Frame(
            self.card,
            bg=CARD
        )

        bottom.pack()

        tk.Label(
            bottom,
            text="Don't have an account?",
            bg=CARD,
            fg=MUTED,
            font=(FONT, 9)
        ).pack(side="left")

        signup = tk.Label(
            bottom,
            text=" Sign Up",
            bg=CARD,
            fg="#00d084",
            font=(FONT, 9, "bold"),
            cursor="hand2"
        )

        signup.pack(side="left")

        signup.bind(
            "<Button-1>",
            lambda e: self.show_signup()
        )

        self.on_submit = self.do_login

        self.user.entry.focus_set()

    # ---------- Login ----------
    def do_login(self):

        username = self.user.get().strip()
        password = self.pw.get()

        if not username or not password:

            self.msg.config(
                text="Please enter your username and password.",
                fg=ERROR
            )

            return

        if USERS.get(username) == password:

            self.msg.config(
                text=f"Welcome back, {username}!",
                fg=SUCCESS
            )

        else:

            self.msg.config(
                text="Incorrect username or password.",
                fg=ERROR
            )

    # ---------- Sign Up ----------
    def show_signup(self):

        self.clear_window()

        self.load_logo()

        self.header(
            "Create Account",
            "Create your QuickChat account"
        )

        self.card = tk.Frame(
            self,
            bg=CARD,
            padx=30,
            pady=25
        )

        self.card.pack(
            padx=40,
            fill="x"
        )

        self.user = Field(
            self.card,
            "Username"
        )

        self.user.pack(
            fill="x",
            pady=(0, 15)
        )

        self.pw = Field(
            self.card,
            "Password",
            secret=True
        )

        self.pw.pack(
            fill="x",
            pady=(0, 15)
        )

        self.pw2 = Field(
            self.card,
            "Confirm Password",
            secret=True
        )

        self.pw2.pack(
            fill="x",
            pady=(0, 10)
        )

        self.msg = tk.Label(
            self.card,
            text="",
            bg=CARD,
            fg=ERROR,
            font=(FONT, 9)
        )

        self.msg.pack(pady=5)

        signup_btn = tk.Button(
            self.card,
            text="Sign Up",
            command=self.do_signup,
            bg=PRIMARY,
            fg=PRIMARY_TEXT,
            activebackground="#dddddd",
            activeforeground="#000000",
            relief="flat",
            bd=0,
            font=(FONT, 10, "bold"),
            cursor="hand2"
        )

        signup_btn.pack(
            fill="x",
            ipady=8,
            pady=(5, 20)
        )

        bottom = tk.Frame(
            self.card,
            bg=CARD
        )

        bottom.pack()

        tk.Label(
            bottom,
            text="Already have an account?",
            bg=CARD,
            fg=MUTED,
            font=(FONT, 9)
        ).pack(side="left")

        login = tk.Label(
            bottom,
            text=" Log In",
            bg=CARD,
            fg="#00d084",
            font=(FONT, 9, "bold"),
            cursor="hand2"
        )

        login.pack(side="left")

        login.bind(
            "<Button-1>",
            lambda e: self.show_login()
        )

        self.on_submit = self.do_signup

        self.user.entry.focus_set()

    # ---------- Sign Up ----------
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

            self.msg.config(
                text="Account created! You can now log in.",
                fg=SUCCESS
            )

            self.after(
                1000,
                self.show_login
            )

            return

        self.msg.config(
            text=error,
            fg=ERROR
        )


# ---------- Run ----------
if __name__ == "__main__":
    QuickChat().mainloop()