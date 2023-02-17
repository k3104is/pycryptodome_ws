# https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
# https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf
# C.1 AES-128 (Nk=4, Nr=10)
# https://www.rfc-editor.org/rfc/rfc3602
# Case #2
from Crypto.Cipher import AES

VAR_PATH = "./var/"

def main():
  # read variables
  with  open(VAR_PATH + "key.txt") as fk, \
        open(VAR_PATH + "data.txt") as fd, \
        open(VAR_PATH + "iv.txt") as fi:
    key = bytearray.fromhex(fk.read())
    iv = bytearray.fromhex(fi.read())
    data = bytearray.fromhex(fd.read())

  # aes-cbc
  ciphertext = aes_cbc_encrypt(key, iv, data)
  plaintext = aes_cbc_decrypt(key, iv, ciphertext)

  # result
  print("data       :" + data.hex())
  print("key        :" + key.hex())
  print("iv         :" + iv.hex())
  print("encrypted  :" + ciphertext.hex())
  print("decrypted  :" + plaintext.hex())

# encrypt
def aes_cbc_encrypt(key, iv, text):
  cipher = AES.new(key, AES.MODE_CBC, iv)
  ciphertext = cipher.encrypt(text)
  return ciphertext

# decrypt
def aes_cbc_decrypt(key, iv, ciphertext):
  plaintext = 0
  cipher = AES.new(key, AES.MODE_CBC, iv)
  try:
    plaintext = cipher.decrypt(ciphertext)
  except (ValueError, KeyError):
    print("Incorrect decryption")
  return plaintext

if __name__ == '__main__':
  main()
