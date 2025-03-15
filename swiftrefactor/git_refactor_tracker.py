import subprocess

"This file does the git commit refactoring analysis"

def get_git_diff():
    diff_output = subprocess.check_output(["git", "log", "--pretty=format:'%h - %an, %ar : %s'", "-10"], text=True)
    print("Recent Refactoring Commits:")
    print(diff_output)

if __name__ == "__main__":
    get_git_diff()