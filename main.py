from transformers import pipeline
print("abc")
sentiment_analyser = pipeline("sentiment-analysis")
print("abc")
res = sentiment_analyser("I am happy")
print(res)
