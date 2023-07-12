import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

'''Similarities between cat, monkey and banana:
 -"cat" and "monkey" have a similarity score of 0.5265434598064423, which suggests that they share some common attributes
 or features, but they are not highly similar, this makes sense because they are both animals though of different species.
 -"banana" has a higher similarity score (0.5397804374427795) with "monkey" compared to "cat." This implies that bananas and
   monkeys may have more shared characteristics or associations in terms of their contexts or attributes.
   This could be due to the fact that monkeys are naturally known to be lovers of bananas.'''

'''As an example of my own, I would consider "car" and "bicycle". I would assume that if we calculate their similarity using word vectors,
 we would expect a moderate similarity score since both are modes of transportationalthough they differ in terms of 
 their structure, functionality, and purpose. The similarity score would likely indicate that they have some shared features,
 but they are distinct enough to have a noticeable difference.'''

#example.py
'''The 'en_core_web_sm' model is a smaller and simpler version of the language model compared to 'en_core_web_md', which means it may have less
   nuanced word representations and may not perform as well in capturing the fine-grained semantic similarities between texts.'''