def print_snake_fashion(a, ar, ac):
    i = 0
    j = 0
    n = 0
    while n < ar * ac:
        
        if i%2 == 0:
            si = 0
            ei = ac
            ss = 1
        else:
            si = ac -1
            ei = -1
            ss = -1
        
        for j in range(si, ei, ss):
            n +=1
            print(a[i][j])
        
        i +=1

if __name__ == '__main__':
    
    ar = 4
    ac = 3
    a = [
            [1, 2, 3],
            [5, 4, 6],
            [7, 8, 9],
            [10, 11, 12]
        ]
    print_snake_fashion(a, ar, ac)
                    
                
        
