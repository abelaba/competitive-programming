class Solution:
    def numberToWords(self, num: int) -> str:
        first = {0:'Zero', 1:'One',2:'Two',3:'Three',4:'Four', 5:'Five', 6:'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10:'Ten', 11: 'Eleven', 12: 'Twelve', 13:'Thirteen', 14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        second = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80:'Eighty', 90:'Ninety'}
        
        digits = len(str(num))
        string = ""
        
        if digits <=2 : 
            
            if num <= 19:
                string += first[num]
            
            elif 20 <= num:
                if num%10==0:
                    string += second[num]
                else:
                    string += second[(num//10)*10]+ ' ' + first[num%10]
        
        elif digits == 3: 
            if num%100 == 0:
                return first[num//100]+' '+ 'Hundred'
            string += first[num//100] + ' ' + 'Hundred' + ' ' + self.numberToWords(num-(num//100)*100)
        
        elif 4<=digits<=6: 
            if num%1000 == 0:
                return self.numberToWords(num//1000) + ' ' + 'Thousand'
            string += self.numberToWords(num//1000)+ ' ' + 'Thousand' + ' ' + self.numberToWords(num-(num//1000)*1000)
        
        elif 7<=digits<=9: 
            if num%1000000 == 0:
                return self.numberToWords(num//1000000)+' '+ 'Million'
            string += self.numberToWords(num//1000000)+ ' ' + 'Million' + ' ' + self.numberToWords(num-(num//1000000)*1000000)
        
        elif digits == 10: 
            if num%1000000000 == 0:
                return first[num//1000000000]+' '+'Billion'
            string += first[num//1000000000]+' '+ 'Billion' + ' '+ self.numberToWords(num-(num//1000000000)*1000000000)
        
        return string
