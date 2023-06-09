# The count_users function recursively counts the amount of users that belong to a group in the company system, 
# by going through each of the members of a group and if one of them is a group, 
# recursively calling the function and counting the members. 
# But it has a bug! Can you spot the problem and fix it?

def count_users(group):
    count = 0
    for member in get_members(group):
        if is_group(member):
            count += count_users(member)
        else:
            count += 1
    return count


print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18