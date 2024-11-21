#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing modules:

from datetime import datetime, timedelta

# Creating policyholders class:

class Policyholder:
    def __init__(self, policyholder_id, name, date, policy_type):
        self.policyholder_id = policyholder_id
        self.name = name
        self.status = 'active'
        self.date = date
        self.policy_type = policy_type

# Policy holders registration:
    def register(self):
        try:
            self.status = 'active'
            self.date = datetime.now()
            print(f"Policyholder {self.name} registered on {self.date}.")
        except Exception as e:
            print(f"Error during registration: {e}")

# suspend policy if not renewed after 30 days and remove policy if not renewed after 90 days:
    
    def suspend(self):
        try:
            if self.status == 'active' and datetime.now() > self.date + timedelta(days=30):
                self.status = 'suspended'
                print(f"Policyholder {self.name} suspended.")
            elif self.status == 'suspended' and datetime.now() > self.date + timedelta(days=90):
                self.status = 'removed'
                print(f"Policyholder {self.name} removed.")
        except Exception as e:
            print(f"Error during suspension: {e}")

# Reactivate policy if payment was made after suspension:
    
    def reactivate(self):
        try:
            if self.status == 'suspended':
                self.status = 'active'
                self.date = datetime.now()
                print(f"Policyholder {self.name} reactivated on {self.date}.")
            else:
                print(f"Policyholder {self.name} is not suspended and cannot be reactivated.")
        except Exception as e:
            print(f"Error during reactivation: {e}")

#Update policyholders with changes in policy:
    
    def update(self, name=None, date=None, policy_type=None):
        try:
            if name:
                self.name = name
            if date:
                self.date = date
            if policy_type:
                self.policy_type = policy_type
            print(f"Policyholder {self.policyholder_id} updated: Name - {self.name}, Date - {self.date}, Policy Type - {self.policy_type}.")
        except Exception as e:
            print(f"Error during update: {e}")


# In[ ]:




