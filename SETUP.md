# Setting Up

## Git & GitHub 

Everyone will need a GitHub account. If you already have a GitHub account, you can skip step 1. 

### Step 1: Create a GitHub Account

1. Go to [github.com](https://github.com) and click **Sign up**
2. Follow the prompts to create your account
3. Verify your email address if required

### Step 2: Fork the Repository

1. Navigate to the original repository on GitHub
2. Click the **Fork** button in the top-right corner
3. Select your account as the destination for the fork, e.g. if your GitHub account is "msmith", you'd use `msmith/ds2002-course` as name for the forked repo (should be set as default).
4. Wait for the fork to complete
5. Bookmark the webpage of your forked GitHub repository. You will be using it frequently :) 

### Step 3: Create a Personal Access Token (PAT)

**Note:** This step is required if you plan to use git on your own computer/laptop.

Personal Access Tokens (PATs) are an established best practice for securing access to your repositories. Unlike SSH keys, which grant broad access, PATs provide more granular control over what actions are allowed. You can create tokens with specific scopes (like read-only access, or access only to certain repositories), making them more secure and easier to manage. PATs are also easier to revoke if compromised, as you can delete individual tokens without affecting your entire account.

1. Go to GitHub Settings → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Click **Generate new token** → **Generate new token (classic)**
3. Give your token a descriptive name (e.g., "DS2002 Course")
4. Select the **repo** scope (this enables clone, pull, push, and submitting pull requests)
5. Set the token expiration date to May 31, 2026.
6. Click **Generate token** at the bottom
7. **Copy the token immediately** - you won't be able to see it again!
8. Store it securely (you'll use it as your password when using git from your local machine)

### Step 4: First Steps in GitHub Codespaces

The easiest way to get started is to use GitHub Codespaces (next section, Option 1). You can launch Codespaces directly through your repo in GitHub; all the software tools you will need are already configured and will be at your disposal at single click of a button. It couldn't be easier. 

1. In your forked repository, click the green **Code** button
2. Select the **Codespaces** tab
3. Click **Create codespace on main** (or select a branch)
4. GitHub will automatically detect and use the default devcontainer configuration
5. Wait for the codespace to initialize (this may take a few minutes)

You should see a screen like this:
![Screenshot of terminal in GitHb Codespaces](/docs/images/codespaces.png)

Once your codespace is ready, you'll have a fully configured development environment in your browser!
