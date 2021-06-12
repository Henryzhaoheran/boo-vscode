# Test output
box = 'too hot'
temp = 30 # unit celsius
book_price = 55.50 # unit RMB


# format output
'''
    ("string$s"$variable)
    %d integer
    %f float
'''
print("weather: %s"%box)
print("temperature is %sC"%temp)
print("the book price is: %fCNY"%book_price)
print("the book price is: %10.2fCNY"%book_price)
print("the book price is: %10.4fCNY"%book_price)
print("=============================")

# 3.multiple values output
print("weath: %s, temperature: %dC, Book Price: %f"%(box, temp, book_price))

print("=============================")
print("Wealth: {}, Temperature: {}C Book Price: {}".format(box, temp, book_price))


# 4更改结束符
print(box, end=", ")
print(temp, "c", end=", ")

