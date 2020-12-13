import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
bat
mat
pat
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'abc')

# # .: matches anything except newline
# pattern = re.compile(r'.')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'coreyms\.com')

# # \d: matches any digit (0-9)
# # \D: matches anything that is not a digit (0-9)
# pattern = re.compile(r'\d')
# pattern = re.compile(r'\D')

# # \w: word character (a-z,A-Z,0-9,_)
# # \W: not word character
# pattern = re.compile(r'\w')
# pattern = re.compile(r'\W')

# pattern = re.compile(r'\s')
# pattern = re.compile(r'\S')

# # \s: whitespace (space, tab, newline)
# # \S: not whitespace
# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'\BHa')

# # ^: begining of a string
# pattern = re.compile(r'^Start')
# pattern = re.compile(r'^tart')
# pattern = re.compile(r'^S')

# # $: end of a string
# pattern = re.compile(r'end$')
# pattern = re.compile(r'en$')
# pattern = re.compile(r'd$')

# # To search a phone no. e.g. - 321-555-4321
# # 123.555.1234
# # 123*555*1234
# # 800-555-1234
# # 900-555-1234
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# # character set []
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[^a-zA-Z]')
# pattern = re.compile(r'[^b]at')

# # Quantifiers
# # {some_number}: matches the exact number 
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# # ?: 0 or 1
# pattern = re.compile(r'Mr\.')
# pattern = re.compile(r'Mr\.?')

# # ?: 1 or more
# pattern = re.compile(r'Mr\.?\s[A-Z]\w+')

# # ?: 0 or more
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)
# matches = pattern.finditer(sentence)

# # pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# # pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# # matches = pattern.findall(text_to_search)

# # match is similar to ^
# # pattern = re.compile(r'Start')
# # pattern = re.compile(r'art')
# # matches = pattern.match(sentence)
# # print(matches)

# # pattern = re.compile(r'sentence')
# # pattern = re.compile(r'art')
# # pattern = re.compile(r'abc')
# # matches = pattern.search(sentence)
# # print(matches)

# # pattern = re.compile(r'start', re.IGNORECASE)
# # pattern = re.compile(r'start', re.I)
# # matches = pattern.search(sentence)
# # print(matches)

for match in matches:
    print(match)

# # To match pattern in a file
# with open('data.txt', 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)


#print(text_to_search[:4])