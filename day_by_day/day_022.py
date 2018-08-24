with open('letter.txt', 'w') as letter:
    letter.write("Hi Bromley! \n"
                 "Can Flynn, Cassidy and I stop by for a tea this afternoon? \n"
                 "Cleon")


'''
letter= open('letter.txt', 'w')
try:
    letter.write("Hi Bromley! \n"
                 "Can Flynn, Cassidy and I stop by for a tea this afternoon? \n"
                 "Cleon")
finally:
    letter.close()
'''

# https://docs.python.org/3/library/threading.html#lock-objects
