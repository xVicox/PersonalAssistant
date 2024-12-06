from expense import Expense
from expense_tracker import ExpenseTracker

expense_tracker = ExpenseTracker()

#make category inputs lowercase !!!!
exp1 = Expense("ESP32 - Super Starter Kit", 47.5, "hobbies")
exp2 = Expense("ESP32 NodeMCU Module WLAN WiFi Dev Kit", 25.2, "hobbies")
exp3 = Expense("5 x KY-015 DHT 11 Temperature Sensor", 13.1, "hobbies")
exp4 = Expense("J.R.R. Tolkien - Hobbit", 7.5, "education")


expense_tracker.add_expense(exp1)
expense_tracker.add_expense(exp2)
expense_tracker.add_expense(exp3)
expense_tracker.add_expense(exp4)

print("==================")
expense_tracker.show_expenses("hobbies")
print("==================")





