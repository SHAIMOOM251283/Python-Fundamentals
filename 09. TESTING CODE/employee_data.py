from employee import Employee

emp_list = []

print("Enter 'q' at any time to quit.\n")
while True:
    first_name = input("\nEnter First Name: ").title()
    if first_name.lower() == 'q':
        break
    last_name = input("Enter Last Name: ").title()
    if last_name.lower() == 'q':
        break
    annual_salary = input("Enter Annual Salary: ")
    if annual_salary == 'q':
        break    
    emp = Employee(first_name, last_name, int(annual_salary))
    bonus_input = input("Enter Bonus Amount (or press enter to skip): ")
    if bonus_input != '':
        bonus_amount = int(bonus_input)
        emp.give_raise(bonus_amount)
    else:
        emp.give_raise()
    emp_list.append(emp)

    for emp in emp_list:
        print(f"\nName: {emp.first_name} {emp.last_name}\nAnnual Salary: {emp.annual_salary}")