def print_diagnonally(a, ar, ac):
    i = 0
    j = 0
    down=False
    
    while i < ar-1 or j< ac-1:
        
        while down:
            print(a[i][j])
            
            if i + 1 < ar and j -1 >= 0:
                i += 1
                j -= 1
            else:
                down = False
                if i + 1 >= ar and j - 1 < 0:
                    j +=1
                elif i + 1 >= ar:
                    j +=1
                else:
                    i +=1
        
        while not down:
            print(a[i][j])
            
            if i - 1 >= 0 and j + 1 < ac:
                i -= 1
                j += 1
            else:
                down = True
                if i - 1 < 0 and j + 1 >= ac:
                    i +=1
                elif i - 1 < 0:
                    j +=1
                else:
                    i +=1

if __name__ == '__main__':
    
    ar = 4
    ac = 4
    a = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ]
    print_diagnonally(a, ar, ac)
