def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                name, salary = line.strip().split(',')
                salaries.append(int(salary))

            total = sum(salaries)
            average = total / len(salaries) if salaries else 0
            return total, int(average)
    except FileNotFoundError:
        print(f"File at {path} not found.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0

total, average = total_salary('salaries.txt')
print(f"Total amount: {total}")
print(f"Average amount: {average}")