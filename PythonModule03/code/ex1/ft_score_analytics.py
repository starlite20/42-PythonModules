import sys

def main():
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores = []

    i = 1
    while i < len(sys.argv):
        try:
            score = int(sys.argv[i])
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1

    len_scores = len(sys.argv)
    if len_scores == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total_score = sum(scores)
    average_score = total_score / len_scores
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print("Scores processed:", scores)
    print("Total players:", len_scores)
    print("Total score:", total_score)
    print("Average score:", average_score)
    print("High score:", high_score)
    print("Low score:", low_score)
    print("Score range:", score_range)


if __name__ == "__main__":
    main()