import matplotlib.pyplot as plt

# Example: Sentiment predictions for customer feedback
# Imagine you’re building a sentiment analysis system for customer feedback in a compliance-driven organization. 
# After running a simple AI model (like a logistic regression or even a pretrained sentiment classifier), you want to visualize the results for stakeholders.

# Let's say we processed 100 feedback entries
sentiment_counts = {
    "Positive": 50,
    "Neutral": 30,
    "Negative": 20
}

# --- Visualization 1: Bar chart for sentiment distribution --
plt.figure()
plt.bar(sentiment_counts.keys(), sentiment_counts.values(), color=['green', 'yellow', 'red'])
plt.title("Customer Feedback Sentiment Distribution")
plt.xlabel("Sentiment Category")
plt.ylabel("Number of Feedbacks")
plt.show()

# --- Visualization 2: Pie chart for stakeholder storytelling ---
plt.figure()
plt.pie(sentiment_counts.values(),
        labels=sentiment_counts.keys(),
        autopct='%1.1f%%',
        colors=['green', 'yellow', 'red']
    )
plt.title("Sentiment Breakdown (%)")
plt.show()

 