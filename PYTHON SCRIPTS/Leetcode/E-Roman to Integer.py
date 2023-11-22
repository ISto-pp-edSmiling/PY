class Solution:
    def romanToInt(self, s: str) -> int:
            s=s.replace('CM', '900.')
            s=s.replace('CD', '400.') 
            s=s.replace('XC', '90.')
            s=s.replace('XL', '40.')
            s=s.replace('IX', '9.')
            s=s.replace('IV', '4.')
            s=s.replace('M', '1000.')
            s=s.replace('D', '500.')
            s=s.replace('C', '100.')
            s=s.replace('L', '50.')
            s=s.replace('X', '10.')
            s=s.replace('V', '5.')
            s=s.replace('III', '3.')
            s=s.replace('II', '2.')
            s=s.replace('I', '1.')
            m = s.split('.')
            n = []
            for me in m:
                if not me == '':
                    n.append(int(me))
            return(sum(n))
        
# funny r code fr