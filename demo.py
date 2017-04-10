from pyparsing import Word, alphas

greeting_parser = Word(alphas) + "," + Word(alphas) + "!"
hello = "Hello, World!"
print hello, "->", greeting_parser.parseString(hello)
