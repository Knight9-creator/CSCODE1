def score_analyzer():
    scores = []

    i = 0
    while i < 6:
        try:
            user_input = float(input(f"Type in a score for Score #{i+1}: "))
            scores.append(user_input)
            i += 1

        except ValueError:
            print("Invalid Input!")
    

    min_score = min(scores)
    max_score = max(scores)
    sum_score = sum(scores)

    print("\n" + "Results: " + "\n" + f"Scores: {scores}" + "\n" + f"Average: {sum_score / len(scores):.2f}" + "\n" + f"Maximum Score: {max_score:.2f}" + "\n" + f"Minimum Score {min_score:.2f}" + "\n")

if __name__ == '__main__':
    score_analyzer()
