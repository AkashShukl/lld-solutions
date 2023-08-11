
from BOs import ExpenseItemBO
from services.register import Register

class SplitWise:
    def __init__(self, users):
        self.users = users
        self.register = Register(users)

    def show(self, user=None):
        reportString = "No balances"
        if user is None:
            report = []
            for user in self.users:
                report.extend(self.register.getReport(user.uid))
            if len(report) > 0:
                reportString = "\n".join(report)
        else:
            report = self.register.getReport(user.uid)
            if len(report) > 0:
                reportString = "\n".join(report)
        return reportString

    def registerExpense(self, expenseItem: ExpenseItemBO):
        self.register.split(expenseItem)
