total_score = 0
count = 0

try:
    with open("grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            # strip() removes the newline \n, split(",") separates name and score
            name, score = line.strip().split(",")
            total_score += int(score)
            count += 1

    if count > 0:
        average = total_score / count
        print(f"Processed {count} students. Average Score: {average:.2f}")
    else:
        print("The file is empty.")

except FileNotFoundError:
    print("Error: 'grades.txt' not found.")