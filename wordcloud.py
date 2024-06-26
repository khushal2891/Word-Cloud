import sys
import numpy as np
from PIL import Image
import wikipedia  # to extract information
from wordcloud import WordCloud, STOPWORDS

# We will import STOPWORDS to remove common words
a = str(input("Enter the name of which you want to make word cloud: "))

# Search for the title from Wikipedia
title = wikipedia.search(a)[0]

# Search the page related to the given topic on Wikipedia
page = wikipedia.page(title)

# Extract the content of that topic
text = page.content
print(text)

bg = np.array(Image.open("abcd.jpg"))

# Set of unwanted words
unwanted_words = set(STOPWORDS)

# Generate word cloud
wordcloud = WordCloud(background_color="black", max_words=400, mask=bg, stopwords=unwanted_words)
wordcloud.generate(text)

# Save the word cloud
wordcloud.to_file("sample.png")