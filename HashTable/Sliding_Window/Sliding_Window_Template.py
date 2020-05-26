import collections
def slidingWindowTemplateByHarryChaoyangHe(sstr, tstr):
    #init a collection or int value to save the result according the question.
    result = []
    if len(sstr)<len(tstr):
        return result
        
    #create a hashmap to save the Characters of the target substring.
    #(K, V) = (Character, Frequence of the Characters)
    count_dict = collections.Counter(tstr)
        
    #maintain a counter to check whether match the target string.
    counter = len(count_dict)#must be the map size, NOT the string size because the char may be duplicate.
        
    #Two Pointers: begin - left pointer of the window; end - right pointer of the window
    begin, end = 0, 0
        
    #the length of the substring which match the target string.
    len_ = int('inf'); 
        
    #loop at the begining of the source string
    while(end < len(sstr))
            
        #get current looping character
        c = sstr[end]
        if c in count_dict:
            count_dict[c] -= 1
            if count_dict[c]==0: #this character already matched
                counter -= 1 #[*] modify the counter according the requirement(different condition).
            
        end += 1
            
        #increase begin pointer to make it invalid/valid again
        while(counter == 0): # [*] modify the counter condition according to different question

            c_ = sstr[begin] #***be careful here: choose the char at begin pointer, NOT the end pointer
            if c_ in count_dict:
                count_dict[c_] += 1 #[*] plus or minus one according to the question
                if count_dict[c_]>0:
                    counter += 1  #[*] modify the counter according the requirement (different condition).
                
            # [*] modify here
            # save / update(min/max) the result if find a target
            # result collections or result int value
            # ....
            # ....

            begin += 1
        
    return result
