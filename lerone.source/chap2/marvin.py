paranoid_android = "Marvin"
letters = list(paranoid_android)
for char in letters:
    # print a tab concatenated with the current char
    print('\t'+ char)
    # comma is not doing concatenation, it is sending a tab followed by space then the char
    print('\t', char)