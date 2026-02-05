class Solution():
    
    def __init__(self, s, t):
        self.s=s
        self.t=t
         

    def isAnagram(self):
        
        if ((len(self.s)>=1 and len(self.s)<= 5e4) and (len(self.t) >=1 and len(self.t)<= 5e4)):

            s_sorted=sorted(self.s)
            print(s_sorted)
            t_sorted=sorted(self.t)
            print(t_sorted)

            if s_sorted==t_sorted:
                print("They are a valid anagram")

            else:
                print("They are not a valid anagram")

        else:
            print("invalid length")


sol1=Solution("triangle","integral")

sol1.isAnagram()


        

