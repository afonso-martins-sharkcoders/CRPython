import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime


class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendário com Agenda")

        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.year = datetime.now().year
        self.month = datetime.now().month

        self.create_widgets()
        self.show_calendar(self.year, self.month)

    def create_widgets(self):
        self.header = ttk.Frame(self.root)
        self.header.pack(pady=10)

        self.prev_button = ttk.Button(self.header, text="<<", command=self.prev_month)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = ttk.Button(self.header, text=">>", command=self.next_month)
        self.next_button.pack(side=tk.RIGHT)

        self.month_label = ttk.Label(self.header, text="", font=("Arial", 16))
        self.month_label.pack(side=tk.LEFT, padx=20)

        self.calendar_frame = ttk.Frame(self.root)
        self.calendar_frame.pack()

        self.agenda_frame = ttk.Frame(self.root)
        self.agenda_frame.pack(pady=10)

        self.agenda_label = ttk.Label(self.agenda_frame, text="Agenda", font=("Arial", 14))
        self.agenda_label.pack()

        self.agenda_text = tk.Text(self.agenda_frame, width=40, height=10)
        self.agenda_text.pack()

    def show_calendar(self, year, month):
        self.month_label.config(text=f"{calendar.month_name[month]} {year}")

        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        days = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
        for day in days:
            ttk.Label(self.calendar_frame, text=day).grid(row=0, column=days.index(day))

        month_days = self.cal.monthdayscalendar(year, month)
        for i, week in enumerate(month_days):
            for j, day in enumerate(week):
                if day != 0:
                    day_button = ttk.Button(self.calendar_frame, text=str(day),
                                            command=lambda d=day: self.show_agenda(d))
                    day_button.grid(row=i + 1, column=j)

    def show_agenda(self, day):
        self.agenda_text.delete(2.0, tk.END)
        self.agenda_text.insert(tk.END, f"Agenda para {day}/{self.month}/{self.year}:\n")

    def prev_month(self):
        if self.month == 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1
        self.show_calendar(self.year, self.month)

    def next_month(self):
        if self.month == 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1
        self.show_calendar(self.year, self.month)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
