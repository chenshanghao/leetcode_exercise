class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # quotient 商
        # denominator 余数
        # divmod return quotient, denominator
        sign = '-' if numerator * denominator < 0 else ''
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        if remainder == 0:
            return sign + str(quotient)
        result_list = [sign, str(quotient), '.']
        remainders = []
        while remainder not in remainders:
            remainders.append(remainder)
            quotient, remainder = divmod(remainder * 10, abs(denominator))
            result_list.append(str(quotient))
            
        idx = remainders.index(remainder)
        result_list.insert(idx + 3, '(')
        result_list.append(')')
        # Input 1 2, need replace (0) to ''
        result = ''.join(result_list).replace('(0)', '')
        return result