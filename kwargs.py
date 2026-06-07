def display(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


def combine(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == "__main__":
    display(name = "vignesh", dept = "SW")
    combine(10,20, name = "vignesh", dept = "SW")

