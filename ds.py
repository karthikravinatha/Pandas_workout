#from __future__ import division
from collections import Counter
users = [   {	"id":	0,	"name":	"Hero"	},
           {	"id":	1,	"name":	"Dunn"	},
           {	"id":	2,	"name":	"Sue"	},
           {	"id":	3,	"name":	"Chi"	},
           {	"id":	4,	"name":	"Thor"	},
           {	"id":	5,	"name":	"Clive"	},
           {	"id":	6,	"name":	"Hicks"	},
           {	"id":	7,	"name":	"Devin"	},
           {	"id":	8,	"name":	"Kate"	},
           {	"id":	9,	"name":	"Klein"	} ]
friendships = [(0,	1),	(0,	2),	(1,	2),	(1,	3),	(2,	3),	(3,	4),
                     (4,5),	(5,	6),	(5,	7),	(6,	8),	(7,	8),	(8,	9)]
for user in users:
    user["friends"] = []
    #print(user)

for i,j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])
    #print(i,j)

def no_of_friends(user):
    return len(user["friends"])

total_connection = sum(no_of_friends(user)for user in users)
#print(total_connection)


no_users = len(user)
#print(no_users)
avg_connection = total_connection/no_users
no_of_friends_byid = [(user["id"],no_of_friends(user))for user in users]
print(no_of_friends_byid)
# a = sorted(no_of_friends_byid,
#         key = lambda (user_id:num_frd):num_frd,
#         reverse=True)

def friends_of_friend_bad(user):
    return [foaf["id"]
            for friend in user["friends"]
            for foaf in friend["friends"]
            ]

#print(friends_of_friend_bad(users[4]))
def not_same(user,other_user):
    return user["id"]!=other_user["id"]

def not_friend(user,other_user):
    return all(not_same(friend,other_user)
               for friend in user["friends"])
def friend_of_friend_id(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_same(user,foaf) and not_friend(user,foaf)
                   )
print(friend_of_friend_id(users[3]))
