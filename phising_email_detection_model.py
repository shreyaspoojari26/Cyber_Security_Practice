from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Simple dataset
emails = [
    "Congratulations you won a free prize click this link",
    "Your account has been selected for a reward claim now",
    "Urgent verify your bank account immediately",
    "You have won a lottery send your details",
    "Click here to reset your password immediately",
    "Your account will be blocked verify your information",
    "You received a free gift click the link",
    "Update your payment information urgently",

    "Meeting is scheduled for tomorrow at 10 AM",
    "Please find the project report attached",
    "Your college exam timetable is available",
    "The team meeting starts at 2 PM",
    "Please submit your assignment before Friday",
    "Here are the notes from today's class",
    "Your interview is scheduled for Monday",
    "The project presentation will be held tomorrow"
]

# 1 = Phishing, 0 = Safe
labels = [
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0
]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    emails, labels, test_size=0.25, random_state=42
)

# Convert text into numbers
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Test model
prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)
matrix = confusion_matrix(y_test, prediction)

print("===== PHISHING EMAIL DETECTION =====")

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nConfusion Matrix:")
print(matrix)

# Test a new email
new_email = input("\nEnter an email message to check: ")

new_email_vector = vectorizer.transform([new_email])
result = model.predict(new_email_vector)

if result[0] == 1:
    print("\nResult: PHISHING EMAIL")
else:
    print("\nResult: SAFE EMAIL")
