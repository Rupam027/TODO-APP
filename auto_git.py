import os
import sys

if __name__ == '__main__':

    arg = sys.argv
    n = len(arg)
    if n == 3:
        print("hello")
        os.system('git add .')
        repo_type = arg[1]
        commit_message = arg[2]
        commit_command = 'git commit -m "' + commit_message + '"'
        print(commit_command)
        os.system(commit_message)
        if repo_type == '-g':
            os.system('git push')
    
            
            
              
    