import spoj_get_solved_prob
import sys
import getpass
def main():
    print("Please enter your SPOJ username :")
    username = input()
    print("Please enter your password :")
    password = getpass.getpass()
    spoj_get_solved_prob.getInfoAndDownload(username,password)

if __name__ == "__main__":
    main()