import spacy
from grammarbot import GrammarBotClient

nlp = spacy.load('en')

msg_body = input("Enter the body of the message: ")
tokens = nlp(msg_body)
err_count = 0
for sent in tokens.sents:
    x = sent.string.strip()
    #print(x)
    client = GrammarBotClient()
    res = client.check(x, 'en-GB')
    if len(res.matches) > 0:
      #print(res.matches)
      err_count += 1
if err_count > 5:
  print("\n\nThis job is probably fake")
