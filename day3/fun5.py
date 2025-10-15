def connect(**opcje):  # ** dowolna ilośc argumentów nazwanych (kwargs)
    print(opcje)


connect()  # {}
connect(a=7)  # {'a': 7}
connect(a=7, name="Radek")  # {'a': 7, 'name': 'Radek'}


def all_args(*args, **kwargs):
    print(f"{args=}")
    print(f"{kwargs=}")


all_args()
# args=()
# kwargs={}

all_args(1, 2, 3)
# args=(1, 2, 3)
# kwargs={}

all_args(b=1, c=2, x=3)
args = ()
kwargs = {'b': 1, 'c': 2, 'x': 3}

all_args(1, 2, name="radek")
# args=(1, 2)
# kwargs={'name': 'radek'}

# SyntaxError: positional argument follows keyword argument
# all_args(name="Radek", 1)
