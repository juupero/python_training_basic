contacts = {}
result = []

n = int(input())

for i in range(n):
    query = input().split()
    if query[0] == 'add':
        _, number, name = query
        contacts.setdefault(name, tuple())
        contacts[name] += (number, )
    else:
        _, name = query
        if query[0] == 'del':
            contacts.pop(name, None)
        else:
            response = 'not found'
            if name in contacts:
                response = min(contacts[name])
            result.append(response)

print('\n'.join(result))