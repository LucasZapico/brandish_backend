import nltk.tokenize as nt
import nltk


text = 'Danish gummi bears ice cream cupcake jujubes sugar plum pastry icing. Fruitcake gingerbread muffin sweet liquorice chupa chups chocolate bar tart cupcake.'

tags = []

def tokenize(copy):
  ss=nt.sent_tokenize(copy)
  tokenized_sent=[nt.word_tokenize(sent) for sent in ss]
  pos_sentences=[nltk.pos_tag(sent) for sent in tokenized_sent]
  print(pos_sentences)
  for i in pos_sentences[0]: 
    tags.append(i[1])

  print(tags)
tokenize(text)