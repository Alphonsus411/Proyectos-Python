from unittest import result


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.2f} km".format(miles, km)
    return result

print(convert_distance(12)) #should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) #should be: 5.5 miles equals 8.8 km
print(convert_distance(1)) #should be: 1 miles equals 1.6 km
