https://roadmap.sh/projects/github-user-activity
# GitHub-User-Activity-CLI
A simple command-line interface (CLI) tool that fetches and displays the recent GitHub activity of any user using the GitHub public API.A simple command-line interface (CLI) tool that fetches and displays the recent GitHub activity of any user using the GitHub public API.

This project helps you practice:

Working with APIs

Handling JSON data

Building a CLI tool

Managing errors

Working without external libraries

🚀 Features

Fetches recent GitHub user activity

Displays readable activity output

Handles errors (invalid usernames, network issues, API errors)

Runs from the command line

Uses no external libraries — only Python built-ins

📦 Installation

Clone or download the project:

git clone https://github.com/<your-username>/github-activity-cli.git


Navigate into the project folder:

cd github-activity-cli


Make sure Python is installed:

python --version

▶️ Usage

Run the script using:

python github_activity.py <github-username>

Example:
python github_activity.py torvalds

Output Example:
Fetching activity for GitHub user: torvalds ...

Recent GitHub Activity:

- Pushed 3 commits to torvalds/linux
- Starred a repository: some-repo/name
- Created a new branch in torvalds/linux
- Forked repo: someone/project


(Actual output depends on the user’s activity.)

🛠 How It Works

The script uses the GitHub public API endpoint:

https://api.github.com/users/<username>/events


It then:

Fetches JSON event data

Parses each event type

Displays readable activity in the terminal

Supported event types include:

PushEvent

CreateEvent

IssuesEvent

ForkEvent

PullRequestEvent

WatchEvent (stars)

MemberEvent

And default fallback for unknown types

❗ Error Handling

The program gracefully handles:

Invalid GitHub usernames

API rate limiting

Network failures

Missing data fields

Examples:

Error: GitHub user not found.

Network error: Could not connect to GitHub.

📁 Project Structure
github-activity-cli/
│
├── github_activity.py     # Main CLI tool
├── README.md              # Documentation

✨ Future Improvements (Optional)

You can extend the project by adding:

Event filtering (--push, --stars, etc.)

Colored terminal output

Pagination support

Caching results for speed

Packaging as a pip installable CLI tool

👤 Author

Nanya (GitHub: @NanyaMary71)
Feel free to fork, improve, and submit pull requests!

📜 License

This project is open-source and free for learning purposes.


