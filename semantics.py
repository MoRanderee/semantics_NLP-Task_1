import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("\nWord comparison:\n")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
"""
cat is almost 60% similar to monkey as these are both animals and nouns.
monkey is 40% similar to banana and monkeys are often linked to bananas.
cat and banana are just 22% similar as a cat and banana dont have much in common.
"""

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("\nSentence comparison:\n")
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
