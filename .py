str=input("enter your string:")
def isPalindrome(str):

	# Run loop from 0 to len/2
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True


ans = isPalindrome(str)

if (ans):
	print("Palindrome")
else:
	print("Not Palindrome")
