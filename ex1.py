#program to perform sentiment analysis on product reviews from a CSV file
#displaying reviews 
#cleaning data by removing duplicates and invalid entries
#analyzing sentiment using predefined word lists
#showing summary and bar chart of sentiment distribution


import csv
import re
import matplotlib.pyplot as plt

# ---------------- SENTIMENT WORD LISTS -------------------

positive_words = [
    "good", "excellent", "amazing", "awesome", "nice",
    "love", "satisfied", "happy", "best", "perfect"
]

negative_words = [
    "bad", "poor", "worst", "hate", "disappointed",
    "terrible", "awful", "problem", "boring", "waste"
]

# ---------------- GLOBAL VARIABLES -----------------------

reviews = []                 # raw reviews
cleaned_reviews_list = []    # cleaned reviews
sentiments = []

positive_count = 0
negative_count = 0
neutral_count = 0

is_cleaned = False

# ---------------- FUNCTIONS -----------------------------

def load_reviews(filename):
    data = []
    try:
        with open(filename, 'r', encoding='latin-1') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row:
                    data.append(row[0])
    except FileNotFoundError:
        print("File not found")
    return data


def analyze_sentiment(review):
    review = review.lower()
    pos = 0
    neg = 0

    for w in positive_words:
        if w in review:
            pos += 1

    for w in negative_words:
        if w in review:
            neg += 1

    if pos > neg:
        return "Positive"
    elif neg > pos:
        return "Negative"
    else:
        return "Neutral"


def clean_reviews(review_list):
    cleaned = []
    for review in review_list:
        review = review.strip()

        if not review:
            continue

        if review in cleaned:
            continue

        # keep only reviews that contain at least one letter
        if re.search(r'[a-zA-Z]', review):
            cleaned.append(review)

    return cleaned


def analyze_all_reviews():
    global positive_count, negative_count, neutral_count, sentiments

    sentiments.clear()
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for review in cleaned_reviews_list:
        result = analyze_sentiment(review)
        sentiments.append(result)

        if result == "Positive":
            positive_count += 1
        elif result == "Negative":
            negative_count += 1
        else:
            neutral_count += 1


def display_reviews():
    print("\nALL REVIEWS (RAW DATA)")
    print("-" * 50)

    for i, review in enumerate(reviews):
        if re.search(r'[a-zA-Z]', review):
            sentiment = analyze_sentiment(review)
        else:
            sentiment = "Not Analyzed / Invalid"

        print(f"{i+1}. {review} --> {sentiment}")


def show_summary():
    total = positive_count + negative_count + neutral_count
    print("\nSENTIMENT SUMMARY (CLEANED DATA)")
    print("-" * 40)
    print("Total Valid Reviews :", total)
    print("Positive :", positive_count)
    print("Negative :", negative_count)
    print("Neutral  :", neutral_count)


def draw_bar_chart():
    labels = ['Positive', 'Negative', 'Neutral']
    values = [positive_count, negative_count, neutral_count]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Sentiment Analysis on Cleaned Reviews")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()


def menu():
    print("\n----- MENU -----")
    print("1. View All Reviews (Raw)")
    print("2. Clean Reviews & Analyze")
    print("3. View Sentiment Summary")
    print("4. Display Bar Chart")
    print("5. Exit")


# ---------------- MAIN PROGRAM ---------------------------

def main():
    global reviews, cleaned_reviews_list, is_cleaned

    reviews = load_reviews(
        "C:/Users/KEERTHANA/OneDrive/Desktop/program/reviews.csv"
    )

    print("DEBUG: Raw reviews loaded =", len(reviews))

    if not reviews:
        print("No reviews found")
        return

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            display_reviews()

        elif choice == '2':
            cleaned_reviews_list = clean_reviews(reviews)
            is_cleaned = True

            print("DEBUG: Cleaned reviews =", len(cleaned_reviews_list))
            analyze_all_reviews()

            print("Data cleaning & analysis completed")

        elif choice == '3':
            if not is_cleaned:
                print("Please clean the data first (choose option 2)")
            else:
                show_summary()

        elif choice == '4':
            if not is_cleaned:
                print("Please clean the data first (choose option 2)")
            else:
                draw_bar_chart()

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


# ---------------- PROGRAM START --------------------------

main()
