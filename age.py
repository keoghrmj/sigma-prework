import datetime


def age_calculator(user_date, current_date):
    formatted_user_date = datetime.datetime.strptime(
        user_date, "%d-%m-%Y").date()
    date_diff = current_date.year-formatted_user_date.year
    if (current_date.month, current_date.day) < (formatted_user_date.month, formatted_user_date.day):
        date_diff -= 1
    return date_diff


if __name__ == "__main__":
    user_date = input("Please enter a date in the format dd-mm-yyyy: ")
    current_date = datetime.date.today()
    print(f'You are {age_calculator(user_date, current_date)} years old')
