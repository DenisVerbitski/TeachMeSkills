def endless_fib_generator():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b
        
gen = endless_fib_generator()
for i in range(20):
    print(next(gen))
