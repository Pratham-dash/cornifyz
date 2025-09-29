class Pallindrome:
    def reversed_string(self, s):
        s1=s[::-1]
        return s1
    
    def check_pallindrome(self, s):
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        if s==self.reversed_string(s):
            return True
        else:
            return False

    def main(self):
        user_input = input("Enter a string: ")
        print("your input is:", user_input)
        r=self.reversed_string(user_input)
        print("Reversed string is:", r)
        if self.check_pallindrome(user_input):
            print(f'"{user_input}" is a palindrome.')
        else:
            print(f'"{user_input}" is not a palindrome.')

    if __name__ == "__main__":
        main()    
       