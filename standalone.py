from tkinter import *
from tkinter import messagebox

# ---------- DATA ----------
# Each flight: [flight_number, origin, destination, seats_available]
flights = [
    ["AA101", "New York", "London", 50],
    ["AA102", "Los Angeles", "Tokyo", 30],
    ["AA103", "Chicago", "Paris", 20],
    ["AA104", "Miami", "Dubai", 15]
]

bookings = []   # each booking: [passenger_name, flight_number]

# ---------- FUNCTIONS ----------
def show_flights():
    result.delete(1.0, END)
    result.insert(END, "AVAILABLE FLIGHTS\n\n")
    for flight in flights:
        result.insert(
            END,
            f"Flight: {flight[0]}\n"
            f"From: {flight[1]}\n"
            f"To: {flight[2]}\n"
            f"Seats: {flight[3]}\n\n"
        )

def search_flight():
    flight_no = flight_entry.get()
    result.delete(1.0, END)
    found = False
    for flight in flights:
        if flight[0] == flight_no:
            found = True
            result.insert(
                END,
                f"Flight Found\n\n"
                f"Flight: {flight[0]}\n"
                f"From: {flight[1]}\n"
                f"To: {flight[2]}\n"
                f"Seats Available: {flight[3]}"
            )
            break
    if not found:
        result.insert(END, "Flight Not Found")

def book_ticket():
    name = name_entry.get().strip()
    flight_no = flight_entry.get().strip()
    if not name or not flight_no:
        messagebox.showerror("Error", "Please enter both name and flight number")
        return

    for flight in flights:
        if flight[0] == flight_no:
            if flight[3] > 0:
                flight[3] -= 1
                bookings.append([name, flight_no])
                messagebox.showinfo("Success", "Ticket Booked Successfully")
                return
            else:
                messagebox.showerror("Error", "No Seats Available")
                return
    messagebox.showerror("Error", "Flight Not Found")

def view_bookings():
    result.delete(1.0, END)
    result.insert(END, "BOOKED TICKETS\n\n")
    if not bookings:
        result.insert(END, "No Bookings Found")
    else:
        for booking in bookings:
            result.insert(
                END,
                f"Passenger: {booking[0]}\n"
                f"Flight: {booking[1]}\n\n"
            )

def cancel_ticket():
    name = name_entry.get().strip()
    flight_no = flight_entry.get().strip()
    if not name or not flight_no:
        messagebox.showerror("Error", "Please enter both name and flight number")
        return

    for booking in bookings:
        if booking[0] == name and booking[1] == flight_no:
            bookings.remove(booking)
            # Increase seat count for that flight
            for flight in flights:
                if flight[0] == flight_no:
                    flight[3] += 1
                    break
            messagebox.showinfo("Success", "Booking Cancelled")
            return
    messagebox.showerror("Error", "Booking Not Found")

# ---------- GUI ----------
root = Tk()
root.title("Airline Management System")
root.geometry("980x650")
root.configure(bg="#0f766e")

# HEADER
header = Frame(root, bg="#f8fafc")
header.pack(fill=X)
Label(
    header,
    text="✈ AIRLINE CONTROL DASHBOARD",
    font=("Arial", 20, "bold"),
    bg="#f8fafc",
    fg="#0f766e"
).pack(pady=15)

# INPUT
center_frame = Frame(root, bg="#0f766e")
center_frame.pack(expand=True)

card = Frame(center_frame, bg="#f8fafc", bd=2, relief=RIDGE, padx=25, pady=20)
card.pack()

Label(card, text="Passenger Name", bg="#f8fafc").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = Entry(card, width=30)
name_entry.grid(row=0, column=1)

Label(card, text="Flight Number", bg="#f8fafc").grid(row=1, column=0, padx=10, pady=10, sticky="e")
flight_entry = Entry(card, width=30)
flight_entry.grid(row=1, column=1)

# BUTTONS
btn_frame = Frame(root, bg="#0f766e")
btn_frame.pack(pady=10)

Button(btn_frame, text="Flights", bg="#2563eb", fg="white", width=12, command=show_flights).grid(row=0, column=0)
Button(btn_frame, text="Search", bg="#3b82f6", fg="white", width=12, command=search_flight).grid(row=0, column=1)
Button(btn_frame, text="Book", bg="#16a34a", fg="white", width=12, command=book_ticket).grid(row=0, column=2)
Button(btn_frame, text="Bookings", bg="#f59e0b", fg="white", width=12, command=view_bookings).grid(row=0, column=3)
Button(btn_frame, text="Cancel", bg="#dc2626", fg="white", width=12, command=cancel_ticket).grid(row=0, column=4)

# OUTPUT
result = Text(root, width=110, height=18, bg="#ffffff", fg="#0f172a")
result.pack(pady=10)

# STATUS BAR
status_bar = Label(root, text="Ready ✈", bg="#f8fafc", fg="#0f766e", anchor=W)
status_bar.pack(fill=X, side=BOTTOM)

root.mainloop()