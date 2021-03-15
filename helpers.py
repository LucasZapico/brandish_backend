import urllib.request, urllib.parse, urllib.error
import nltk
import re
from bs4 import BeautifulSoup



# get the copy from a given url 
# tokenize the content using nlp 
# return ajetives 

# tags = ["JJ", "NN", "NNS", "RBR", "RBS", "VBN","NPP", "NNP"]
tags = ['NNP']
tags_danish = ['JJ', 'NN', 'NNS', 'VBP', 'NNS', 'VB', 'NNS', 'VB', 'NNS', 'NN', 'NN']


def url_set_to_scrape(base_url):
  # store of previously searched urls
  searched = []
  # get domain url : https://example.com/page/100 -> https://example.com
  domain = re.findall(r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}', base_url)
  print('test',domain)
  get_links(base_url, domain[0])



def get_links(url, domain_url):
    links_on_page = []
    markup = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(markup, 'html.parser')
    


    tags = soup('a')
    print(tags[:5])
    for tag in tags: 
      if domain_url in tag: 
        links_on_page.append(tag)
    print(links_on_page)

# get site markup
def get_site_markup(url):
  markup = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(markup, 'html.parser')
  # remove header and footer copy as it doesn't have brandish copy
  # todo remove tags that have footer 
  if(soup.find('footer') != None):
    soup.find('footer').decompose()
  if(soup.find('header') != None):
    soup.find('header').decompose()  
  
  # tags = soup(['h1','h2', 'h3', 'h4', 'h5', 'p', 'a'])
  copy = soup.get_text(' ', strip=True)
  return copy


social = ['email', 'facebook', 'instagram']
business = ['subscribe', 'login','menu', 'wishlist','faq','connect', 'account', 'company','tweet', 'checkout', 'free', 'total', 'payments', 'customer', 'cart','buy', 'policy', 'return', 'sale', 'customerservice', 'shipping', 'chat', 'purchase', 'privacy', 'inc', 'ordering']
dev = ['error', 'submit', 'sitemap']

def clean_copy(copy):
  
  clean_copy = re.sub(r'[^a-zA-Z\s]',' ', copy)
  for w in social: 
    clean_copy = re.sub(w,' ', clean_copy, flags=re.IGNORECASE)
  for w in business:
    clean_copy = re.sub(w,' ', clean_copy, flags=re.IGNORECASE)
  for w in dev:
    clean_copy = re.sub(w,' ', clean_copy, flags=re.IGNORECASE)
  
  return clean_copy

# take copy and create token key 
def tokenize(copy):
  ss=nltk.sent_tokenize(copy)
  tokenized_sent=[nltk.word_tokenize(sent) for sent in ss]
  pos_sentences=[nltk.pos_tag(sent) for sent in tokenized_sent]
  
  return pos_sentences
  

# match tokenized copy to defined set tokens
def match_tokens(token_array, nltk_selection_set = ['NNP']):
  copy_set = set()
  
  for token_set in token_array: 
    for token in token_set: 
      if token[1] in nltk_selection_set:
        word = token[0].strip().lower()
        copy_set.add(word)
  copy = list(copy_set)
  return copy


def make_para(copy, para_size, number_para):
  copyArr = copy.split(' ')
  para_size = int(para_size)
  number_para = int(number_para)
  total = number_para * para_size
  paras = []
  if(len(copyArr) > total):
    para = 0
    for i in range(number_para):
      paras.append(copyArr[para: para + para_size])
      para = para + para_size
      print(paras)
    for p in range(len(paras)): 
      paras[p] = ' '.join(paras[p])
    return paras
  else:
    # create enough copy
    while total > len(copyArr): 
      print('copy', len(copyArr))
      print('tot',total)
      copyArr = copyArr + copyArr
    # parse into number of paragraphs of defined length
    para = 0
    for i in range(number_para):
      paras.append(copyArr[para: para + para_size])
      para = para + para_size
    for p in range(len(paras)): 
      paras[p] = ' '.join(paras[p])
    return paras


drop_words = ['shipping', 'payments', 'contact', 'login', 'orders', 'total', 'account', 'sales', 'customer', 'faq', 'privacy', 'policy']