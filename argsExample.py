class Employee:

    def details(self, *args):

        if len(args) == 1:
            print("Name: ", args[0])
        elif len(args) == 2:
            print("Name: ", args[0])
            print("salary: ", args[1])
        elif len(args) == 3:
            print("Name: ", args[0])
            print("salary: ", args[1])
            print("Dep: ", args[2])


obj = Employee()
obj.details("vignesh", 30000)

