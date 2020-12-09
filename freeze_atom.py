import sys

freeze_atom_list = ['C', 'N', 'O']
while True:
    try:
        input_line = input()
        line = ''
        s = input_line.split()
        if not s:
            print()
            continue
        if s[0] in freeze_atom_list:
            line += s[0] + '\t' + '-1' + '\t'
            line += '\t'.join(s[1:])
            print(line)
        else:
            print(input_line)

    except EOFError:
        break
