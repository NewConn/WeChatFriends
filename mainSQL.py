import itchat
import sqlite3
import codecs
import re

itchat.login()

friends = itchat.get_friends(update=True)[0:]
total = len(friends[1:])
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table friends (nickname varchar(20) primary key, sex varchar(5), province varchar(10), city varchar(10), sign varchar(100))')

# fieldnames = ['NickName', 'Sex', 'Province', 'City', 'Signature']
class friend():
    def __init__(self, fri):
        NickName = fri['NickName']
        if fri['Sex'] == 1:
            Sex = '男'
        elif fri['Sex'] == 2:
            Sex = '女'
        else:
            Sex = '未知'

        Province = fri['Province']
        City = fri['City']
        Signature = fri['Signature'].strip().replace("span", "").replace("class", "").replace("emoji", "")
        rep = re.compile("1f\d+\w|[<>/=]")
        Signature = rep.sub("", self.Signature)


for fri in friends:
    member = friend(fri)
    cursor.execute('insert into friends (nickname, sex, province, city, sign) values (member.NickName, member.Sex, member.Province, member.City, member.Signature'))
cursor.close()
conn.commit()
conn.close()
