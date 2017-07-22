import itchat
import csv

itchat.login()


def getInfo():
    friends = itchat.get_friends(update=True)[0:]
    total = len(friends[1:])

    for friend in friends[1:]:
        sexnum = friend['Sex']
        nickname = friend['NickName']
        province = friend['Province']
        city = friend['City']
        signature = friend['Signature']
        if sexnum == 1:
            sex = "男"
        elif sex == 2:
            sex = "女"
        else:
            sex = "未知"

fieldnames = ['sexnum', 'nickname', 'province', 'city', 'signature']
dict_writer = csv.DictWriter(file('info.csv', 'wb'), fieldnames=fieldnames)
dict_writer.writerow(fieldnames)
dict_writer.writerows(friends)

