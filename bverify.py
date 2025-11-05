import bcrypt
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: bverify <bcrypt_hash> <password>")
        sys.exit(1)

    hashed = sys.argv[1].encode('utf-8')
    password = sys.argv[2].encode('utf-8')

    if bcrypt.checkpw(password, hashed):
        print("✅ Password matches")
    else:
        print("❌ Password does not match")

if __name__ == "__main__":
    main()
