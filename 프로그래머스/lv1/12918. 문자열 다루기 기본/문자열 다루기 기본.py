def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            new = int(s)
        except:
            return False
        
        else:
            return True
    else:
        return False