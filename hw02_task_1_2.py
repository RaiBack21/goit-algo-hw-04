from pathlib import Path

# Task 1
def total_salary(path):
    """
    Calculates the total and average salary of all developers.
    """
    total_salary = list()

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                total_salary.append(float(line.strip().split(',')[1]))
        
        return (sum(total_salary), sum(total_salary) / len(total_salary))
    
    except Exception:
        print("Файл відсутній або пошкоджений.")
        return (0, 0)

# Task 2
def get_cats_info(path):
    """
    Returns a list of dictionaries with information about each cat.
    """
    cats_list = list()

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip().split(',')
                cats_list.append({'id': line[0], 'name': line[1], 'age': line[2]})

        return cats_list
    
    except Exception:
        return "Файл відсутній або пошкоджений."
                

total, average = total_salary("salaries.txt")
print(total, average)

cats_info = get_cats_info("cats.txt")
print(cats_info)
