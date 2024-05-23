def you_are_balanced(algebra):
    dictionary_of_brackets = {']': '[', '}': '{', ')': '('}
    list_of_brackets = []

    for character in algebra:
        if character in dictionary_of_brackets.values():
            list_of_brackets.append(character)
        elif character in dictionary_of_brackets.keys():
            if list_of_brackets == [] or dictionary_of_brackets[character] != list_of_brackets.pop():
                return False
    if len(list_of_brackets) != 0:
        return False
    return True

def main():
    expression_one = "[(a+b)*t]"        # Balanced
    expression_two = "[{(a+b)*t} - y]"  # Balanced
    expression_three = "[(a+b)*t)"      # Not balanced
    expression_four = "[(a+b)"          # Not balanced
    expressions = [expression_one, expression_two, expression_three, expression_four]
    
    for expression in expressions:
        if you_are_balanced(expression):
            print(f"{expression} is balanced")
        else:
            print(f"{expression} is not balanced")

if __name__ == "__main__":
    main()
