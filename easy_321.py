
def add_user_data(n, a, u):
    user_data = "your name is {}, you are {}, and your username is {}" .format(n, a, u)
    print(user_data)
    with open("user.txt", "a") as f:
        f.write(user_data+'\n')

if __name__ == "__main__":
    name = input("name? ")
    age = input("age? ")
    u_reddit = input("reddit username? ")
    add_user_data(name, age, u_reddit)