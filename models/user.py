from cmath import exp
import itertools
from models.expense import Expense


class User:

    id_iter = itertools.count(start=0, step=1)

    def __init__(self, name, email, username, password):
        if type(name) is not str:
            raise ValueError

        if type(email) is not str:
            raise ValueError

        self.id = next(User.id_iter)
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.expenses = []

    def add_expense(self, expense: Expense):
        """Add an expense to user's list"""
        if type(expense) is not Expense:
            raise TypeError

        self.expenses.append(expense)

    def delete_expense(self, expense: Expense):
        """Remove an expense from user's list"""
        index = None
        for i, e in enumerate(self.expenses):
            if e.get_expense_id() == expense.get_expense_id():
                index = i
                break

        del self.expenses[index]

    def edit_expense(self, expense_id: int, attr: str, value):
        """Allow user to edit an existing expense"""
        for e in self.expenses:
            if e.get_expense_id() == expense_id:
                e.edit_attr(attr, value)
