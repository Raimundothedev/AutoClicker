import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from config import *
import clicker
import webbrowser

ctk.set_appearance_mode(Config.THEME)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"Auto Clicker | {Config.VERSION}")
        self.geometry(f"{Config.WIDTH}x{Config.HEIGHT}")
        self.resizable(False, False)

        self.create_widgets()

        self.update_button()

    #======================
    # Create Widgets
    #======================

    def create_widgets(self):
        self.build_header()
        self.build_main()


    #=======================
    # Header
    #=======================

    def build_header(self):

        # Header frame
        self.header_frame = ctk.CTkFrame(
            self,
            height=50
        )
        self.header_frame.pack(side="top", fill="x")
        self.header_frame.pack_propagate(False)

        # Title
        title = ctk.CTkLabel(
            self.header_frame,
            text="Auto Clicker",
            font=ctk.CTkFont(size=26, weight="bold", family="Segoe UI")
        )
        title.pack(side="left", padx=50)

        github = ctk.CTkButton(
            self.header_frame,
            text=f"{Config.GITHUB}",
            fg_color="transparent",
            hover=False,
            text_color=("blue", "lightblue"),
            command=lambda: webbrowser.open("https://github.com/Raimundothedev/FileOrganizer")
        )
        github.pack(side="right", pady=(20, 0))


    #=======================
    # Main tab
    #=======================

    def build_main(self):

        # Main frame
        self.main_frame = ctk.CTkFrame(
            self,
            corner_radius=18
        )
        self.main_frame.pack(
            padx=50,
            pady=50,
            fill="both",
            expand=True
        )
        self.main_frame.pack_propagate(False)

        #=======================
        # Click interval
        #=======================

        # Variáveis dos Entries
        self.hours = ctk.StringVar(value="0")
        self.minutes = ctk.StringVar(value="0")
        self.seconds = ctk.StringVar(value="0")
        self.milliseconds = ctk.StringVar(value="0")

        # Atualiza o intervalo quando qualquer Entry mudar
        self.hours.trace_add("write", lambda *args: self.update_interval())
        self.minutes.trace_add("write", lambda *args: self.update_interval())
        self.seconds.trace_add("write", lambda *args: self.update_interval())
        self.milliseconds.trace_add("write", lambda *args: self.update_interval())

        # Entries
        self.hours_entry = ctk.CTkEntry(self, textvariable=self.hours)
        self.minutes_entry = ctk.CTkEntry(self, textvariable=self.minutes)
        self.seconds_entry = ctk.CTkEntry(self, textvariable=self.seconds)
        self.milliseconds_entry = ctk.CTkEntry(self, textvariable=self.milliseconds)

        self.interval_frame = ctk.CTkFrame(
            self.main_frame,
            height=80
        )
        self.interval_frame.pack(
            padx=20,
            pady=(20, 0),
            fill="x"
        )
        self.interval_frame.pack_propagate(False)

        interval_title = ctk.CTkLabel(
            self.interval_frame,
            text="Click interval",
            font=ctk.CTkFont(size=16, weight="bold", family="Segoe UI")
        )
        interval_title.pack(
            side="top",
            anchor="w",
            padx=10,
            pady=(8, 5)
        )

        # Hours
        self.hours_entry = ctk.CTkEntry(
            self.interval_frame,
            width=60,
            textvariable=self.hours
        )
        self.hours_entry.pack(side="left", padx=(10, 5))

        ctk.CTkLabel(
            self.interval_frame,
            text="hours",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14
            )
        ).pack(side="left", padx=(0, 15))


        # Minutes
        self.minutes_entry = ctk.CTkEntry(
            self.interval_frame,
            width=60,
            textvariable=self.minutes
        )
        self.minutes_entry.pack(side="left", padx=(0, 5))

        ctk.CTkLabel(
            self.interval_frame,
            text="mins",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14
            )
        ).pack(side="left", padx=(0, 15))


        # Seconds
        self.seconds_entry = ctk.CTkEntry(
            self.interval_frame,
            width=60,
            textvariable=self.seconds
        )
        self.seconds_entry.pack(side="left", padx=(0, 5))

        ctk.CTkLabel(
            self.interval_frame,
            text="secs",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14
            )
        ).pack(side="left", padx=(0, 15))


        # Milliseconds
        self.milliseconds_entry = ctk.CTkEntry(
            self.interval_frame,
            width=60,
            textvariable=self.milliseconds
        )
        self.milliseconds_entry.insert(0, "100")
        self.milliseconds_entry.pack(side="left", padx=(0, 5))

        ctk.CTkLabel(
            self.interval_frame,
            text="milliseconds",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14
            )
        ).pack(side="left")

        #=======================
        # Click Options
        #=======================
        
        # Frame
        self.options_frame = ctk.CTkFrame(
            self.main_frame,
            height=80
        )
        self.options_frame.pack(
            padx=20,
            pady=(10, 0),
            fill="x"
        )
        self.options_frame.pack_propagate(False)

        options_title = ctk.CTkLabel(
            self.options_frame,
            text="Click options",
            font=ctk.CTkFont(size=16, weight="bold", family="Segoe UI")
        )
        options_title.pack(
            side="top",
            anchor="w",
            padx=10,
            pady=(8, 5)
        )


        # Mouse option

        ctk.CTkLabel(
            self.options_frame,
            text="Mouse button:",
            font=ctk.CTkFont(size=16, family="Segoe UI")
        ).pack(side="left", padx=10)
        

        self.mouse_option = ctk.CTkOptionMenu(
            self.options_frame,
            values=[
                "Left",
                "Right",
                "Middle"
            ],
            width=100,
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14
            ),
            command=self.get_button_type
        )
        self.mouse_option.pack(side="left", padx=10)
        self.mouse_option.set("Left")

        ctk.CTkLabel(
            self.options_frame,
            text="Click type:",
            font=ctk.CTkFont(size=16, family="Segoe UI")
        ).pack(side="left", padx=10)

        self.click_type = ctk.CTkOptionMenu(
            self.options_frame,
            width=100,
            values=[
                "Single",
                "Double"
            ],
            command=self.get_click_type
        )
        self.click_type.pack(side="left", padx=10)
        self.click_type.set("Single")

        #=======================
        # Toggle Auto Clicker
        #=======================

        # Frame
        self.toggle_frame = ctk.CTkFrame(
            self.main_frame,
            height=300
        )
        self.toggle_frame.pack(
            padx=20,
            pady=(10, 20),
            fill="x",
        )
        self.toggle_frame.pack_propagate(False)

        # Start button
        self.start_button = ctk.CTkButton(
            self.toggle_frame,
            height=50,
            width=150,
            text=f"Start ({Config.hotkey})",
            command= self.start_clicker
        )
        self.start_button.pack(padx=10, pady=(20, 0), fill="x")


        # Stop button
        self.stop_button = ctk.CTkButton(
            self.toggle_frame,
            height=50,
            width=150,
            text=f"Stop",
            command= self.stop_clicker
        )
        self.stop_button.pack(padx=10, pady=(20, 0), fill="x")

        self.hotkey_button = ctk.CTkButton(
            self.toggle_frame,
            height=50,
            width=150,
            text="Set hotkey",
            command=self.get_hotkey
        )
        self.hotkey_button.pack(padx=10, pady=(20, 40), fill="x")

    #=======================
    # Functions
    #=======================

    def update_interval(self):
        if self.hours.get() == "":
            self.hours.set("0")

        if self.minutes.get() == "":
            self.minutes.set("0")

        if self.seconds.get() == "":
            self.seconds.set("0")

        if self.milliseconds.get() == "":
            self.milliseconds.set("100")

        try:
            hour = int(self.hours.get())
            minutes = int(self.minutes.get())
            seconds = int(self.seconds.get())
            milliseconds = int(self.milliseconds.get())

        except ValueError:
            return

        if hour < 0:
            self.hours.set("0")
            hour = 0

        if minutes < 0:
            self.minutes.set("0")
            minutes = 0

        if seconds < 0:
            self.seconds.set("0")
            seconds = 0

        if milliseconds < 0:
            self.milliseconds.set("100")
            milliseconds = 100

        total = (
            hour * 60 * 60
            + minutes * 60
            + seconds
            + milliseconds / 1000
        )

        if total <= 0:
            milliseconds = 100
            self.milliseconds.set("100")
            total = 0.1

        Config.interval = total
        print(f"Interval: {Config.interval}s")

    def get_click_type(self, click_type):
        clicker.type = click_type.lower()

    def get_button_type(self, button_type):
        clicker.button = button_type.lower()
    

    def get_hotkey(self):
        clicker.set_hotkey()

    def start_clicker(self):
        if not Config.hotkey:
            return
        clicker.start_loop()


    def stop_clicker(self):
        clicker.stop_loop()

    def update_button(self):
        self.start_button.configure(
                text=f"Start ({Config.hotkey})"
        )
        self.after(100, self.update_button)        

    def create_time_field(parent, label):
        frame = ctk.CTkFrame(parent, fg_color="transparent")

        entry = ctk.CTkEntry(
            frame,
            width=70
        )
        entry.pack(side="left")

        text = ctk.CTkLabel(
            frame,
            text=label
        )
        text.pack(side="left", padx=(5, 15))

        return frame, entry

    


def start():
    app = App()
    app.mainloop()