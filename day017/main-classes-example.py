class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
# print(user_1.username)
user_2 = User("002", "jack")
# print(user_2.followers)

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)

## Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')
#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
