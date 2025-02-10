import random
import re
user_accounts = {}

def deposit(email_address, password, amount):
    if email_address in user_accounts and user_accounts[email_address][0] == password:
        user_accounts[email_address][1] += amount
        return f"✅ Amount ₹{amount} credited successfully! Your new balance: ₹{user_accounts[email_address][1]}"
    else:
        return "❌ Invalid email or password."

def withdrawal(email_address, password, amount):
    if email_address in user_accounts and user_accounts[email_address][0] == password:
        if user_accounts[email_address][1] >= amount:
            user_accounts[email_address][1] -= amount
            return f"✅ Amount ₹{amount} debited successfully! Your new balance: ₹{user_accounts[email_address][1]}"
        else:
            return "❌ Insufficient balance."
    else:
        return "❌ Invalid email or password."

def transfer(email_address, password, recipient_name, amount):
    if email_address in user_accounts and user_accounts[email_address][0] == password:
        if user_accounts[email_address][1] >= amount:
            user_accounts[email_address][1] -= amount
            return f"✅ ₹{amount} transferred to {recipient_name} successfully! Your new balance: ₹{user_accounts[email_address][1]}"
        else:
            return "❌ Insufficient balance."
    else:
        return "❌ Invalid email or password."

def check_balance(email_address, password):
    if email_address in user_accounts and user_accounts[email_address][0] == password:
        return f"💰 Your current balance: ₹{user_accounts[email_address][1]}"
    return "❌ Invalid email or password."

# Bank Management System
print("\n\t\t🏦 BANKING MANAGEMENT SYSTEM 🏦")
name = input("Enter your name: ").strip().title()
print(f"👋 Hello {name}, Welcome! Please sign up with your email to create an account.")

# Sign-up Process
while True:
    email_address = input("Enter your Email ID: ").strip()
    password = input("Create a Password: ").strip()

    # Email Validation
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_address):
        print("❌ Invalid email format. Please enter a valid email.")
        continue

    # Password Validation
    if len(password) < 8 or not re.search("[A-Z]", password) or not re.search("[a-z]", password) or not re.search("[0-9]", password) or not re.search("[@!#$%^&*]", password):
        print("❌ Weak password! It must be at least 8 characters long and include uppercase, lowercase, a number, and a special character.")
        continue

    # Store user account details
    account_no = random.randint(10000, 99999)
    user_accounts[email_address] = [password, 5000]  # Default balance ₹5000
    print("\n✅ Sign-up Successful!")
    print(f"👤 Account Holder: {name}\n🏦 Account Number: {account_no}\n💰 Your Balance: ₹5000")
    break

# Banking Services Menu
while True:
    print("\n🔹 Available Banking Services:")
    print("\t1️⃣ Deposit Money")
    print("\t2️⃣ Withdraw Money")
    print("\t3️⃣ Transfer Money")
    print("\t4️⃣ Check Balance")
    print("\t5️⃣ Exit")

    try:
        choice = int(input("\nEnter your choice (1-5): "))
    except ValueError:
        print("❌ Invalid choice! Please enter a number between 1-5.")
        continue

    if choice == 1:
        print("\n💰 DEPOSIT MONEY")
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        try:
            amount = int(input("Enter the amount to deposit: ₹"))
            if amount <= 0:
                print("❌ Deposit amount must be greater than zero.")
            else:
                print(deposit(email, password, amount))
        except ValueError:
            print("❌ Invalid amount. Please enter a valid number.")

    elif choice == 2:
        print("\n💸 WITHDRAW MONEY")
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        try:
            amount = int(input("Enter the amount to withdraw: ₹"))
            if amount <= 0:
                print("❌ Withdrawal amount must be greater than zero.")
            else:
                print(withdrawal(email, password, amount))
        except ValueError:
            print("❌ Invalid amount. Please enter a valid number.")

    elif choice == 3:
        print("\n📤 TRANSFER MONEY")
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        recipient = input("Enter the recipient's name: ").strip().title()
        try:
            amount = int(input(f"Enter the amount to transfer to {recipient}: ₹"))
            if amount <= 0:
                print("❌ Transfer amount must be greater than zero.")
            else:
                print(transfer(email, password, recipient, amount))
        except ValueError:
            print("❌ Invalid amount. Please enter a valid number.")

    elif choice == 4:
        print("\n📊 CHECK BALANCE")
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        print(check_balance(email, password))

    elif choice == 5:
        print("\n👋 Thank you for using our Banking Management System. See you again!")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1-5.")
