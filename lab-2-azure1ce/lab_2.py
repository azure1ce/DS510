# Lab 2 
#Jingming Tan 1278301612
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
def education_details(major, graduation_year):
    major = str(major)
    graduation_year = int(graduation_year)
    print(major+",",graduation_year)
    return

# invoke function example: uncomment below line after completing above function
education_details("Computer Science", "2025")


# ----------------- Question 2 -----------------
# Create global variable named "usd_to_gbp" with value as 1.25
usd_to_gbp = 1.25
def yearly_allowance(hourly_wage, weekly_hours, weeks_per_year):
    hourly_wage = float(hourly_wage)
    weekly_hours = int(weekly_hours)
    weeks_per_year = int(weeks_per_year)
    total_yearly_allowance = int(hourly_wage*weekly_hours*weeks_per_year)
    return total_yearly_allowance


def conversion_to_british_pound(usd_amount):
    usd_amount = int(usd_amount)
    gbp_amount = round(float(usd_amount/usd_to_gbp),1)
    return gbp_amount

# uncomment below lines after completing above functions
hourly_wage = 15
weekly_hours = 40
weeks_per_year = 52

# uncomment below and invoke the function with relevant args
usd_amount = 1000
gbp_amount = 1000


# ----------------- Question 3 -----------------
def yearly_profit(daily_profit, days_per_year):
    daily_profit = int(daily_profit)
    days_per_year = int(days_per_year)
    total_yearly_profit = int(daily_profit*days_per_year)
    return total_yearly_profit


def percentage_change(current_profit, previous_profit):
    current_profit = int(current_profit)
    previous_profit = int(previous_profit)
    total_percentage_change = round(float((current_profit-previous_profit))/previous_profit*100,2)
    if total_percentage_change >= 0:
        return (str(total_percentage_change)+"% profit")
    elif total_percentage_change <0:
        return (str(-total_percentage_change)+"% loss")

# uncomment below lines after completing above functions
daily_profit = 250
days_per_year = 365
previous_profit = 60000

# uncomment below and invoke the function with relevant args
current_profit = 100000
percent_change = "0% profit"
