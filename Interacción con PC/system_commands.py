
import subprocess

subprocess.run(["date"])
subprocess.run(["sleep", "2"])
result = subprocess.run(["ls", "this file_does_not_exist"])
print(result.returncode)






