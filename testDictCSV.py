import itchat
import csv

itchat.login()

friends = itchat.get_friends(update=True)[0:]
total = len(friends[1:])
with open('names.csv', 'wb') as csvfile:
    fieldnames = ['Sex', 'NickName', 'Province', 'City', 'Signature']
    dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    dict_writer.writerow(fieldnames)
    dict_writer.writerows(friends)

