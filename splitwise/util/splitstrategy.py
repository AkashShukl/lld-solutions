from constants import EQUAL, EXACT, PERCENT
from BOs import ExpenseItemBO
import ipdb


class SplitStrategy:
    def split(self, register , expenseItem : ExpenseItemBO):
        raise NotImplementedError("SubClasses must implement this method")

    def update_register(self, register, payer_id, reciver_id, net):
        register[payer_id][reciver_id] += net
        register[reciver_id][payer_id] -= net


class EqualSplitStrategy(SplitStrategy):
    def split(self,register, expenseItem : ExpenseItemBO):
        # ipdb.set_trace()
        splitFactor = len(expenseItem.paidForUsers)
        expenditure_per_head = round(expenseItem.amount / splitFactor, 2)

        for user in expenseItem.paidForUsers:
            if user.uid != expenseItem.payer.uid:
                self.update_register(register, expenseItem.payer.uid,
                                     user.uid, expenditure_per_head)


class PercentSplitStrategy(SplitStrategy):
    def split(self, register,expenseItem : ExpenseItemBO):
        for idx in range(len(expenseItem.paidForUsers)):
            uid = expenseItem.paidForUsers[idx].uid
            percent = expenseItem.paidPercents[idx]
            net = expenseItem.amount * percent / 100
            if uid != expenseItem.payer.uid:
                self.update_register(register, expenseItem.payer.uid, uid, net)


class ExactSplitStrategy(SplitStrategy):
    def split(self, register,expenseItem : ExpenseItemBO):
        for idx in range(len(expenseItem.paidForUsers)):
            uid = expenseItem.paidForUsers[idx].uid
            net = expenseItem.paidAmounts[idx]
            if uid != expenseItem.payer.uid:
                self.update_register(register, expenseItem.payer.uid, uid, net)

