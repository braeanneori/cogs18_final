#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class MyExpenses():

#Tests to see if a user's expenses are going above or below what is suggested
    
    def __init__(self, item, price, date):
        self.item = item
        self.price = price
        self.date = date
        
        
    def expense_check(self):
        monthly_budget = 1000
        """Finds if a user has spend too much on one item
        
        Parameters
        ----------
        input: self.price
            Price that will be checked
            
        Returns
        -------
        output : string
            Lets a user know if they have spent to much on one item, or if they're in the clear
        """
        if monthly_budget - self.price <= 900:
            print("You spent too much on one item!")
        else:
            print("You are in the clear!")
    
    
    def monthly_check(self):
        """Lets user know when they should be more mindful of spending
        
        Paramters
        ---------
        input: self.date
            Date that will be checked
            
        Returns
        -------
        output: string
            Tells the user if the month just started, or that they're past the halfway mark
        """
        
        #This function only takes into account the month of December - 12, and the decimal is the date
        if self.date >= 12.16:
            print("You are halfway through the month. Be careful with your spending!")
        else:
            print("The month just restarted, but keep track of your expenses!")


# In[ ]:


def add_expenses(expense_list):
    """Add a list of expenses
    
    Parameters
    ----------
    expense_list : list
        Integers that will be added
    Returns
    -------
    total: integer
        Gives the total of the list
    """
    total = sum(expense_list)
        
    return total
    
def leftover(expense_list):
    """Checks how much of the budget is leftover
    
    Parameters
    ----------
    expense_list: list
        Prices that will be added
        
    Returns
    -------
    budget = integer
        Amount of money leftover in the budget
    """
    
    #The total of the expenses is subtracted from the monthly budget
    monthly_budget = 1000
    total = sum(expense_list)
        
    budget = monthly_budget - total
        
    return budget

