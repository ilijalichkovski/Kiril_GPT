vocab = set()

x = input('Name of the training file: ')
y = input('Name of the validation file: ')

with open(x, "r", encoding="utf-8") as data:
    text = data.read()
    characters = set(text)
    vocab.update(characters)

with open(y, "r", encoding="utf-8") as data:
    text = data.read()
    characters = set(text)
    vocab.update(characters)

print(vocab)

vocab_file = 'mk_vocab_1.txt'

with open(vocab_file, "w", encoding="utf-8") as vfile:
    for char in vocab:
        vfile.write(char + '\n')