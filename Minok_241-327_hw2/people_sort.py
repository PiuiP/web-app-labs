import operator

def person_lister(f): #f = name_format
    def inner(people):
        res = sorted(people, key = lambda x: int(x[2]))
        if int(res[0][2]) < 0:
            return ['Математическая ошибка'] #если первый неотрцательные, то дальше тем более
        res = [f(res[i]) for i in range(len(people))]
        return res
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
