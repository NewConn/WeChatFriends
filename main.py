import itchat

itchat.login()

def getSex():
    friends = itchat.get_friends(update=True)[0:]
    male = female = other = 0
    for i in friends[1:]:
        sex = i['Sex']
        if sex == 1:
            male = male + 1
        elif sex == 2:
            female = female + 1
        else:
            other = other + 1

    total = len(friends[1:])
    print("男性：%.2f%%" %(float(male)/total*100) + "\n" + "女性：%.2f%%" %(float(female)/total*100) + "\n" + "不明性别：%.2f%%" %(float(other)/total*100) + "\n")

def getVar(friend):
    # var = []
    # sex = friend['Sex']
    # nickname = friend['NickName']
    # province = friend['province']
    # city = friend['city']




getSex()
