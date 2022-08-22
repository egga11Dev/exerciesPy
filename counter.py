counter_intern = 0
counter_exit = 0

while counter_exit <= 5:
    while counter_intern < 6:
        print(counter_exit, counter_intern)
        counter_intern += 1
    counter_exit += 1
    counter_intern = 0
