import sys
from subprocess import call

if len(sys.argv) != 4:
    print("Error wrong parameter number")
    print("Usage: python runterraform.py region prefix destroy")
    print("Example: python runterraform.py eu-central-1 peppetest1 False")
    sys.exit(1)

region = sys.argv[1]
prefix = sys.argv[2]
destroy = sys.argv[3]

cmd = ["terraform"]

if destroy.lower() == "true":
    cmd.extend(["destroy", "-auto-approve"])
else:
    cmd.extend(["apply", "-auto-approve"])

cmd.extend(["-var", f"region={region}"])
cmd.extend(["-var", f"prefix={prefix}"])

print(cmd)
call(cmd)
