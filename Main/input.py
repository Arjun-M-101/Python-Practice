import sys
full_name=" ".join(sys.argv[1:])
print(full_name)

email = full_name.lower().replace(" ", ".")+"@company.com"

print("\n--- Your Profile ---")
print("Full Name:", full_name)
print("Email:", email)