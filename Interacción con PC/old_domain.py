#!/usr/bin/env python3

# import libraries

import csv
import re

def contains_domain(address, domain):
    """Returns True if the email adress contains the give domain,
    in the domain position, false if not."""
    domain_pattern = r'[\w\.-]+@'+domain+'$'
    if re.match(domain_pattern, address):
        return True
    
    return False

def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in the received address."""
    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address

def main():
    """Processes the list of emails, replacing any instances of the old domain with the new domain."""
    

    
