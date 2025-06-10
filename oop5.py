############ Q1 ############

def print_stars(n):
    print('*' * n)
print_stars(8)

############ Q2 ############

def count_char(a, word):
    return word.count(a)
print(count_char("a", "armenia"))

############ Q3 ############

def print_digits(num):
    for digit in str(num):
        print(digit, end= " ")
    print()

print_digits(527)

############ Q4 ############
def print_odd_digits(n):
    print(*[d for d in str(n) if int(d) % 2 == 1])

print_odd_digits(237421)

############ Q5 ############
def reverse_print(word):
    if word == "":
        return
    reverse_print(word[1:])
    print(word[0], end="")

reverse_print("laptop")
print()

