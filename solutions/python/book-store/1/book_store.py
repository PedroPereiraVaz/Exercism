def total(basket):

    book_price = 800
    discounts = {5:0.25, 4:0.2, 3:0.1, 2:0.05, 1:0}
    
    groups = []

    while basket:
        pack = set(basket)
        groups.append(len(pack))

        for book in pack:
            basket.remove(book)

    while 5 in groups and 3 in groups:
        groups.remove(5)
        groups.remove(3)
        groups.append(4)
        groups.append(4)

    ticket = 0
    for size in groups:
        ticket += (size * book_price) * (1 - discounts[size])
        

    return ticket
