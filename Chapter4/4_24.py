import os

print(os.listdir('.'))

print(os.listdir(b'.'))

pi_name_bytes = os.listdir(b'.')[1]
pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
print(pi_name_str)

print(pi_name_str.encode('ascii', 'surrogateescape'))
