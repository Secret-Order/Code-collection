import random, sys, doctest


def read_file(filename):
    lines = open(filename, encoding="utf8").read().splitlines()
    friend_list = [i.split() for i in lines]
    return friend_list


def extract_nickname_lists(friend_table):
    nickname_table = []
    for i in range(len(friend_table)):
        nickname_table.append(friend_table[i][3])
    return nickname_table


def read_nickname(member):
    list_nickname = []
    for i in range(member):
        list_nickname.append(input(f"Enter Nickname member{i + 1}: "))
    return list_nickname


def nickname_index(nickname_table, list_nickname):
    list_nickname_index = []
    for i in list_nickname:
        for j in nickname_table:
            if i.lower() == j.lower():
                list_nickname_index.append(nickname_table.index(j))
                break
    return sorted(list_nickname_index)


def display_members(friend_table, list_nickname_index):
    print("Group members:")
    for i in list_nickname_index:
        print(*friend_table[i])


def operate(friend_table, list_nickname_index, member, choice):
    if choice == 1:  #random member
        random_time = int(input("How many people: "))
        random_member_index = []
        while random_time > 0:
            random_index = random.randint(0, member-1)
            if random_index in random_member_index:
                pass
            else:
                random_member_index.append(random_index)
                random_time -= 1
        for i in range(len(random_member_index)):
            print(i+1)
            print(*friend_table[list_nickname_index[random_member_index[i]]])
    else:  #exit
        print("Bye")
        sys.exit()


def main():
    filename = "friend_list.txt"
    friend_table = read_file(filename)
    # print(friend_table)
    nickname_table = extract_nickname_lists(friend_table)
    # print(nickname_table)

    member = int(input("How Many people in a Group: "))
    list_nickname = read_nickname(member)
    list_nickname_index = nickname_index(nickname_table, list_nickname)
    display_members(friend_table, list_nickname_index)

    print("0. exit")
    print("1. random")
    choice = int(input("Enter choice: "))
    operate(friend_table, list_nickname_index, member, choice)


if __name__ == '__main__':
    doctest.testmod()
    main()
