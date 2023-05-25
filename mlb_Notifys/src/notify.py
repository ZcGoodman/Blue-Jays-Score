"""
-------------------------------------------------------
[This program will give your windows computer a notification of the Blue Jays score everytime the Jyas score a run. For example
if the jays score a run it will notifiy you and say Blue jays score 1-0 or 4-5. Jays score will always come up on the left]
-------------------------------------------------------
Author: Zachary Goodman 
-------------------------------------------------------
"""
from win10toast import ToastNotifier

toaster = ToastNotifier()

import statsapi

 
team_id=[]
h_or_a=""
opponet=""
score=0
oScore=0

team=statsapi.lookup_team('tor')
      
for id_ in team:
    team_id.append(id_["id"])
    
id= team_id[0]

s=statsapi.schedule(date=None, start_date=None, end_date=None, team=id, opponent="", sportId=1, game_id=None)

while (s[0]["status"]!="Final"):
    s=statsapi.schedule(date=None, start_date=None, end_date=None, team=id, opponent="", sportId=1, game_id=None)
    if (s[0]["venue_name"]=="Rogers Centre"):
         h_or_a="home_score"
         opponet="away_score"
    

    else:
        h_or_a="away_score"
        opponet="home_score"
        
    inning= s[0]["current_inning"]
    state= s[0]["inning_state"]
    oScore=s[0][opponet]
    if (s[0][h_or_a]>score):
        score=s[0][h_or_a]
        message= f"Blue Jays socre is {score}-{oScore} in the {state} of the {inning}"
        toaster.show_toast("Blue Jays",message,duration=5)
        
s=statsapi.schedule(date=None, start_date=None, end_date=None, team=id, opponent="", sportId=1, game_id=None)
if (s[0]["venue_name"]=="Rogers Centre"):
    h_or_a="home_score"
    opponet="away_score"
    

else:
    h_or_a="away_score"
    opponet="home_score"
score=s[0][h_or_a]
oScore=s[0][opponet]

if (score>oScore):
    message= f"Blue Jays won {score}-{oScore}"
    toaster.show_toast("Blue Jays",message,duration=5)
else:
    message= f"Blue Jays lost {oScore}-{score}"
    toaster.show_toast("Blue Jays",message,duration=5)
    
