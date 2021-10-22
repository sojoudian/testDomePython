def symbolic_to_octal(perm_string):
    perms = {
    '---': '0',
    '--x': '1',
    '-w-': '2',
    '-wx': '3',
    'r--': '4',
    'r-x': '5',
    'rw-': '6',
    'rwx': '7'
    }

    return perms[perm_string[:-6]] + perms[perm_string[3:-3]] + perms[perm_string[6:]]