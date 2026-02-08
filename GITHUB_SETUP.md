# GitHub Setup Guide for ERP System

## Prerequisites
- Git installed (https://git-scm.com/download/win)
- GitHub account (https://github.com/signup)

## Step 1: Install Git (Windows)

### Option A: Windows Package Manager (Fastest)
```powershell
winget install Git.Git
```
Then restart your terminal/PowerShell.

### Option B: Direct Download
Download from: https://git-scm.com/download/win
- Run the installer
- Use default settings
- Restart your terminal

### Verify Installation
```powershell
git --version
```

---

## Step 2: Configure Git (First Time Only)

Replace with your actual GitHub username and email:

```powershell
git config --global user.name "Your GitHub Username"
git config --global user.email "your.email@example.com"
```

Verify configuration:
```powershell
git config --global --list
```

---

## Step 3: Initialize Git Repository

```powershell
cd "D:\MCA Final Project\ERP-based Integrated Student Management system"
git init
```

---

## Step 4: Stage Files for Commit

```powershell
# Add all files (gitignore will exclude unnecessary files)
git add .

# View staged files
git status
```

---

## Step 5: Create Initial Commit

```powershell
git commit -m "Initial commit: ERP-based Integrated Student Management System

Features:
- Admission module with student registration
- Fee management system
- Hostel allocation
- Exam records management
- Role-Based Access Control (RBAC)
- Admin dashboard with real-time updates
- Secure authentication with Flask-Login"
```

---

## Step 6: Create GitHub Repository

1. Go to https://github.com/new
2. **Repository name**: `ERP-Student-Management` (or your preferred name)
3. **Description**: `ERP-based Integrated Student Management System`
4. **Public or Private**: Choose based on your preference
5. **Add README**: Uncheck (we already have one)
6. **Add .gitignore**: Uncheck (we already have one)
7. Click **"Create repository"**

---

## Step 7: Connect Local Repo to GitHub

GitHub will show you commands after creating the repo. Run these in your PowerShell:

```powershell
# Add GitHub as remote (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/ERP-Student-Management.git

# Rename branch to main (if needed)
git branch -M main

# Push code to GitHub
git push -u origin main
```

---

## Step 8: Push Updates in Future

After making changes:

```powershell
git add .
git commit -m "Describe your changes here"
git push
```

---

## Helpful Git Commands

```powershell
# Check git status
git status

# View commit history
git log

# View changes
git diff

# Create a new branch
git branch feature-name

# Switch branch
git checkout feature-name

# Undo recent changes
git reset --hard HEAD~1

# See remote URLs
git remote -v
```

---

## .gitignore Already Created

The `.gitignore` file is already created in your project. It excludes:
- `__pycache__/` directories
- `*.pyc` files
- `.venv/` and `venv/` directories
- `.env` files
- IDE files (`.vscode/`, `.idea/`)
- Database backups
- And more...

This ensures you don't push unnecessary files to GitHub.

---

## Recommended GitHub Setup

1. **Add a proper README.md** (already exists - good!)
2. **Add topics** to your repo (github.com/YOUR-USERNAME/repo → About → Topics)
   - `erp` `student-management` `flask` `mysql` `python`
3. **Enable Issues** for bug tracking
4. **Enable Discussions** for community interaction

---

## Quick Reference: Complete Setup from Scratch

```powershell
# 1. Install Git
winget install Git.Git

# 2. Configure Git
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# 3. Initialize and commit
cd "D:\MCA Final Project\ERP-based Integrated Student Management system"
git init
git add .
git commit -m "Initial commit: ERP System"

# 4. Create repo on GitHub at https://github.com/new

# 5. Connect and push
git remote add origin https://github.com/YOUR-USERNAME/ERP-Student-Management.git
git branch -M main
git push -u origin main
```

---

## Need Help?

- Git Documentation: https://git-scm.com/doc
- GitHub Help: https://docs.github.com
- GitHub Desktop (GUI Alternative): https://desktop.github.com

