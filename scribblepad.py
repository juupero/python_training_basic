def fun(s):
    # return True if s is a valid email, else return False
    if '@' in s:
        words = s.split('@')
        if '.' in words[1]:
            website = words[1].split('.')
            print (website)
        print(words)


fun("juupero@gmail.com")
# def filter_mail(emails):
#     return list(filter(fun, emails))

# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for _ in range(n):
#         emails.append(input())

# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)
