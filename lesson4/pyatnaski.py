
field = list(range(15))

counter = 0
for i in field:
    counter += 1
    if counter % 4 == 0:
        end = '\n'
        sep = ''
    else:
        end = ''
        sep = '|'
    print(" {0:2} {1}".format(counter, sep), end=end)
