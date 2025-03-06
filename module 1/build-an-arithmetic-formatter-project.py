def arithmetic_arranger(problems, solution = False):
    #Errors
    #Too many problems:
    if len(problems)>5:
        return 'Error: Too many problems.'
    #If within 5 problems max
    else:
        condition = len(problems)
        individual_problems_list = []
        #Create a list with individual lists for each problem
        for problem in problems:
            individual_problems_text = problem.split(' ')
            individual_problems_list.append(individual_problems_text)
        
        first_operand = []
        second_operand = []
        operator = []
        
        #Create individual lists for each operand and operator
        for item in individual_problems_list:
            first_operand.append(item[0])
            second_operand.append(item[2])
            operator.append(item[1])

        #Create second line
        second_line_list = []
        
        #Define lenghts of everything
        operator_spaces = []
        iterator_1 = 0
        space = ' '
        #Calculate how many spaces for operator
        while iterator_1 < len(problems):
            if len(first_operand[iterator_1]) <= len(second_operand[iterator_1]):
                operator_spaces.append(space*1)
            else:
                dif = (len(first_operand[iterator_1]) - len(second_operand[iterator_1])) + 1
                operator_spaces.append(space*dif)
            iterator_1 +=1
        
        len_first = len(first_operand)
        len_second_operand = len(second_operand)
        
        
        #Define length of the second line and dashes
        line = '-'
        dash_number = []
        iterator_2 = 0
        while iterator_2 < len(problems):
            dash_count = len(operator_spaces[iterator_2]) + len(second_operand[iterator_2]) + 1
            dash_number.append(line*dash_count)
            iterator_2 += 1
        
        #Third line
        third_line = '    '.join(dash_number)
                     
        #Join operator and second operand
        iterator_3 = 0
        while iterator_3 <= (len(problems)-1):
            if iterator_3 < (len(problems)-1):
                second_line_list.append(f'{operator[iterator_3]}{operator_spaces[iterator_3]}{second_operand[iterator_3]}    ')
                iterator_3 += 1
            elif iterator_3 == (len(problems)-1):
                second_line_list.append(f'{operator[iterator_3]}{operator_spaces[iterator_3]}{second_operand[iterator_3]}')
                iterator_3 += 1
 
        
        #Calculate first_space
        if len(second_operand[0]) < len(first_operand[0]):
            first_line_space = space * 2

        else:
            first_line_space = space * ((len(second_operand[0]) - len(first_operand[0])) +2)
    
        #Calculate spaces in between first operands
        first_line_list = [first_operand[0]]
        iterator = 1
        while iterator < (len(problems)):
            if len(second_operand[iterator]) >= len(first_operand[iterator]):
                space_between = len(second_operand[iterator]) - len(first_operand[iterator])+6
                first_line_list.append((space*space_between)+first_operand[iterator])
                iterator += 1

            elif len(second_operand[iterator]) < len(first_operand[iterator]):
                first_line_list.append((space*6)+first_operand[iterator])
                iterator += 1
            
        first_line = ''.join(first_line_list)
        second_line = ''.join(second_line_list)
        
        final_text = f'{first_line_space}{first_line}\n{second_line}\n{third_line}'
        
        #Error for invalid operators
        for item in operator:
            if item != '+' and item != '-':
                return "Error: Operator must be '+' or '-'."
        
        #Error for invalid first operands
        for item in first_operand:
            if not item.isnumeric():
                return 'Error: Numbers must only contain digits.'
            elif len(item) >= 5:
                return 'Error: Numbers cannot be more than four digits.' 
        
        #Error for invalid second operands
        for item in second_operand:
            if not item.isnumeric():
                return 'Error: Numbers must only contain digits.'
            elif len(item) >= 5:
                return 'Error: Numbers cannot be more than four digits.' 

        #Math Time
        solution_list = []
        iterator_m = 0
        while iterator_m < len(problems):
            if operator[iterator_m] == '+':
                solution_list.append(int(first_operand[iterator_m]) + int(second_operand[iterator_m]))
                iterator_m += 1
            elif operator[iterator_m] == '-':
                solution_list.append(int(first_operand[iterator_m]) - int(second_operand[iterator_m]))
                iterator_m += 1

        solution_str_list = []
        for i in solution_list:
            item = str(i)
            solution_str_list.append(item)
        
        #Solution line spaces
        #First space
        solution_first_space = (len(dash_number[0]) - len(solution_str_list[0]))*space
        
        #Space in between solutions
        solution_line_list = [solution_str_list[0]]
        iterator_final = 1
        while iterator_final < len(problems):
            solution_space = ((len(dash_number[iterator_final])) - len(solution_str_list[iterator_final])+4)*space 
            solution_line_list.append(solution_space+solution_str_list[iterator_final])           
            iterator_final += 1
        
        solutions = ''.join(solution_line_list)
        
        final_text_solution = f'{first_line_space}{first_line}\n{second_line}\n{third_line}\n{solution_first_space}{solutions}'

        
        #No Math
        if solution == False:
            return final_text
        
        #Yes Math
        if solution == True:
            return final_text_solution
        

           
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')




'''----------------------old code--------------------------------
def arithmetic_arranger(problems, solution = False):
    results = []
    #Errors
    #Too many problems:
    if len(problems)>5:
        return 'Error: Too many problems.'
    #If within 5 problems max
    else:
        #Function to iterate over problems
        def iteration_text(problems):
            #Get each individual operand and operator in text
            operation_text = problems.split(" ")
            first_operand = operation_text[0]
            operator = operation_text[1]
            second_operand = operation_text[2]

            #Define lenghts of everything
            len_first = len(first_operand)
            len_second_operand = len(second_operand)
            #Calculate how many spaces
            space = ' '
            space_len = 1
            #Check which operand is the longest
            #Then add the appropriate number of spaces after operator
            if len(first_operand) <= len(second_operand):
                space_len = 1
            else:
                space_len = (len(first_operand)-len(second_operand))+1
            
            line_num = max(len_first,len_second_operand)
            line = '-'
            #Define length of the second line
            len_second_line = len(second_operand)+space_len+1
            
            #Define final text
            final_text = f'{first_operand:>{len_second_line}}\n{operator}{space*space_len}{second_operand}\n{line*len_second_line}    '
            return final_text
        
        all_text = list(map(iteration_text,problems))
    
    #Return the results
    return '\n\n'.join(all_text)

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')'''
