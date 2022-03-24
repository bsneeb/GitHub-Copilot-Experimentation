'''
Testing out the hash function using Copilot
'''


def hash_map(emails):  # O(n)
    """
    :param emails:
    :return:
    """
    email_map = {}
    for email in emails:
        if email not in email_map:
            email_map[email] = 1
        else:
            email_map[email] += 1
    return email_map


def hash_function(key):
    """
    :param key:
    :return:
    """
    total = 0
    for char in key:
        total += ord(char)
    return total % 37


# main method
if __name__ == '__main__':
    emails = ["bradyneeb@gmail.com", "bsneeb@gmail.com",
              "cwneeb@gmail.com", "msneeb@gmail.com"]

    # print(hash_map(emails))
    # print(hash_function(emails[1]))

    # loop to iterate emails
    for email in emails:
        hash_value = hash_function(email)
        print(hash_value)
