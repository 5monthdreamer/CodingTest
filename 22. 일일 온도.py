
class condingtest:
    
    def test(self, T):    

        result = []
        n = 0
        
        for i, n in enumerate(T):
            
            date = 0
            while n+i < len(T) and T[n] < T[n+i]:
                date += 1
                i += 1
                break
                
            result.append(date)
            n += 1
            i = 1

            

        return print(result)




T = [73, 74, 75, 71, 69, 72, 76, 73]
a = condingtest()
a.test(T)
