import json
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad
from Crypto.Hash import SHA256
import os


SECRET = "GQ39%*g"


def get_user_input():
    print("\n=== AIS JSON Decryptor ===\n")

    pan = input("Enter PAN: ").strip().lower()
    dob = input("Enter DOB (ddmmyyyy): ").strip()

    file_path = input("Enter encrypted file path: ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found!")
        return None, None, None

    output_file = input("Enter output file name (default: decrypted.json): ").strip()
    if output_file == "":
        output_file = "decrypted.json"

    return pan, dob, file_path, output_file


def decrypt_ais(pan, dob, file_path, output_file):
    try:
        # Construct password
        password = (pan + SECRET + dob).encode()

        # Read file
        with open(file_path, "r") as f:
            k = f.read().strip()

        # Parse structure
        iv = bytes.fromhex(k[:32])
        salt = bytes.fromhex(k[32:64])
        ciphertext = base64.b64decode(k[64:])

        # Derive key
        key = PBKDF2(password, salt, dkLen=32, count=1000, hmac_hash_module=SHA256)

        # Decrypt
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)

        # Decode JSON
        decoded = decrypted.decode("utf-8")

        # Pretty format JSON
        parsed = json.loads(decoded) 

        # Save output
        with open(output_file, "w") as f:
            json.dump(parsed, f, indent=4)

        return True, f"Decryption successful! Output saved to: {output_file}"

    except Exception as e:
        return False, str(e)


def main():
    while True:
        pan, dob, file_path, output_file = get_user_input()

        if pan is None:
            continue

        success, message = decrypt_ais(pan, dob, file_path, output_file)
        
        if success:
            print(f"\n🎉 {message}")
        else:
            print("\n❌ Decryption failed!")
            print("Possible reasons:")
            print("- Wrong PAN or DOB")
            print("- Incorrect file")
            print("- File corrupted")
            print(f"Error details: {message}")

        again = input("\nDo you want to decrypt another file? (y/n): ").strip().lower()
        if again != "y":
            print("\n👋 Exiting...")
            break


if __name__ == "__main__":
    main()