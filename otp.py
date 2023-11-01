import os
import sys


def read_file(filename):
    with open(filename, 'rb') as f:
        return f.read()


def write_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)


def generate_otp(length):
    return os.urandom(length)


def xor_bytes(data1, data2):
    return bytes(a ^ b for a, b in zip(data1, data2))


def encrypt(input_filename, otp_filename, encrypted_filename):
    print(f"Encrypting {input_filename}...")
    data = read_file(input_filename)
    otp = generate_otp(len(data))
    encrypted_data = xor_bytes(data, otp)

    write_file(otp_filename, otp)
    write_file(encrypted_filename, encrypted_data)
    print(f"Encryption complete! OTP saved as {otp_filename}, encrypted file saved as {encrypted_filename}.")


def decrypt(encrypted_filename, otp_filename, decrypted_filename):
    print(f"Decrypting {encrypted_filename}...")
    encrypted_data = read_file(encrypted_filename)
    otp = read_file(otp_filename)

    decrypted_data = xor_bytes(encrypted_data, otp)
    write_file(decrypted_filename, decrypted_data)
    print(f"Decryption complete! Decrypted file saved as {decrypted_filename}.")


print("")
print("🌟 Welcome to the Ultimate OTP File Encryption & Decryption Tool 🌟")
print("🛡️ Your go-to solution for secure file cryptography!")
print("🌐 Visit my GitHub repository for readme, other source codes for this and more comments: https://github.com/MasterAGB/OTP-File-Encryptor-Decryptor")
print("--------------------------------------------------------------------------------------")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        action = input("What action would you like to perform? Encrypt (enc) or Decrypt (dec): ")
        input_filename = input("Please provide the input filename: ")
        otp_filename = input("Name your OTP (One-Time Pad) file: ")
        output_filename = input("Name your output file: ")
    else:
        action = sys.argv[1]
        input_filename = sys.argv[2]
        otp_filename = sys.argv[3]
        output_filename = sys.argv[4]

    if action.lower() == 'enc':
        encrypt(input_filename, otp_filename, output_filename)
    elif action.lower() == 'dec':
        decrypt(input_filename, otp_filename, output_filename)
    else:
        print("🚫 Invalid action. Kindly use 'enc' for encryption or 'dec' for decryption.")
