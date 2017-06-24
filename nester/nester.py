""" The is the nester.py modules, and it provides one function called print_lol() which prints lists
that may or may not include nested lists"""


def print_nester(the_list):
    """ This function takes a positional arg. called "the_list", which is any
    Python list. Each data item in the provided list is (recursively) printed to the screen on its own line. """
    for list_item in the_list:
        if isinstance(list_item, list):
            print_nester(list_item)
        else:
            print(list_item)
