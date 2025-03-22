class Category:
    def __init__(self, category, ledger=[]):
        self.category = category
        self.ledger = []
        self.balance = 0
        

    #Deposit
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description':description})
        self.balance += amount  
    
    #Withdraw
    def withdraw(self, amount, description=''): 
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description':description})
            self.balance -= amount 
            return True
        else:
            return False
    
    #Balance
    def get_balance(self):
        return self.balance
    
    #Transfer
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False
    
    #Check funds
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False
    
    #List expenses
    def total_expenses(self):
        expenses = 0
        for i in range(len(self.ledger)):
            if self.ledger[i].get('amount') < 0:
                expenses += abs(self.ledger[i].get('amount'))
        return expenses
                


    #Define STR output
    def __str__(self):
        if (len(self.category) % 2) == 0:
            asterix_left = (((30 - len(self.category)) // 2)) * '*'
            asterix_right = asterix_left
        else:
            asterix_left = (((30 - len(self.category)) // 2)) * '*'
            asterix_right = asterix_left+'*'  
        
        #Arrange ledger descriptions
        descriptions = []
        values = []
        long_description = ''
        short_description = ''
        for item in range(len(self.ledger)):
            #Check if lenght of description is over 23 characters
            if len(self.ledger[item].get('description')) > 23:
                #Create variable to protect original value from being changed
                long_description = self.ledger[item].get('description')
                #Create shorter description
                counter = 0
                while counter < 23:
                    short_description += long_description[counter]
                    counter += 1
                
                descriptions.append(short_description)
                values.append(f"{float(self.ledger[item].get('amount')):.2f}")
                short_description = ''
            else:
                descriptions.append(self.ledger[item].get('description'))
                values.append(f"{float(self.ledger[item].get('amount')):.2f}")
                
        #Create list with all budget items
        final_text_ = []
        for i in range(len(values)):
            #Get alignment size (total line size is 30)
            align = ' '*(30-(len(descriptions[i])+len(str(values[i]))))
            final_text_.append(f"{descriptions[i]}{align}{values[i]}")     
        
        final_text= '\n'.join(final_text_)
        return f"{asterix_left}{self.category}{asterix_right}\n{final_text}\nTotal: {self.balance:.2f}"


def percentage_printer(categories):
        #Calculate the total spent amount
    final_expenses = 0
    for category in categories:
        final_expenses += round(category.total_expenses())
    
    #Get percentages per category
    percentages = []
    for category in categories:
        percentages.append((category.total_expenses() / final_expenses)*100)

        #Print percentages and bars
    def bar_chart(category_number):
        if percentage > percentages[category_number]:
            return '   '
        elif percentage <= percentages[category_number]:
            return ' o '
    
    final_graph = ''
    for percentage in range(100,-10,-10):
        if len(percentages) == 4:
            if percentage > 0:
                final_graph += f'{percentage:>3}|{bar_chart(0)}{bar_chart(1)}{bar_chart(2)}{bar_chart(3)} \n'
            else:
                final_graph += f'{percentage:>3}|{bar_chart(0)}{bar_chart(1)}{bar_chart(2)}{bar_chart(3)} '
        elif len(percentages) == 3:
            if percentage > 0:
                final_graph += f'{percentage:>3}|{bar_chart(0)}{bar_chart(1)}{bar_chart(2)} \n'
            else:
                final_graph += f'{percentage:>3}|{bar_chart(0)}{bar_chart(1)}{bar_chart(2)} '
        elif len(percentages) == 2:
            if percentage > 0:
                final_graph += f'{percentage:>3}|{bar_chart(0)}{bar_chart(1)} \n'
            else:
                final_graph += f'{percentage:>3}|{bar_chart(0)}{bar_chart(1)} '
        elif len(percentages) == 1:
            if percentage > 0:
                final_graph += f'{percentage:>3}|{bar_chart(0)} \n'
            else:
                final_graph += f'{percentage:>3}|{bar_chart(0)} '
        
    return final_graph

#Creating chart
def create_spend_chart(categories):
    #Graph title
    title = 'Percentage spent by category'
      
    percentage_print = f'{percentage_printer(categories)}'
 
    #Lines
    line = '    '
    line +=('-'*len(categories)*3)+'-'

    #Category names
    category_names = []
    for category in categories:
        category_names.append(category.category)
        #Get category name sizes and save de longest
    category_size = []
    for category in categories:
        category_size.append(len(category.category))
    longest = max(category_size)
    shortest = min(category_size)
        #Normalize name size
    category_names_normalized = []
    for item in category_names:
        if len(item) < longest:
            item += ' '*(longest-len(item))
            category_names_normalized.append(item)
        else:
            category_names_normalized.append(item)

        
        #Prints
    def name_printer(line):
        string = '     '
        for item in category_names_normalized:
            string += ''+item[line]+f'  '
        return string
    
    names = ''
    for i in range(longest):
        if i < (longest-1):
            names += f'{name_printer(i)}\n'
        else:
            names += f'{name_printer(i)}'
    

    #Return
    return f'{title}\n{percentage_print}\n{line}\n{names}'




#TESTING
food = Category('Food')
clothing = Category('Clothing')
entertainment = Category('Entertainment')
auto = Category('Auto')

food.deposit(10, 'bought bread and paid rent')
food.deposit(300, 'ifood')
food.withdraw(31.23, 'a very very very long string')
food.deposit(40, 'misc')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
food.transfer(10, clothing)

clothing.deposit(100)
clothing.withdraw(30, 'pants')

entertainment.deposit(300, 'testing a very long string here')
entertainment.withdraw(3, 'rides')
entertainment.withdraw(10, 'testing')

auto.deposit(1000)
auto.withdraw(50)


print(entertainment)
print('\n')
print(create_spend_chart([food,clothing,entertainment,auto]))

