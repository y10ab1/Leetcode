class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        Ori_palindrome = palindrome
        if len(palindrome) == 1:
            return ''
        for idx, c in enumerate(palindrome):
            if c!='a' and (idx+1)*2-1!=len(Ori_palindrome):
                palindrome = palindrome[:idx]+'a'+palindrome[idx+1:]
                print(Ori_palindrome)
                if palindrome != Ori_palindrome:
                    return palindrome
            elif idx==len(Ori_palindrome)-1:
                palindrome = palindrome[:-1] + 'b'
                if palindrome != Ori_palindrome:
                    return palindrome
        
        
        
        