class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += "#" + str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []

        i = 1
        k = 2

        while i < len(s):
            while k < len(s) and s[k] != '#':
                k += 1
            
            numLen = s[i:k]
            print(numLen)
            i = k + int(numLen) + 1
            string = s[k+1:i]
            print(string)
            decoded.append(string)

            i += 1
            k = i+1

        return decoded


        

