
def romanToInt(s: str):
        values = {'I': 1, 
                  'V': 5, 
                  'X': 10, 
                  'L': 50, 
                  'C': 100, 
                  'D': 500, 
                  'M': 1000}
        total = 0

        for  i in range(len(s)-1):
            if values[s[i+1]] > values[s[i]]:
                total += values[s[i+1]] - values[s[i]]
                total -= values[s[i+1]]
            else:
                total += values[s[i]]
        
        print(total+values[s[-1]])
            

s = 'MCMXCIV'
romanToInt(s)