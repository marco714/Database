from database import connect
from database import create_table
from database import add_bean
from database import get_all_beans
from database import get_beans_by_name
from database import get_preparation_for_beans

MENU_PROMPT = """---Coffee Bean APP
1.) Add A New Bean
2.) See All Bean
3.) Find A Bean by Name
4.) See which preparation method is best for a bean
5.) Exit

Your Selection:"""

def menu():
    
    connection = connect()
    create_table(connection)
    user_input = input(MENU_PROMPT)
    while user_input != "5":

        if user_input == "1":
            name = input("Enter Bean Name: ")
            method = input("Enter How you've Prepared It: ")
            rating = int(input("Enter Your Rating Score: "))

            add_bean(connection, name, method, rating)
        elif user_input == "2":
            beans = get_all_beans(connection)

            for bean in beans:
                print(f"{bean[1]} {bean[2]} {bean[3]}")

        elif user_input == "3":
            name = input("Enter bean Name to find: ")
            beans = get_beans_by_name(connection, name)

            for bean in beans:
                print(f"{bean[1]} {bean[2]} {bean[3]}")
        elif user_input == "4":
            name = input("Enter Bean name to find: ")
            best_method = get_preparation_for_beans(connection, name)

            print(f"The Best Preparation method for {name} is: {best_method[2]}")
            
        user_input = input(MENU_PROMPT)
if __name__ == '__main__':
    menu()