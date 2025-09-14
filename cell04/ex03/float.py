nb = input('Give me a number: ')

is_valid_format = False
temp_nb = nb

if temp_nb.startswith('-') or temp_nb.startswith('+'):
    temp_nb = temp_nb[1:]

if temp_nb.count('.') <= 1:
    if temp_nb.replace('.', '', 1).isdigit():
        is_valid_format = True

if is_valid_format:
    nb_f = float(nb)
    nb_i = int(nb_f)

    if nb_f == nb_i:
        print('This number is an integer.')
    else:
        print('This number is a decimal.')
else:
    print('Error: Input is not a valid number.')