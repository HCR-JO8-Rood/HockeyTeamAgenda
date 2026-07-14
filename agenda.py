import pandas as pd

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTGp8rcr7o0yd45tCYMSgMBJcwUd_UBaKxhL-WHJ_6IZmvoZotlTfEELyJ3xSbwjqC5ajfQyKh19IeL/pub?output=csv"

df = pd.read_csv(CSV_URL)

print(df.head())
