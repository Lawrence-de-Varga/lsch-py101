def sum(a, b):
    return a + b


def make_a_big_string(lst_of_strings):
    big_str = ''

    for str in lst_of_strings:
        big_str = big_str + str

    return big_str


def every_other(lst):
    index = 0

    new_lst = []
    for obj in lst:
        if index % 2 == 0:
            new_lst.append(obj)

        index += 1

    return new_lst


def index_of_third(str, char):
    index = 0
    count = 0

    for character in str:
        if character == char:
            count += 1
            index += 1
            if count == 3:
                return index
        else:
            index += 1

    return None
