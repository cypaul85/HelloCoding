voted = {}
def check_voter(name):
    if voted.get(name):
        print("kick {} out".format(name))
    else:
        voted[name] = True
        print("Let {} vote".format(name))

check_voter("tom")
check_voter("mike")
check_voter("mike")
check_voter("John")
print(voted)
