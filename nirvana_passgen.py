import hashlib
import re
import qrcode
import os
from datetime import datetime

def hash_password(password, algorithm=1):
    try:
        if algorithm == 1:
            return hashlib.md5(password.encode()).hexdigest()
        elif algorithm == 2:
            return hashlib.sha1(password.encode()).hexdigest()
        elif algorithm == 3:
            return hashlib.sha256(password.encode()).hexdigest()
        else:
            raise ValueError("Unexpected algorithm value. Please choose 1, 2, or 3.")
    except Exception as e:
        print(f"Error in hashing password: {e}")
        return None

def pass_strength(password):
    try:
        score = 0
        if len(password) >= 12:
            score += 1
        if re.search(r'[A-Z]' , password):
            score += 1
        if re.search(r'[a-z]',password):
            score += 1
        if re.search(r'[0-9]',password):
            score += 1
        if re.search(r'[\W_]',password):
            score += 1

        if score <= 2:
            print("Weak Password")
        elif score == 3 or score == 4:
            print("Medium Strength")
        elif score == 5:
            print("Strong Password")
    except Exception as e:
        print(f"Error in password strength evaluation: {e}")

def estimate_crack_time(password):
    try:
        charset_size = 0
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'[0-9]', password):
            charset_size += 10
        if re.search(r'[\W_]', password):
            charset_size += 32

        total_combinations = charset_size ** len(password)
        guesses_per_sec = 1_000_000_000
        seconds = total_combinations / guesses_per_sec
        years = seconds / (60 * 60 * 24 * 365)

        if years > 1_000_000:
            print("Virtually Uncrackable (Millions of Years)")
        elif years > 1000:
            print("Extremely Strong (Thousands of Years)")
        elif years > 10:
            print("Strong (Decades)")
        elif years > 1:
            print("Medium (Years)")
        elif seconds > 3600:
            print("Weak (Hours)")
        else:
            print("Very Weak (Seconds to Minutes)")
    except Exception as e:
        print(f"Error in estimating crack time: {e}")

def save_qr(password):
    try:
        reversed_password = password[::-1]
        qr = qrcode.make(reversed_password)
        if not os.path.exists('backups'):
            os.makedirs('backups')

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        qr_file_path = f'backups/{timestamp} Pass .png'
        qr.save(qr_file_path)
        print(f"Backup QR Code saved at: {qr_file_path}")
    except Exception as e:
        print(f"Error in saving QR code: {e}")

def get_valid_choice():
    while True:
        try:
            print("\nChoose hash algorithm:")
            print("1. MD5")
            print("2. SHA1")
            print("3. SHA256")
            choice = int(input("Enter (1/2/3): "))
            if choice not in [1, 2, 3]:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue
            return choice
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

print("Welcome to NirvanaPassGen")

while True:
    try:
        password = input("Enter your base password/key: ")
        if not password:
            print("Password cannot be empty. Please try again.")
            continue

        pass_strength(password)
        estimate_crack_time(password)

        choice = get_valid_choice()
        hashed_password = hash_password(password, choice)
        if hashed_password:
            print(f"Your Hashed Password : {hashed_password}")

        save_qr(password)
        break
    except Exception as e:
        print(f"Unexpected error: {e}")
