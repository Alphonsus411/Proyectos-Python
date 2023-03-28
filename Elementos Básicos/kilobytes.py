"""
Consider this scenario about using Python to make calculations:

In a managed computing environment, there are 200 remote computers that must download 200 MB (megabytes) of updates each month.  
There are 1024 KB (kilobytes) in each MB.  

Fill in the blank in the code below to compute the number of total kilobytes downloaded by these computers from the remote update server each month.

"""

download_size_kb = 200*1024
total_computers = 200
total_kbs = download_size_kb*total_computers


print(total_kbs) # Should print 40960000.0