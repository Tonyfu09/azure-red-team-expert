#!/usr/bin/env python3

import os
import subprocess
import sys

REPO_URL = "https://github.com/SySS-Research/azurenum.git"
REPO_DIR = "azurenum"

def run_command(cmd, cwd=None):
    print(f"\n[*] Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    return result.returncode

# Clone repository if missing
if not os.path.exists(REPO_DIR):
    print("[*] Cloning AzurEnum...")
    if run_command(f"git clone {REPO_URL}") != 0:
        print("[!] Failed to clone repository.")
        sys.exit(1)

# Install requirements
requirements = os.path.join(REPO_DIR, "requirements.txt")

if os.path.exists(requirements):
    print("[*] Installing requirements...")
    run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        cwd=REPO_DIR
    )

# Prompt for UPN
upn = input("\nEnter UPN (user@domain.com): ").strip()

if not upn:
    print("[!] UPN cannot be empty.")
    sys.exit(1)

# Run AzurEnum
cmd = f"{sys.executable} azurenum.py -u {upn}"

print("\n[*] Starting AzurEnum...")
subprocess.run(cmd, shell=True, cwd=REPO_DIR)
