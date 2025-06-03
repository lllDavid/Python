import uuid

random_uuid = uuid.uuid4()
print(f"Random UUID4: {random_uuid}")

time_based_uuid = uuid.uuid1()
print(f"Time-based UUID1: {time_based_uuid}")

namespace = uuid.NAMESPACE_DNS
name = "example.com"

uuid3 = uuid.uuid3(namespace, name) 
print(f"UUID3 (MD5): {uuid3}")

uuid5 = uuid.uuid5(namespace, name)  
print(f"UUID5 (SHA-1): {uuid5}")

parsed_uuid = uuid.UUID(str(random_uuid))
print(f"Parsed UUID: {parsed_uuid}")

def is_valid_uuid(val):
    try:
        uuid_obj = uuid.UUID(val)
        return True
    except ValueError:
        return False

print(is_valid_uuid(str(random_uuid)))  
print(is_valid_uuid("invalid-uuid-string"))  
