import json
import os
choose=input("enter you want search or store team  (if you want store team choose (1) or you want search team choose (2) = ")
l=[]
d={}
maindict={}
if choose=="1":
    team_name=input("please inter your team name = ")
    member=int(input("how many members you want to add in your team"))
    project_name=input("enter your project name")
    technology=input("which technology you want to use in your project")
    time=input("how much time project will take")
    i=1
    list=[]
    while i<=member:
        member_name=input("inter your team member name = ")
        list.append(member_name)
        i+=1
    d["Team_name"]=team_name
    d["Members"]=member
    d["Team_members_name"]=list
    d["Project_name"]=project_name
    d["Technology"]=technology
    d["Time"]=time
    if os.path.exists('teamdetails.json')== True:
                myfile=open("teamdetails.json")
                opened_file=json.load(myfile)
                l=opened_file['team']
                l.append(d)
                maindict["team"]=l
                myfile=open("teamdetails.json","w")
                json.dump(maindict,myfile,indent=4)
                myfile.close()
    else:
        l.append(d)
        maindict["team"]=l
        myfile=open("teamdetails.json","w")
        json.dump(maindict,myfile,indent=4)
        myfile.close()
        b=maindict
elif choose=="2":
    team_name=input("enter your team name = ")
    with open("teamdetails.json","r") as x:
        team_info=json.load(x)
        flag=False
        for i in team_info["team"]:
            if i["Team_name"]==team_name :
                flag=True;
                print("teamname = ",i["Team_name"])
                print("Members = ",i["Members"])
                print("Team member name = ",i["Team_members_name"])
                print("project name = ",i["Project_name"])
                print("Technology = ",i["Technology"])
                print("Time = ",i["Time"])
                break
        if flag==False:
             print(" sorry! team name are Invalid please first store  your team profile information")

else:
    print("please choose only 1 or 2 ")
    