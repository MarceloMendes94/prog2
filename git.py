import sys
import os
def main():
	if len(sys.argv) == 2:
		text = sys.argv[1]
		os.system("git add .")
		#text = input("mensagem: ")
		os.system("git commit -m "+ text)
		os.system("git push")
	else:
		print("argumento MENSAGEM não foi digitado")
	return 0

if __name__ == '__main__':
	main()

