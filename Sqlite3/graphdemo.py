from data import (
    run_data
)

def run():

    while (user_input:=input("What are you looking for: ")) != "quit":

        output = run_data(user_input)
        print(output)

if __name__ == "__main__":
    run()