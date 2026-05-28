from pathlib import Path

def total_salary(path):
  
  # checking for existing file and early return if not exist
  file = Path(path)
  if not file.exists():
    return None

  with open(path, mode='r', encoding="utf-8", errors="strict") as fh:
    # checking case if lines have \n
    people = [el.strip() for el in fh.readlines()]

    total = 0

    for person in people:
      total += int(person.split(",")[1])
    average = int(total / len(people))

    return total, average


total, average = total_salary("goit-pycore-hw-04/salary_file.txt") 
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
