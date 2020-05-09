def alternative_choices(option):
    if option == 'r':
        option = 'rock'
    if option == 's':
        option = 'scissors'
    if option == 'p':
        option = 'paper'
    if option == 'y':
        option = 'yes'
    if option == 'n':
        option = 'no'
    return option


def valid_option(prompt, possibilities):
    while True:
        option = input().lower()
        option = alternative_choices(option)
        if option in possibilities:
            return option
        else:
            print(prompt)

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))