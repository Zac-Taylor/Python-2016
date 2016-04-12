BOOK_TAX = .075
SHIPPING_OF_BOOKS = 2.0

values=[]

numOfBooks = input("How mamy books do you have:" + " ")
numBooks = int(numOfBooks)

for loop in range(numBooks):
    values.append(float(input("Enter vaule for book:" + " ")))

    mult =1
    for value in values:
        mult*=value

total_Costs = (numBooks * SHIPPING_OF_BOOKS) * mult * BOOK_TAX

print(total_Costs)
