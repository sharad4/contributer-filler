import subprocess
import datetime
import random
import os

def backdate_commit(days_back=90):
    commit_message = [
        "Fix bug in the main function",
        "Update documentation",
        "Refactor code for better readability",
        "Add error handling",
        "Imporove performance of data processing",
        "Update dependencies",
        "Fix typo in comments",
        "Add new feature",
        "Remove dead code",
        "Update README file",
        "Improve algorithm efficiency",
        "Add unit tests",
        "Code cleanup",
        "Bug fix for edge case"
    ]

    file_extensions = ['.py', '.js', '.txt', '.md', '.json', '.yml']

    base_date = datetime.datetime.now() - datetime.timedelta(days=days_back)

    for i in range(days_back):
        current_date = base_date + datetime.timedelta(days=i)

        if current_date.weekday() >= 5 and random.random() < 0.6:
            continue

        if random.random() < 0.15:
            continue

        num_commits = random.choices([1, 2, 3], weights=[0.7, 0.25, 0.05])[0]

        for commit_num in range(num_commits):
            date_str = current_date.strftime('%Y-%m-%d')
            file_ext = random.choice(file_extensions)
            filename = f"code/day_{date_str}_{commit_num}{file_ext}"

            os.makedirs(os.path.dirname(filename), exist_ok=True)
            content = generate_file_content(file_ext, date_str, commit_num)

            with open(filename, 'w') as f:
                f.write(content)

            hour = random.randint(9, 18)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)

            commit_datetime = current_date.replace(hour=hour, minute=minute, second=second)
            date_string = commit_datetime.strftime('%Y-%m-%d %H:%M:%S')

            subprocess.run(['git', 'add', filename])

            env = os.environ.copy()
            env['GIT_AUTHOR_DATE'] = date_string
            env['GIT_COMMITTER_DATE'] = date_string

            commit_message = random.choice(commit_message)
            subprocess.run(['git', 'commit', '-m', commit_message], env=env)

            print(f"Created commit for {date_string}: {commit_message}")

def generate_file_content(file_ext, date_str, commit_num):
    """Generate content for the file based on its extension."""
    if file_ext == '.py':
        return f"""# Python code for {date_str}
def main():
    print("Hello from {date_str}")
    return True

if __name__ == "__main__":
    main()
"""
    elif file_ext == '.js':
        return f"""// JavaScript file - {date_str}
function greet() {{
    console.log("Hello from {date_str}");
    return true;
}}

greet();
"""
    elif file_ext == '.md':
        return f"""# Progress Report - {date_str}
## What I learned today:
- Worked on project improvements
- Fixed several bugs
- Updated documenation

## Next Steps:
- Continue with feature development
- Add more tests
""" 
    elif file_ext == '.json':
        return f"""{{
        "date": "1. {date_str}",
        "version": "1.{commit_num}",
        "status": "active"
        }}"""
    elif file_ext == '.yml':
        return f"""# Config file - {date_str}
version: 1.{commit_num}
date: {date_str}
enabled: true
"""
    else: # .txt
        return f"""Daily log entry for {date_str}
Progress made:
- Code improvements
- Bug fixes
- Documentation updates

Commit #{commit_num}
"""
if __name__ == "__main__":
    backdate_commit(90)