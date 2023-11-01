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
    data = read_file(input_filename)
    otp = generate_otp(len(data))
    encrypted_data = xor_bytes(data, otp)

    write_file(otp_filename, otp)
    write_file(encrypted_filename, encrypted_data)


def decrypt(encrypted_filename, otp_filename, decrypted_filename):
    encrypted_data = read_file(encrypted_filename)
    otp = read_file(otp_filename)

    decrypted_data = xor_bytes(encrypted_data, otp)
    write_file(decrypted_filename, decrypted_data)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        action = input("What would you like to do? (enc/dec): ")
        input_filename = input("Input filename: ")
        otp_filename = input("OTP filename: ")
        output_filename = input("Output filename: ")
    else:
        action = sys.argv[1]
        input_filename = sys.argv[2]
        otp_filename = sys.argv[3]
        output_filename = sys.argv[4]

    if action == 'enc':
        encrypt(input_filename, otp_filename, output_filename)
    elif action == 'dec':
        decrypt(input_filename, otp_filename, output_filename)
    else:
        print("Invalid action. Please use 'enc' for encryption or 'dec' for decryption.")
