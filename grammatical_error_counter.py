import spacy
from grammarbot import GrammarBotClient

nlp = spacy.load('en')
def error_counter(msg_body):
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
		return "\n\nDue to high grammatical errors this job is probably fake"
	else:
	    return "\n\nDue to low grammatical errors this job is probably real"

print(error_counter("what is good"))
