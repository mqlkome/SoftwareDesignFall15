from pattern.web import *
from pattern.en import *
#Loopsites takes a user-inputted word, creates a gsearch query for each site, and runs gsearch on each query. 
#It gives the URL from gsearch to artext, which grabs the plaintext article from that URL. 
#Then, it loops through the articles from artext, and runs sentmood on each of them.
#Finally, it puts the analysis somewhere pretty. 
def loopsites(userin):
     sites = ["www.huffingtonpost.com", "www.bbc.com", "www.latimes.com", "www.nytimes.com", "www.foxnews.com", "www.cnn.com"]
     print "Here are some articles about " + userin
     for site in sites:
          url = gsearch("site:" + site + " " + userin) 
          article = artext(url) 
          analysis = sentmood(article)
          print url
          print analysis

##The functions gsearch and artext are here to search for userinput on the web and process the search results into something that can be analysed.
# gsearch is directed to run a google search of a news site and return the url of the first article on userinput. 
def gsearch(query):
     g = Google()
     return g.search(query)[0].url


# loopsites provides a url(from gsearch) and artext makes a string: the plaintext of the article at the URL.
def artext(url):
     article = URL(url).download()
     plain = plaintext(article)
     return plain

##Below are the functions that perform the analysis of the plaintext of the articles.
## They analyse the subjectivity and mood of each article and return descriptive words.
##Sentmood uses positivity and subjectivity to turn sentiment and mood analysis into user-friendly descriptors. 
def sentmood(article):            
     sent = sentiment(article) ## Will return a tuple, (polarity, subjectivity)
     subj = subjectivity(sent[1])
     pos = positivity(sent[0])
     atti = mood(article) ## will return a string which indicates the grammatical mood (indicative, imperative, conditional, subjunctive)

     return [subj, pos, atti]

def positivity(sent0):
     if 0.1 <= sent0 <= 1:
          return "Positive"
     elif -0.1 < sent0 < 0.1:
          return "Neutral"
     elif -1 <= sent0 <= -0.1:
          return "Negative"
     else:
          return

def subjectivity(sent1):
     if 0 <= sent1 < .5:
          return "Objective"
     elif .5 <= sent1 <=1:
          return "Subjective"
     else:
          return

	
print "Indicative means facts and beliefs. Imperative means commands and warnings. Conditional means conjectures. Subjunctive means wishes and opinions."
	

