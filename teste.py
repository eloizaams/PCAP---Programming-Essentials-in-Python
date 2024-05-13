from platform import *

print(platform())
print(platform(1))
print(platform(0, 1))
print(platform(aliased = False, terse = False))
print(machine())
print(processor())
print(system())
print(version())

print(python_implementation())

for atr in python_version_tuple():
    print(atr)