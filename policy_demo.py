#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Importing classes as modules exported as executable Python files:
from policyholder import Policyholder
from product import Product, ProductManager
from payment import Payment


# In[16]:


# Function to get valid input
def get_valid_input(prompt, input_type):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

# Demo with user input
def demo():
    manager = ProductManager()

    # Creating products with user input
    for _ in range(2):
        product_id = get_valid_input("Enter product ID: ", int)
        name = input("Enter product name: ")
        price = get_valid_input("Enter product price: ", float)
        manager.create_product(product_id, name, price)

    # Optionally update a product
    update_choice = input("Do you want to update a product? (yes/no): ").strip().lower()
    if update_choice == 'yes':
        product_id = get_valid_input("Enter product ID to update: ", int)
        name = input("Enter new product name (leave blank to keep current): ")
        price = input("Enter new product price (leave blank to keep current): ")
        price = float(price) if price else None
        manager.update_product(product_id, name=name if name else None, price=price)

    # Optionally remove a product
    remove_choice = input("Do you want to remove a product? (yes/no): ").strip().lower()
    if remove_choice == 'yes':
        product_id = get_valid_input("Enter product ID to remove: ", int)
        manager.remove_product(product_id)

if __name__ == "__main__":
    demo()


# In[20]:


def input_policyholder():
    while True:
        try:
            policyholder_id = int(input("Enter Policyholder ID: "))
            name = input("Enter Policyholder Name: ")
            date = datetime.strptime(input("Enter Registration Date (YYYY-MM-DD): "), "%Y-%m-%d")
            policy_type = input("Enter Policy Type: ")
            return Policyholder(policyholder_id, name, date, policy_type)
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    policyholders = []
    for _ in range(5):
        policyholder = input_policyholder()
        policyholders.append(policyholder)

    while True:
        print("\nOptions:")
        print("1. Register Policyholder")
        print("2. Suspend Policyholder")
        print("3. Reactivate Policyholder")
        print("4. Update Policyholder")
        print("5. Print Policyholders")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            policyholder_id = int(input("Enter Policyholder ID to register: "))
            for ph in policyholders:
                if ph.policyholder_id == policyholder_id:
                    ph.register()
                    break
            else:
                print("Policyholder not found.")
        elif choice == '2':
            policyholder_id = int(input("Enter Policyholder ID to suspend: "))
            for ph in policyholders:
                if ph.policyholder_id == policyholder_id:
                    ph.suspend()
                    break
            else:
                print("Policyholder not found.")
        elif choice == '3':
            policyholder_id = int(input("Enter Policyholder ID to reactivate: "))
            for ph in policyholders:
                if ph.policyholder_id == policyholder_id:
                    ph.reactivate()
                    break
            else:
                print("Policyholder not found.")
        elif choice == '4':
            policyholder_id = int(input("Enter Policyholder ID to update: "))
            for ph in policyholders:
                if ph.policyholder_id == policyholder_id:
                    name = input("Enter new name (leave blank to keep current): ")
                    date_input = input("Enter new date (YYYY-MM-DD, leave blank to keep current): ")
                    date = datetime.strptime(date_input, "%Y-%m-%d") if date_input else None
                    policy_type = input("Enter new policy type (leave blank to keep current): ")
                    ph.update(name=name if name else None, date=date, policy_type=policy_type if policy_type else None)
                    break
            else:
                print("Policyholder not found.")
        elif choice == '5':
            for ph in policyholders:
                print(f"ID: {ph.policyholder_id}, Name: {ph.name}, Status: {ph.status}, Date: {ph.date}, Policy Type: {ph.policy_type}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[21]:


# Function to create payments based on user input
def create_payments():
    payments = []
    for i in range(5):
        payment_id = input(f"Enter payment ID for payment {i+1}: ")
        policyholder_id = input(f"Enter policyholder ID for payment {i+1}: ")
        amount = float(input(f"Enter amount for payment {i+1}: "))
        date = input(f"Enter date (YYYY-MM-DD) for payment {i+1}: ")
        payment = Payment(payment_id, policyholder_id, amount, date)
        payments.append(payment)
    return payments

# Function to demonstrate the use case
def demo():
    payments = create_payments()
    for payment in payments:
        payment.process_payment()
        payment.send_reminder()
        payment.apply_penalty()

# Run the demo
demo()


# In[ ]:




