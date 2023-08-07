from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import requests

def main():
    current_date = datetime.now()
    print(current_date)

def data():
    r = requests.get('https://habr.com/ru/all/')
    print(r.status_code)

if __name__ == '__main__':
    main()
    calculate_salary()
    get_employees()
    data()
