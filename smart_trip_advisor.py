import tkinter as tk
from tkinter import messagebox

def plan_trip():
    destination = destination_entry.get()
    days = days_entry.get()
    budget = budget_entry.get()
    travel_type = travel_type_var.get()

   
    if destination == "" or days == "" or budget == "":
        messagebox.showerror("Error", "All fields must be filled")
        return

    try:
        days = int(days)
        budget = int(budget)
    except:
        messagebox.showerror("Error", "Days and Budget must be numbers")
        return

    daily_budget = budget / days

    
    if daily_budget < 1000:
        suggestion = "Low budget trip ❌\nChoose nearby places or reduce days"
    elif daily_budget < 3000:
        suggestion = "Medium budget trip 👍\nBudget friendly hotels & travel"
    else:
        suggestion = "High budget trip 😍\nComfortable and luxury options"

    
    result = f"""
Destination : {destination}
Days        : {days}
Travel Type : {travel_type}
Total Budget: ₹{budget}
Daily Budget: ₹{int(daily_budget)}

Suggestion:
{suggestion}
"""

    output_label.config(text=result)



root = tk.Tk()
root.title("Smart Trip Advisor App")
root.geometry("450x520")

tk.Label(root, text="Smart Trip Advisor", font=("Arial", 16, "bold")).pack(pady=10)


tk.Label(root, text="Destination").pack()
destination_entry = tk.Entry(root, width=30)
destination_entry.pack()


tk.Label(root, text="Number of Days").pack()
days_entry = tk.Entry(root, width=30)
days_entry.pack()


tk.Label(root, text="Total Budget (₹)").pack()
budget_entry = tk.Entry(root, width=30)
budget_entry.pack()


tk.Label(root, text="Travel Type").pack()
travel_type_var = tk.StringVar()
travel_type_var.set("Solo")

tk.OptionMenu(root, travel_type_var, "Solo", "Friends", "Family").pack()


tk.Button(root, text="Plan My Trip", command=plan_trip, bg="green", fg="white").pack(pady=15)


output_label = tk.Label(root, text="", justify="left", font=("Arial", 10))
output_label.pack(pady=10)

root.mainloop()