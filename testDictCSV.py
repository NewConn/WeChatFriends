import itchat
import csv
import codecs
import re

itchat.login()

friends = itchat.get_friends(update=True)[0:]
total = len(friends[1:])

# fieldnames = ['NickName', 'Sex', 'Province', 'City', 'Signature']
class friend():
    def __init__(self, fri):
        self.csvFrame = {}
        self.csvFrame['NickName'] = fri['NickName']
        sex = fri['Sex']
        if sex == 1:
            self.csvFrame['Sex'] = '男'
        elif sex == 2:
            self.csvFrame['Sex'] = '女'
        else:
            self.csvFrame['Sex'] = '未知'

        self.csvFrame['Province'] = fri['Province']
        self.csvFrame['City'] = fri['City']
        self.csvFrame['Signature'] = fri['Signature'].strip().replace("span", "").replace("class", "").replace("emoji", "")
        rep = re.compile("1f\d+\w|[<>/=]")
        self.csvFrame['Signature'] = rep.sub("", self.csvFrame['Signature'])

file = codecs.open('names.csv', 'w', 'gbk', 'ignore')
fieldnames = ['NickName', 'Sex', 'Province', 'City', 'Signature']
writer = csv.DictWriter(file, fieldnames=fieldnames)
writer.writeheader()
for fri in friends:
    member = friend(fri)
    writer.writerow(member.csvFrame)
file.close()

