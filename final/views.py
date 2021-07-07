from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import instaloader
import os
L = instaloader.Instaloader()
def button(request):
    
    return render(request,'home.html')
def add(request):
    username=request.GET['u']
    password=request.GET['p']
    L.login(username, password)        # (login)


    # Obtain profile metadata
    profile = instaloader.Profile.from_username(L.context, username)

    # Print list of followers
    try:
    #Print list of followers
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
        df=pd.DataFrame(f)
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
            df1=pd.DataFrame(f)
            print()
            print('------------------------')
    except:
        print('end')
    d=pd.concat([df,df1], axis=1)
    res=d
    return render(request,'form.html',{"res":res})