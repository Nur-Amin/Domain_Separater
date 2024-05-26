import os
import re

def separate_emails(email_list_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    with open(email_list_file, 'r') as emails:
        for email in emails:
            email = email.strip()  # Remove leading/trailing whitespace
            match = re.search(r'@(.+)', email)
            if match:
                domain = match.group(1)
                output_file = os.path.join(output_dir, domain + '.txt')
                with open(output_file, 'a') as outfile:  # Append emails to domain file
                    outfile.write(email + '\n')

# Example usage (modify file names and directory as needed)
separate_emails('email_list.txt', 'separated_emails')

print("Emails separated by domain successfully!")
