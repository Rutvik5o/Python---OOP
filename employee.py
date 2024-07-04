# employeepy.py

def calculate_da(basic_salary):
    """Calculate Dearness Allowance (DA)"""
    da = basic_salary * 0.10  # 10% of basic salary
    return da

def calculate_hra(basic_salary):
    """Calculate House Rent Allowance (HRA)"""
    hra = basic_salary * 0.15  # 15% of basic salary
    return hra

def calculate_pf(basic_salary):
    """Calculate Provident Fund (PF)"""
    pf = basic_salary * 0.12  # 12% of basic salary
    return pf

def calculate_itax(gross_salary):
    """Calculate Income Tax (ITAX)"""
    # Simple progressive tax rate for example purposes
    if gross_salary <= 250000:
        itax = 0
    elif gross_salary <= 500000:
        itax = (gross_salary - 250000) * 0.05
    elif gross_salary <= 1000000:
        itax = (500000 - 250000) * 0.05 + (gross_salary - 500000) * 0.20
    else:
        itax = (500000 - 250000) * 0.05 + (1000000 - 500000) * 0.20 + (gross_salary - 1000000) * 0.30
    return itax

def grosspay(basic_salary):
    """Calculate Gross Salary"""
    da = calculate_da(basic_salary)
    hra = calculate_hra(basic_salary)
    gross_salary = basic_salary + da + hra
    return gross_salary

def netpay(basic_salary):
    """Calculate Net Salary"""
    gross_salary = grosspay(basic_salary)
    pf = calculate_pf(basic_salary)
    itax = calculate_itax(gross_salary)
    net_salary = gross_salary - pf - itax
    return net_salary
