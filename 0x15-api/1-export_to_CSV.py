#!/usr/bin/python3
"""extended Python script to export data in the CSV format."""


import csv
import requests
import sys


def gather_and_export_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()

    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            csv_writer.writerow([user_data['id'], user_data['username'], str(task['completed']), task['title']])

            print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer as the employee ID.")
        sys.exit(1)

    gather_and_export_data(employee_id)
