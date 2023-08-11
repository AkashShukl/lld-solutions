from BOs import UserBO, ExpenseItemBO
from constants import EQUAL, EXACT, PERCENT
from util.splitstrategy import EqualSplitStrategy
from util.splitstrategy import PercentSplitStrategy
from util.splitstrategy import ExactSplitStrategy
from exceptions import UnexpectedSplitStrategy


class Register:
    def __init__(self, users):
        self.users = users
        self.register = {}

        for user in self.users:
            self.register[user.uid] = dict()
            for u in self.users:
                if user != u:
                    self.register[user.uid][u.uid] = 0
        print(self.register)

    def split(self, expenseItem: ExpenseItemBO):

        try:
            splitStrategy = None
            if expenseItem.splitStrategy == EXACT:
                splitStrategy = ExactSplitStrategy()

            elif expenseItem.splitStrategy == PERCENT:
                splitStrategy = PercentSplitStrategy()

            elif expenseItem.splitStrategy == EQUAL:
                splitStrategy = EqualSplitStrategy()

            splitStrategy.split(self.register, expenseItem)
        except:
            raise UnexpectedSplitStrategy(" unexpected ", expenseItem.splitStrategy == EQUAL)

    def getReport(self, uid):
        reportString = []
        report = self.register[uid]
        for k, v in report.items():

            if v < 0:
                reportString.append(str(uid) + " owes " +
                                    str(k) + " : " + str(v))
        return reportString
