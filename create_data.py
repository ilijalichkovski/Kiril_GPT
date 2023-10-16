from lxml import etree
import html
from bs4 import BeautifulSoup
import re
import random
import numpy as np

print('hello')

# path of the uncompressed wikipedia XML file
xml_file_path = "C:/Users/ilija/Downloads/mkwiki-20231001-pages-articles/mkwiki-20231001-pages-articles.xml"

num_articles_training = 1000
num_articles_validation = 200

# Parse the XML file
tree = etree.parse(xml_file_path)
root = tree.getroot()

rand_pos = random.randint(0, len(root))

decoded = test = etree.tostring(root[rand_pos], pretty_print=True).decode('utf-8')

print('index = ', rand_pos, '\n',  decoded)

'''
# create file with training data
training_indices = np.random.randint(0, len(root), num_articles_training)


with open('train_mk_2.txt', 'w') as f:

    for i in training_indices:

        # Get the text
        test = etree.tostring(root[i], pretty_print=True).decode('utf-8')

        if len(test) < 6000:
            pass
        else:
            # Use BS to parse the HTML
            soup = BeautifulSoup(test, 'html.parser')
            text_content = soup.get_text()
            text_content = html.unescape(text_content)

            # Removing <ref> and </ref>, {{ and }}, [[ and ]] 
            text_content = re.sub(r'<ref.*?>.*?</ref>', '', text_content)
            text_content = re.sub(r'\{\{(.*?)\}\}', r'', text_content)
            text_content = re.sub(r'\[\[(.*?)\]\]', r'\1', text_content)

            f.write(text_content)

# create file with validation data
validation_indices = np.random.randint(0, len(root), num_articles_validation)

with open('val_mk_2.txt', 'w') as f:

    for i in validation_indices:

        # Get the text
        test = etree.tostring(root[i], pretty_print=True).decode('utf-8')

        if len(test) < 6000:
            pass
        else:
            # Use BS to parse the HTML
            soup = BeautifulSoup(test, 'html.parser')
            text_content = soup.get_text()
            text_content = html.unescape(text_content)

            # Removing <ref> and </ref>, {{ and }}, [[ and ]] 
            text_content = re.sub(r'<ref.*?>.*?</ref>', '', text_content)
            text_content = re.sub(r'\{\{(.*?)\}\}', r'', text_content)
            text_content = re.sub(r'\[\[(.*?)\]\]', r'\1', text_content)

            f.write(text_content)

'''