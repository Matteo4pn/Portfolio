import sys
import csv
from tabulate import tabulate

def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]

        return data
    except FileNotFoundError:
        sys.exit("Error: The specified file does not exist.")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

def print_pizza_table(data):
    table = tabulate(data, headers="keys", tablefmt="grid")
    print(table)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
        sys.exit("Usage: python pizza.py <filename.csv>")

    file_path = sys.argv[1]
    pizza_data = read_csv_file(file_path)
    print_pizza_table(pizza_data)
