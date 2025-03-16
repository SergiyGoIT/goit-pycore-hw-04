def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(",")
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}")

        if not salaries:
            return 0, 0  

        total = sum(salaries)
        average = total / len(salaries)
        return total, average

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

total, average = total_salary("D:\\Git_GoIT\\goit-pycore-hw-04\\salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
