class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def devide(self):
        return self.x / self.y
    def multi(self):
        return self.x * self.y

action = input("enter the quetion(between four main actions)\n(example: 2 * 3): ").replace(" ","")

run = 0
def Run():
    global run
    run = Calculator(float(num_x), float(num_y))

if "+" in action:
    num_x = action.rpartition("+")[0]
    num_y = action.rpartition("+")[2]
    Run()
    print(run.add())

elif "-" in action:
    num_x = action.rpartition("-")[0]
    num_y = action.rpartition("-")[2]
    Run()
    print(run.sub())

elif "/" in action:
    num_x = action.rpartition("/")[0]
    num_y = action.rpartition("/")[2]
    Run()
    print(run.devide())

elif "*" in action:
    num_x = action.rpartition("*")[0]
    num_y = action.rpartition("*")[2]
    Run()
    print(run.multi())

else:
    print("cant reconized")