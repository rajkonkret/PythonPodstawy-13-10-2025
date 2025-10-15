def connect(**opcje):  # ** dowolna ilośc argumentów nazwanych (kwargs)
    print(opcje)


connect()  # {}
connect(a=7)  # {'a': 7}
connect(a=7, name="Radek")  # {'a': 7, 'name': 'Radek'}
