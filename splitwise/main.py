from models.users import User
from services.splitwise import SplitWise
from constants import EQUAL
from BOs import ExpenseItemBO, UserBO

if __name__ == '__main__':

    u1 = User(UserBO("akash", "a@gmail.com", 1111, "8960282870"))
    u2 = User(UserBO("sam", "s@gmail.com", 1112, "8960282870"))
    u3 = User(UserBO("raj", "r@gmail.com", 1113, "8960282870"))
    u4 = User(UserBO("mon", "c@gmail.com", 1114, "8960282870"))
    e1 = ExpenseItemBO(u1, 1000,  EQUAL, [u2,u3,u4])
    e2 = ExpenseItemBO(u2, 1000,  EQUAL, [u1,u3,u4])
    allUsers = [u1, u2, u3, u4]

    splitWise = SplitWise(allUsers)
    print(splitWise.show())
    print(splitWise.show(u1))
    splitWise.registerExpense(e1)
    splitWise.registerExpense(e2)
    print(splitWise.show())