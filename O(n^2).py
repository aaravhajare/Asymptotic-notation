
def print_n(n):

    iter = 0 

    for i in range(0,n):
        for j  in range (0 , n):
            print("*" , end= " ")
            iter+= 1
        print("")

print_n(10)
print_n(1)
print_n(6)
print("with every n time taken  = n^2")
