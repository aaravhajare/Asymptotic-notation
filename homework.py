def sd(n) :

    for i in range(0,n+1):
        print("first loop")

    j = 1
    while (j<=n+1) :
        print("second loop")
        j = j*2

    for i in range(0,100) :
        print("third loop")

sd(15)
print("function above will take time")
print("Time taken  = O(n) + O(log n) + O(100)" )