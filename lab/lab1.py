import random


def can_construct(word, letters):
    word = list(word)
    letters = list(letters)
    matching = 0
    for i in range(len(word)):
        for j in range(len(letters)):
            if word[i] == letters[j]:
                del letters[j]
                matching += 1
                break
    print(matching == len(word))

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        first = self.a * other.a
        outer = self.a * other.b
        inner = self.b * other.a
        last = self.b * other.b
        return Complex(first-last, outer + inner)

    def __repr__(self):
        info = f"{self.a} + {self.b}i"
        return info

    def __iadd__(self, other):
        self.a += other.a
        self.b += other.b


def create_permutation(n):
    temp = list(range(n))
    lst = []
    for i in range(len(temp)):
        rand = random.randint(0, len(temp)-1)
        lst.append(temp[rand])
        del temp[rand]
    print(lst)
    return lst


def scramble_word(word):
    order = create_permutation(len(word))
    scrambled_word = []
    for i in range(len(word)):
        scrambled_word.append(word[order[i]])
    finished = "".join([str(i) for i in scrambled_word])
    print(finished)
    return finished


def scramble_game(word):
    hint = scramble_word(word)
    print("Unscramble the word:", hint)
    guesses = 3
    for i in range(3, 0, -1):
        guess = input(f"You have {i} guesses left")
        if guess == word:
            print("Yay you got it!")
            break
        else:
            print("Wrong!")
    print("Nice try!")


can_construct("apple", "aplples")
create_permutation(10)
scramble_word("abcd")
#scramble_game("abcd")
cplx1 = Complex(5, 2)
print(cplx1)
cplx2 = Complex(3, 3)
print(cplx2)
print(cplx1 + cplx2)
print(cplx1 - cplx2)
print(cplx1 * cplx2)
print(cplx1)
print(cplx2)

