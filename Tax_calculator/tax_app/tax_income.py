def calculate_income_tax(taxable_income, expenses, num_dependents):
  income_amount = total_income - expenses
  basic_deduction = 1500000 #기본공제
  dependent_deduction = 1500000 * num_dependents   
  total_deduction = basic_deduction + dependent_deduction
  taxable_base = income_amount - total_deduction
  return max(taxable_bas,0),income_amount,total_deduction


def calculate_income_tax(taxable_income):
  #2025년 기준 누진세율(단순화)
  brackets = [
    (0,14000000,0.06,0),
    (14000000,50000000,0.15,1260000),
    (50000000,88000000,0.24,5760000),
    (88000000,150000000,0.35,15360000),
    (150000000,300000000,0.38,24360000),
    (300000000,500000000,0.40,36360000),
    (500000000,1000000000,0.42,48360000),
    (1000000000,float('inf'),0.45,78360000),
  ]
  for lower, upper, rate, deduction in brackets:
    if lower < taxable_income <=upper:
      return taxable_income *rate - deduction
  return 0
