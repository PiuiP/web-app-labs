def wrapper(f):
    def fun(l):                  
        l = [x[-10:] for x in l]    
        l = f(l)  
        formatted = []
        for num in l:
            formatted.append(f'+7 ({num[0:3]}) {num[3:6]}-{num[6:8]}-{num[8:10]}')
        return formatted
    return fun                

@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')
