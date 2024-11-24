#!/usr/bin/env python3

import subprocess

super_user = 'root'
username = subprocess.run('whoami', capture_output=True, text=True).stdout.strip()
group = 'vboxsf'

def exec_command (commands:list):
  result = subprocess.run(commands, check=True)
  return result

def display_final_message():
    """
    Displays a closing message with contact details and credits.
    """
    print("✨ You're all set! Thank you for using this script! 🎉")
    print(" ")

    print("📧 Email: josuezolakiousa@gmail.com")
    print("🌐 Website: https://github.com/josuezolakiomd/modern-linktree")
    print(" ")
    print("💻 Script developed by Josue Zolakio on 11/22/2024.\n")
    print("🛠️ Stay tuned for more awesome tools! 🚀\n")
    print("⚠️ To apply the changes, please log out or restart your system. 🔄")
    print("🔐 Logging out ensures that all configurations are properly updated. ✅\n")

print("💻 Booting up... 🔄 Initializing components...\n")
print("✅ Initialization complete!\n")
print("🛠️ Starting OS update and upgrade process... ⏳\n")

if username and username != super_user:
    update_upgrade_status = "\n✅ System updated and upgraded successfully! 🎉\n"
    adding_user = f"🛠️ Adding '{(username)}' to the group '{group}'... ⏳\n"
    adding_user_status = f"✅ Successfully added '{username}' to the group '{group}'. 🎉\n"

    exec_command(["sudo", "apt", "update"])
    exec_command(["sudo", "apt", "upgrade"])

    print(update_upgrade_status)

    print(adding_user)
    exec_command(["sudo", "adduser", username, group])
    print(adding_user_status)

    display_final_message()
else:
  print("❌ There was an error, try again!")