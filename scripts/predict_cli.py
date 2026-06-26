# predict_cli.py
from models.predict import JobClassifier

def main():
    clf = JobClassifier()

    while True:
        title = input("\nJob Title: ")
        desc = input("Job Description: ")

        result = clf.predict_with_confidence(title, desc)

        print("\nPrediction:", result["label"])
        print("Confidence:", round(result["confidence"], 3))

if __name__ == "__main__":
    main()