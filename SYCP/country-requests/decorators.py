import time


def calculate_exec(function):
    def wrapper():

        initial_time = time.time()
        function()
        final_time = time.time()

        print(f"{function.__name__} Exec total time: {final_time - initial_time}")
    
    return wrapper


@calculate_exec
def main():
    print("Decorators in python")
    for index in range(1, 10000000):
        pass

main()
