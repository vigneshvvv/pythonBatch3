class target:
    def test(*args):
        print(args)


obj = target()
obj.test(100,343,2232)