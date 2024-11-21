#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing required modues:

from datetime import datetime, timedelta

#Creating payments class:

class Payment:
    def __init__(self, payment_id, policyholder_id, amount, date, status='pending'):
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.amount = amount
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.status = status

# First-time insurance policy purchase:
    
    def process_payment(self):
        try:
            if self.status == 'pending':
                self.status = 'completed'
                print(f"Payment {self.payment_id} processed successfully.")
            else:
                print(f"Payment {self.payment_id} has already been processed.")
        except Exception as e:
            print(f"An error occurred while processing payment {self.payment_id}: {e}")

# Policy renewal reminder 25days after policy date:
    
    def send_reminder(self):
        try:
            reminder_date = self.date + timedelta(days=25)
            if datetime.now() >= reminder_date:
                print(f"Reminder sent for payment {self.payment_id}.")
            else:
                print(f"Reminder for payment {self.payment_id} will be sent on {reminder_date.strftime('%Y-%m-%d')}.")
        except Exception as e:
            print(f"An error occurred while sending reminder for payment {self.payment_id}: {e}")

 # Process and apply a penalty of 5% if payment is past due by 7 days:
    
    def apply_penalty(self):
        try:
            due_date = self.date + timedelta(days=7)
            if datetime.now() > due_date and self.status == 'pending':
                penalty_amount = self.amount * 0.05
                self.amount += penalty_amount
                print(f"Penalty applied to payment {self.payment_id}. New amount: {self.amount}")
            else:
                print(f"No penalty applied to payment {self.payment_id}.")
        except Exception as e:
            print(f"An error occurred while applying penalty to payment {self.payment_id}: {e}")


# In[ ]:




