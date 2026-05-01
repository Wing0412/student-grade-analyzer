#wyt44
import matplotlib.pyplot as plt

# Student Grade + Histogram Analyzer with Graph


def calculate_average(scores):
    return sum(scores) / len(scores)


def assign_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"




def main():
    print("Student Grade + Histogram Analyzer")

    student_name = "Alex"
    scores = [75, 82, 68, 90, 77, 82, 75, 90, 68, 82]

    average = calculate_average(scores)
    grade = assign_grade(average)
    histogram = create_histogram(scores)

    print(f"\nStudent: {student_name}")
    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Histogram: {histogram}")

    # Show graph
    plot_histogram(histogram)


if __name__ == "__main__":
    main()
    //Added histogram feature to show score distribution
