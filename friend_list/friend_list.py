from random import randint


class SKE:
    def __init__(self, filename):
        self.friend_table = self.read_friend(filename)
        self.nickname_table = self.extract_nickname_list
        self.id_table = self.extract_id_lists


    @staticmethod
    def read_friend(filename):
        """
        Read file and convert to list
        :param filename:
        :return: list of friend information
        """
        lines = open(filename, encoding="utf8").read().splitlines()
        friend_list = [i.split() for i in lines]
        return friend_list


    @property
    def extract_nickname_list(self):
        """
        Extract friend_table to nickname list
        :return: list of friend nickname
        """
        return [self.friend_table[i][3] for i in range(len(self.friend_table))]


    @property
    def extract_id_lists(self):
        """
        Extract friend_table to KU ID list
        :return: list of friend KU ID
        """
        return [self.friend_table[i][0] for i in range(len(self.friend_table))]


    @staticmethod
    def read_nickname(member):
        """
        Enter friend nickname to list of nickname in group
        :param member: number of members
        :return: list of nickname of member in group
        """
        list_nickname = []
        for i in range(member):
            list_nickname.append(input(f"Enter Nickname member{i + 1}: "))
        return list_nickname


    @staticmethod
    def find_index(table, list_input):
        """
        Find index of friend_table and sort it
        :param table: list of friend information (such as nickname_table, id_table)
        :param list_input: list of information (such as nickname, id)
        :return: index of friend_table that match the list_input
        """
        table_index = []
        for i in list_input:
            for j in table:
                if i.lower() == j.lower() and table.index(j) not in table_index:
                    table_index.append(table.index(j))

        return sorted(table_index)


    def random_member(self, list_nickname_index, member):
        """
        Random members in group
        :param list_nickname_index: list of index of all member in group
        :param member: number of member
        """
        random_time = int(input("How many people: "))
        random_member_index = []
        while random_time > 0:
            random_index = randint(0, member - 1)
            if random_index in random_member_index:
                pass
            else:
                random_member_index.append(random_index)
                random_time -= 1
        for i in range(len(random_member_index)):
            print(f"{i + 1}:", *self.friend_table[list_nickname_index[random_member_index[i]]])


    def display_members(self, list_nickname_index):
        """
        Display all member in group
        :param list_nickname_index: list of index of all member in group
        """
        for i in list_nickname_index:
            print(*self.friend_table[i])


    def group_members(self):
        """
        input number of member and print it
        :return: number of member and list of index of all member in group
        """
        member = int(input("How Many people in a Group: "))
        list_nickname = self.read_nickname(member)
        list_nickname_index = self.find_index(self.nickname_table, list_nickname)
        print("Group members")
        self.display_members(list_nickname_index)
        return member, list_nickname_index


    def operate(self):
        print("1. Group")
        print("2. Person")
        choice_1 = int(input("Enter choice: "))
        if choice_1 == 1:
            member, list_nickname_index = self.group_members()
            print("1. Random members")
            print("2. Random work")
            choice_2 = int(input("Enter choice: "))
            if choice_2 == 1:
                self.random_member(list_nickname_index, member)
            # Random work currently updating
        elif choice_1 == 2:
            print("What do you have")
            print("1. Nickname")
            print("2. ID")
            choice_3 = int(input("Enter choice: "))
            if choice_3 == 1:
                nickname = [input("Enter Nickname: ")]
                self.display_members(self.find_index(self.nickname_table, nickname))
            elif choice_3 == 2:
                id_student = [input("Enter ID: ")]
                self.display_members(self.find_index(self.id_table, id_student))


def main():
    filename = "friend_list.txt"
    friend = SKE(filename)
    friend.operate()


if __name__ == '__main__':
    main()
