import hashlib
file_path=r"C:\Users\HP\Desktop\sample.txt.txt"
with open(file_path, "rb") as file:
   file_data=file.read()
   print(f"File content:{file_data}")
   hash_value = hash("sample.txt")
   print(f"Hash Value:{hash_value}")
   sha256_hash = hashlib.sha256(file_data).hexdigest()
   print(f"Sha Value:{sha256_hash}")
