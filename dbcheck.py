import json



def insert(d): 
    f1 = open('data.json' , 'r')  
    db = json.load(f1)
    db.append(d)
    f2 = open('data.json' , 'w')
    json.dump(db , f2)
    
    
def check(user):
    
    file = open('data.json') 
    db = json.load(file)
    found = False
    details = {}
    for x in db: 
        if x["user"] == user: 
            details = x
            found = True
            break
            
    if found: 
        return details 
    else:
        return -1 
        
        
def update_activity(username , activity):
    
    file = open('data.json' , 'r') 
    db = json.load(file)
    for x in db: 
        if x["user"] == username:
            x["activity"].append(activity) 
            
    f2=open('data.json' , 'w')
    json.dump(db , f2)  
    
def delete_activity(username , index):
    file = open('data.json' , 'r') 
    db = json.load(file)
    for x in db: 
        if x["user"] == username:
            c = x["activity"].pop((index - 1)) 
            break 
    f2=open('data.json' , 'w')
    json.dump(db , f2) 
        
    
if __name__ == '__main__': 
    print(check('prasad'))