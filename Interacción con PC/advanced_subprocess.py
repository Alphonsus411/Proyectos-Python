import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["opt/my_app/"], my_env["PATH"])

result = subprocess.run(["my_app"], env=my_env)

