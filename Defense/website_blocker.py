import os

# Path to the system hosts file in Windows
host_path = r"C:\Windows\System32\drivers\etc\hosts" if os.name == "nt" else "/etc/hosts"
ip_redirect = "127.0.0.1"

# Path to the website file that stores our list of malicious websites
website_list_file = "malicious_websites.txt"

def load_websites_from_file(file_path):
    """Load websites from a file, one per line."""
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist. Creating a new file.")
        with open(file_path, "w") as f:
            pass
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_websites_to_file(file_path, websites):
    """Save a list of websites to a file."""
    with open(file_path, "w") as f:
        f.writelines(f"{website}\n" for website in websites)

def block_websites(websites, host_path=host_path, ip_redirect=ip_redirect):
    try:
        with open(host_path, "r+") as hosts_file:
            content = hosts_file.readlines()
            hosts_file.seek(0)
            
            for line in content:
                hosts_file.write(line)
                for website in websites:
                    if website in line:
                        websites.remove(website)

            for website in websites:
                hosts_file.write(f"{ip_redirect} {website}\n")
            
            hosts_file.truncate()
        print(f"Successfully blocked websites: {', '.join(websites)}")
    except PermissionError:
        print("Permission denied. Run the script with administrative privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")

def unblock_websites(websites, host_path=host_path):
    try:
        with open(host_path, "r+") as hosts_file:
            content = hosts_file.readlines()
            hosts_file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    hosts_file.write(line)
            hosts_file.truncate()
        print(f"Successfully unblocked websites: {', '.join(websites)}")
    except PermissionError:
        print("Permission denied. Run the script with administrative privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_websites_to_file(file_path):
    """Add new websites to the text file."""
    websites = load_websites_from_file(file_path)
    print("Enter the websites you want to block (one per line). Enter 'done' when finished.")
    while True:
        website = input("Website: ").strip()
        if website.lower() == "done":
            break
        if website and website not in websites:
            websites.append(website)
    save_websites_to_file(file_path, websites)
    print(f"Added websites to the block list: {', '.join(websites)}")

# Menu options to modify the website file
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Block websites")
        print("2. Unblock websites")
        print("3. Add websites to block list")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            websites = load_websites_from_file(website_list_file)
            block_websites(websites)
        elif choice == "2":
            websites = load_websites_from_file(website_list_file)
            unblock_websites(websites)
        elif choice == "3":
            add_websites_to_file(website_list_file)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
