import random, sys, doctest

class SKE:
    def __init__(self, filename):
        self.friend_table = self.read_friend(filename)
        self.nickname_table = self.extract_nickname_list(self.friend_table)
        self.id_table = self.extract_id_lists(self.friend_table)



    @staticmethod
    def read_friend(filename):
        lines = open(filename, encoding="utf8").read().splitlines()
        friend_list = [i.split() for i in lines]
        return friend_list


    def extract_nickname_list(self):
        return [self.friend_table[i][3] for i in range(len(self.friend_table))]

    def extract_id_lists(self):
        return [self.friend_table[i][0] for i in range(len(self.friend_table))]



    def read_nickname(self, member):
        list_nickname = []
        for i in range(member):
            list_nickname.append(input(f"Enter Nickname member{i + 1}: "))
        return list_nickname


    def find_index(self, table, list_input):
        list_nickname_index = []
        for i in list_input:
            for j in table:
                if i.lower() == j.lower() and table.index(j) not in list_nickname_index:
                    list_nickname_index.append(table.index(j))
                    break
        return sorted(list_nickname_index)


    def random_member(self, list_nickname_index, member):
        random_time = int(input("How many people: "))
        random_member_index = []
        while random_time > 0:
            random_index = random.randint(0, member - 1)
            if random_index in random_member_index:
                pass
            else:
                random_member_index.append(random_index)
                random_time -= 1
        for i in range(len(random_member_index)):
            print(f"{i + 1}:", *self.friend_table[list_nickname_index[random_member_index[i]]])


    def display_members(self, list_nickname_index):
        for i in list_nickname_index:
            print(*self.friend_table[i])


    def group_members(self, nickname_table):
        member = int(input("How Many people in a Group: "))
        list_nickname = self.ead_nickname(member)
        list_nickname_index = self.find_index(nickname_table, list_nickname)
        print("Group members")
        self.display_members(self.friend_table, list_nickname_index)
        if input("Random members? y/n: ").lower() == "y":
            self.random_member(self.friend_table, list_nickname_index, member)


    def operate(self, id_table):
        print("1. Group")
        print("2. Person")
        choice_1 = int(input("Enter choice: "))
        if choice_1 == 1:
            self.group_members(self.friend_table, self.nickname_table)
        elif choice_1 == 2:
            print("What do you have")
            print("1. Nickname")
            print("2. ID")
            choice_2 = int(input("Enter choice: "))
            if choice_2 == 1:
                nickname = [input("Enter Nickname: ")]
                self.display_members(self.friend_table, self.find_index(self.nickname_table, nickname))
            elif choice_2 == 2:
                id_student = [input("Enter ID: ")]
                self.display_members(self.friend_table, self.find_index(id_table, id_student))


    # friend_table = read_file(filename)
    # # print(friend_table)
    # nickname_table = extract_nickname_lists(friend_table)
    # id_table = extract_id_lists(friend_table)
    # # print(nickname_table)
    # # print(id_table)
    # operate(friend_table, nickname_table, id_table)

if __name__ == '__main__':
    doctest.testmod()
    filename = "friend_list.txt"
    friend = SKE(filename)
