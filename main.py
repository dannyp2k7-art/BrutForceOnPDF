import pikepdf
from tqdm import tqdm


with open("rockyou.txt", "r", encoding="latin-1") as f:
    passwords = [line.strip() for line in f]


for password in tqdm(passwords, "Decrypting PDF"):
    try:

        with pikepdf.open("Test03.pdf", password=password) as pdf:

            print("Password found:", password)
            break
    except pikepdf._core.PasswordError as e:

        continue
