def check(assign, loc):
    if assign['c']!=-1 and assign['d']!=-1 :
        if assign['c']<assign['d'] :
            return False 
    
    if assign['d']!=-1 and assign['a']!=-1 :
        if assign['a']-assign['d']!=1 :
            return False
        
    if assign['d']!=-1 and assign['b']!=-1 :
        if abs(assign['d']-assign['b'])==1 :
            return False
        
    if assign['c']!=-1 :
        if assign['c']==3 :
            return False 
    
    if assign['b']!=-1 :
        if assign['b']==1 :
            return False 
        
    if loc in assign.values() :
        return False
    
    return True


def get_house(assign):
    for node in assign :
        if assign[node]==-1 :
            return node

def isGoal(assign):
    return check(assign,-1)


def backtrack(assign) :
    locs = [1,2,3,4]
    return rec_backtrack(assign, locs)
    


def rec_backtrack(assign, locs):
    if isGoal(assign) :
        return assign
    
    house = get_house(assign)

    for loc in locs :
        if check(assign, loc) :
            assign[house] = loc 
            res = rec_backtrack(assign, locs)
            if res :
                return res 
            assign[house] = -1
            
    return None
    

assign = {
    'a':-1,
    'b':-1,
    'c':-1,
    'd':-1
}

sol = backtrack(assign)

if sol:
    for node in sol:
        print('House :', node, '\tLocation :', sol[node])
else:
    print("No solution exists.")
