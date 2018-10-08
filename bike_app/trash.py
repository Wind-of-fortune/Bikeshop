import uuid

def get_token():
    return str(uuid.uuid4())


print(get_token())

a = []
if a:
    print('a')
else:
    print('b')




