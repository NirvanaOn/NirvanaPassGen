# 🔐 NirvanaPassGen - Secure Password Generator & Backup Tool

Welcome to **NirvanaPassGen** – a beginner-friendly yet powerful Python tool to help users create, evaluate, hash, and back up strong passwords in a secure and memorable way.

Developed by [Nirvana (Om Sonani)](https://github.com/NirvanaOn), this tool is ideal for anyone looking to boost their password game — especially students, ethical hackers, and everyday users who want both **security** and **convenience**.

---

## 🚀 Features

### 🔒 1. Hash Your Password Securely
Choose from popular hashing algorithms:
- MD5
- SHA1
- SHA256

Once hashed, your password becomes irreversible and secure.

---

### 📊 2. Password Strength Evaluation
Your password is scored based on:
- Length (12+ characters preferred)
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Results:
- **Weak**: Not safe for use
- **Medium**: Better, but still improvable
- **Strong**: Good to go!

---

### ⏳ 3. Crack Time Estimation
Estimates how long it would take to crack your password using brute-force:
| Strength Level       | Estimated Time      |
|----------------------|---------------------|
| Very Weak            | Seconds–Minutes     |
| Weak                 | Hours               |
| Medium               | Years               |
| Strong               | Decades             |
| Extremely Strong     | Thousands of Years  |
| Virtually Uncrackable| Millions of Years   |

---

### 🧾 4. Reversed QR Code Backup
Instead of storing passwords, NirvanaPassGen:
- Reverses your base password
- Converts it into a QR code
- Saves it in a `backups/` folder with a timestamp
- Each QR is stored separately — no overwriting

Just scan and reverse again when needed 🔁

---

## 💡 The Ultimate Password Strategy (Memorable + Secure)

🔑 Instead of generating random gibberish you’ll forget, **combine a base key with a modifier**:

### Formula:
Base Key = Nirvana! 
Modifier = 2025#LinkedIn 
Final = Nirvana!2025#LinkedIn


- **Memorable** to you
- **Unique** per website
- **Complex** and long for security
- **Re-creatable** anytime using NirvanaPassGen

🔥 Pair it with QR backup and hashing, and you’ll never lose a password again.

---

## 🛠 How to Run This Tool

### 🔧 Requirements:
- Python 3
- `qrcode` module  
Install via pip:
```bash
pip install qrcode[pil]
