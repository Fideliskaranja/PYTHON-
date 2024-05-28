print("Try programiz.pro")
def compute_gross_pay(hours_worked, rate_per_hour):
    return hours_worked * rate_per_hour
try:
    hours_worked = float(input("Enter hours: "))
    rate_per_hour = float(input("Enter rate per hour: "))
    
  
    gross_pay = compute_gross_pay(hours_worked, rate_per_hour)
    
    print(f"Gross pay: {gross_pay:.2f}")
except ValueError:
    print("Please enter valid numerical values for hours and rate.")
