class ExpenseTracker:

    def __init__(self):
        self._exp_categories = ["education", "hobbies"]
        self._expenses = []
        self._exp_hobbies = []
        self._exp_education = []
        self._total = 0
        self._hobbies_total = 0
        self._education_total = 0
        print("Expense tracker initialized")

    def add_expense(self, expense):
        # check for valid category
        if not expense.category in self._exp_categories:
            print("Not a valid category.")
        # check for negative expense cost
        elif expense.cost < 0:
            print("Can't accept an item with negative value.")
            print("Item was NOT added to the list.")
        # check for empty space in item name and category
        elif expense.item_name == "" or expense.category == "":
            print("Item name or category can't be empty")
            print("Item was NOT added to the list.")
        # validate input type - must be string
        elif  not isinstance(expense.item_name, str) or not isinstance(expense.category, str):
            print("Item name and category must be of type string")
            print("Item was NOT added to the list.")
        #inputs valid
        else:
            match expense.category.lower().strip():
                case "hobbies":
                    print("Adding expense to hobbies list")
                    self._exp_hobbies.append(expense)
                    self._hobbies_total += expense.cost
                case "education":
                    print("Adding expense to education list")
                    self._exp_education.append(expense)
                    self._education_total += expense.cost
                # New category cases to be added here

            #this isn't right, it will add any expense regardless of category
            self._total += expense.cost
            self._expenses.append(expense)
            print("Expense added")




    def get_expenses(self, category):
        match category.lower().strip():
            case "hobbies":
                return round(self._hobbies_total, 2)
            case "education":
                return round(self._education_total,2)
            case "total":
                return round(self._total,2)

    def show_expenses(self, category):
        match category.lower().strip():
            case "hobbies":
                print(f"Total of {len(self._exp_hobbies)} items in the 'hobbies' category:")
                print(f"Total price: {self._education_total}")
                for expense in self._exp_hobbies:
                    print("---------------------")
                    print(expense.__str__())
            case "education":
                print(f"Total of {len(self._exp_education)} items in the 'education' category:")
                print(f"Total price: {self._education_total}")
                for expense in self._exp_education:
                    print("---------------------")
                    print(expense.__str__())
            case "total":
                print("In show expenses - TOTAL")
                print(self._expenses)
                for expense in self._expenses:
                    print(expense.__str__())