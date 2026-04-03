import os
from functions import read_file, create_account
from updated_monitoring import get_size, monitor

if not os.path.exists('profile.json') or os.path.getsize('profile.json') == 0:    
    status = create_account()
    if status == 'admin_mode':
        if __name__ == "__main__":
            monitor()
else:
    current_user = input("Do you want to login this current account? (y/n):  ")

    if current_user.lower() == 'y':
        data = read_file()
        print(f"Hello {data['name'].title()}!")
    else:
        create_account()