import basic 

while True:
    text = input('basic > ')
    print('text:', text)
    result, error = basic.run(text)

    if error: print(error.as_string())
    else: print(result)