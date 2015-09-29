# SoftwareDesignFall15 Mini Project 1 Mimi Kome
The purpose of the NewsAlys project was to take the user's search term and retrieve articles for them on that topic, accompanied by some descriptors to help them decide which article would best meet their needs. 

I first built each of the basic functions of the program separately: one that runs a sentiment analysis of text, one that runs a mood analysis, one that retrieves search results from Google and returns the URL, one that returns the plaintext of whatever is found at a URL. I then pieced them together, streamlining as I went to reduce redundancies. 

NewAlys loops through a List of six news sites. It runs a site-specific google search for each news site plus the search term entered by the user. It passes the first result from each site to a plaintext function, which in turn passes the plain text to the analysis functions. It prints the analysis and article URL to the terminal, prefixed by "Here are some articles about (user's query)" and followed by a key to the analysis terms.

The functions I used that I did not build myself are from pattern; I used functions from pattern.web to grab search results and from pattern.en to analyse the text. 

In order to run NewsAlys from Python you enter "from NewsAlys import newsalys" which causes some instructions to print: "Thanks for opening NewsAlys. What would you like to search for? Please enter newsalys("your interest"). If you follow the prompt, a list of analysed links will appear, from which you can choose an article to read in-browser.

Here is an example of an interaction with NewsAlys:

>>> from NewsAlys import newsalys
Thanks for opening NewsAlys. What would you like to search for? Please enter newsalys("interest")
>>> newsalys("Quail")
Here are some articles about Quail
http://www.huffingtonpost.com/megan-quail/no-matter-who-wins-cancer_b_3225184.html
['Objective', 'Positive', 'conditional']
http://www.bbc.com/food/quail
['Objective', 'Neutral', 'conditional']
http://www.latimes.com/business/autos/la-fi-hy-pebble-beach-2015-rare-elegance-at-the-quail-20150815-story.html
['Objective', 'Positive', 'conditional']
http://www.nytimes.com/2012/10/03/dining/city-kitchen-quail-is-worth-a-second-thought.html
['Objective', 'Positive', 'conditional']
http://www.foxnews.com/recipe/rainier-cherry-maple-glazed-bandera-quail
['Objective', 'Positive', 'conditional']
http://www.cnn.com/2006/POLITICS/02/12/cheney/
['Objective', 'Positive', 'conditional']
Indicative means facts and beliefs. Imperative means commands and warnings. Conditional means conjectures. Subjunctive means wishes and opinions.


Reflection:
It was really useful to have made each of the pieces of the program as their own function. Debugging was much easier, and it was easy to put all the pieces together into the final "NewsAlys." In future versions of NewsAlys, I would like to use DuckDuckGo instead of Google. Google has a limited number of searches per day before you are charged, whereas DuckDuckGo has no such limit. Switching to DuckDuckGo is simply a matter of an update to Pattern.web to reflect the recent update to DuckDuckGo. I would also like to make the results more accessible. My hope is that NewsAlys will have a GUI someday, and that instead of lists of words it will return a more friendly translation of the analysis. A GUI would also make the services of this program more available to anyone who might want to use them. 
The project as-is felt appropriately scoped to me. Everything I did was new to me, which was really exciting. I wanted to do more, but realistically my next steps are above my level right now. I'm interested in continuing to work on this program as I learn more about Python. 
