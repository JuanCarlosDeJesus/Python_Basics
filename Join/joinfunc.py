# Join function for the Join module

# inefficient implementation of join function
words = ["Hello", "world", "this", "is", "a", "test"]

sentence = ""
for word in words:
    sentence += word + " "
sentence = sentence.strip()
print(sentence)

# using the built-in join function
sentence = " ".join(words)
print(sentence)