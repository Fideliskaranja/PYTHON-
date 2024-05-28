print("Try programiz.pro")
def check_loan_eligibility(age, income):
    if age >= 21 and income >= 21000:
        return "Congratulations, you qualify for a loan!"
    else:
        return "Unfortunately, we are unable to offer you a loan at this time."

def main():
    try:
    
        age = int(input("Enter your age: "))
        
        income = float(input("Enter your annual income: "))
        
        result = check_loan_eligibility(age, income)
        
        print(result)
    except ValueError:
        print("Please enter valid numerical values for age and income.")

# Run the main function 
if __name__ == "__main__":
    main()



