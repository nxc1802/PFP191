# Q2 (3 marks): Weighted Average & Score Report

# 1. Weighted average
def weighted_average(scores, weights):
    total = sum(s * w for s, w in zip(scores, weights))
    total_weight = sum(weights)
    return total / total_weight


# 2. Input student data, calculate average, write to file
def input_and_report():
    subjects = ["CSI105", "MAD101", "MAE101", "PFP191"]
    weights  = [3, 3, 3, 3]

    name = input("Enter student name: ")

    scores = []
    for subj in subjects:
        while True:
            try:
                score = float(input(f"Enter score for {subj} (0-10): "))
                if 0 <= score <= 10:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    avg = weighted_average(scores, weights)

    # Write report to file
    with open("score_report.txt", "w") as f:
        f.write(f"Student: {name}\n")
        for subj, score in zip(subjects, scores):
            f.write(f"  {subj}: {score}\n")
        f.write(f"Average Score: {avg:.2f}\n")

    # Also print to console
    print(f"\nStudent: {name}")
    for subj, score in zip(subjects, scores):
        print(f"  {subj}: {score}")
    print(f"Average Score: {avg:.2f}")
    print("Report saved to score_report.txt")


input_and_report()
