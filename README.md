# Brandish Ipsum 

## Todo

- handle forbidden error and other server side errors 
- randomize the copy more
- add 'conjunction' and 'articles'
- dynmaicly remove brand name
- save current set of ipsum 
- 
### Dev Notes 

#### Python Env 

```bash 
source ./env/bin/activate
```

#### auto update requirements.txt 

```shell
pip install pipreqs
```

#### Push to Heroku 

```shell 
git push heroku master
```

### Dev Journal 

#### Challenges 

- attempted deploy on deta, PythonforEveryone, and, heroku
- hosting platforms and nltk 
  - solution: nltk.txt
- flask and hosting platforms (herok)
  - gunicorn (not sure why this solved the deployment failure)
- cors errors WIP 
- 
#### NLP (Natural Language Processing Token table)

|      |                                                                          |
|------|--------------------------------------------------------------------------|
| CC   | coordinating conjunction                                                 |
| CD   | cardinal digit                                                           |
| DT   | determiner                                                               |
| EX   | existential there (like: "there is" ... think of it like "there exists") |
| FW   | foreign word                                                             |
| IN   | preposition/subordinating conjunction                                    |
| JJ   | adjective    'big'                                                       |
| JJR  | adjective, comparative    'bigger'                                       |
| JJS  | adjective, superlative    'biggest'                                      |
| LS   | List marker    1)                                                        |
| MD   | modal    could, will                                                     |
| NN   | noun, singular 'desk'                                                    |
| NNS  | noun plural    'desks'                                                   |
| NNP  | proper noun, singular    'Harrison'                                      |
| NNPS | proper noun, plural    'Americans'                                       |
| PDT  | predeterminer    'all the kids'                                          |
| POS  | possessive ending    parent's                                            |
| PRP  | personal pronoun    I, he, she                                           |
| PRP$ | possessive pronoun    my, his, hers                                      |
| RB   | adverb    very, silently,                                                |
| RBR  | adverb, comparative    better                                            |
| RBS  | Adverb, superlative    best                                              |
| RP   | particle    give up                                                      |
| TO   | to go 'to' the store.                                                    |
| UH   | interjection    errrrrrrrm                                               |
| VB   | Verb, base form    take                                                  |
| VBD  | verb, past tense, took                                                   |
| VBG  | Verb, gerund/present participle    taking                                |
| VBN  | verb, past participle taken                                              |
| VBP  | verb, sing. present, non-3d    take                                      |
| VBZ  | verb, 3rd person sing. present    takes                                  |
| WDT  | wh-determiner  which                                                     |
| WP   | wh-pronoun    who, what                                                  |
| WP$  | possessive wh-pronoun    whose                                           |
| WRB  | wh-adverb    where, when                                                 |
