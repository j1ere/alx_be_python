size = int(input("Enter the size of the pattern:"))

m = 0
while size > 0:
    
    
    the_size = size + m
    
    for n in range(1):
        print('*' * the_size, end="")
    print()
    size -= 1
    m += 1
    
