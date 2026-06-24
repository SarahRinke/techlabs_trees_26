# Git how to

## Quick overview
```
git clone <repo-url>        # Clone the repo
git checkout -b feature/my-feature  # Create a new branch
git add .                   # Stage changes
git commit -m "description" # Commit changes
git push origin feature/my-feature # Push branch
Then open a Pull Request on GitHub
```

# Git Best Practices for Group Projects (Beginner's Guide)

## Branching
- **Never work directly on the main branch** - it should always contain working code
- Create a new branch for every feature or task you work on
   - Example: `git checkout -b feature/login-page`
- Use **clear and descriptive branch names** so teammates know what you're working on
- Delete branches after they have been merged to keep things tidy

## Committing
- **Commit often** - small, frequent commits are better than one large one
- Write **clear commit messages** that describe what you changed and why
   - ✅ `"Add login form validation"`
   - ❌ `"fixed stuff"`
- **Never commit sensitive information** like passwords or API keys
- Always check what you're committing with `git status` before committing

## Staying Up to Date
- **Pull from main regularly** to keep your branch up to date and avoid large conflicts
   - `git pull origin main`
- Do this especially **before starting new work**
- If you get a **merge conflict**, don't panic - read the conflicting lines carefully and talk to your teammate if unsure

## Pull Requests (PRs)
- When your work is ready, **open a Pull Request** on GitHub to merge your branch into main
- Write a **short description** of what your PR does
- **Review your teammates' PRs** and give constructive feedback
- Don't merge your own PR - **have at least one teammate review it first**

## Common Mistakes to Avoid
- Don't use `git push --force` unless you really know what you're doing
- Don't leave large amounts of work uncommitted for days
- Don't work on the same file as a teammate without communicating first
- Don't ignore merge conflicts and just overwrite your teammate's work

## Communication is Key
- **Tell your team** what you are working on to avoid doing the same work twice
- Use **GitHub Issues** to track tasks and bugs
- If something breaks, **let the team know immediately**
- Ask for help early - git can be confusing at first and that's completely normal!

# Your own Dev branch (more detail)

1. Clone the Repository

```bash
git clone <repository-url>
```

2. Navigate into the Project Directory

```bash
cd <repository-name>
```

3. Create and Switch to Your New Branch

```bash
# Create and switch in one command
git checkout -b dev_your_name

# OR using the newer syntax
git switch -c dev_your_name
```

4. Make Your Changes, Then Stage and Commit

```bash
# Stage all changes
git add .

# Or stage a specific file
git add <filename>

# Commit with a message
git commit -m "your commit message"
```

5. Push Your Branch to Git

```bash
git push origin dev_your_name
```

A few tips:

    git branch will list all branches and show which one you're on
    git status will show you what files have been changed/staged

# Merging Dev Branch into Main
## Option 1: Merge (Most Common)

```bash
# Switch to main branch
git checkout main

# Pull latest main to make sure you're up to date
git pull origin main

# Merge dev into main
git merge dev

# Push the updated main
git push origin main
```

## Option 2: Pull Request (Best Practice for Teams)

If you're working on GitHub, the preferred approach is:

    Push your dev branch
    Go to the repository on the website
    Click "Compare & pull request" or "Create merge request"
    Review the changes and merge via the UI

This allows for code review before merging into main.