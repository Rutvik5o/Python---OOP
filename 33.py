#(13)=>Create a program name "employeepy" and implement the functions DA,HRA,PF And ITAX. Create another program that uses the function of employee module and calculates gross and net salaries of an employee.


import employee


print("Salary Program")

name = str(input("Enter the name of the employee=>"))

basic= float(input("Enter Basic salary=>"))

netPay=employee.netpay(basic)

print(f'Net Salary=>',netPay)

grosPay=employee.grosspay(basic)

print(f'gross Salary=> ',grosPay)

