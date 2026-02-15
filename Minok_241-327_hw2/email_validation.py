def fun(s):
    if s.count('@') != 1 or s.count('.') != 1:
        return False
    try:
        name = set(s.split('@')[0])
        site = set((s.split('@')[1]).split('.')[0])
        extension = (s.split('@')[1]).split('.')[1]
    except IndexError:
        return False

    if len(name) == 0 or len(site) == 0 or not(extension.isalpha()) or len(extension) > 3:
        return False

    for i in site:
        if not(i.isalpha()) and not(i.isdigit()):
            return False

    for i in name:
        if not(i.isalpha()) and not(i.isdigit()) and not(i in '-_'):
            return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
