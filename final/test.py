import instaloader
import pandas as pd
L = instaloader.Instaloader()

# Login or load session
username='param'
password ='param1'
L.login(username, password)        # (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)

# Print list of followers
f = []
count=0
for follower in profile.get_followers():
    f.append(follower.username)
    file = open("followers.txt","a+")
    file.write(f[count])
    file.write("\n")
    file.close()
    print(f[count])
    count=count+1
ss=[]
count=0
print('----------------------')
for i in f:
    p=instaloader.Profile.from_username(L.context, i)
    for j in p.get_followers():
        ss.append(j.username)
        file = open("followers_followers.txt","a+")
        file.write(ss[count])
        file.write("\n")
        file.close()
        print(ss[count])
        count=count+1
    print('------------------------')
f =pd.DataFrame(f)
f.to_csv('followers.csv')
ss=pd.DataFrame(ss) 
ss.to_csv('followers.csv')