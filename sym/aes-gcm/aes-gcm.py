# https://telecom-engineer.blog/blog/2022/05/06/python-aes-gcm/
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#ccm-mode
# https://csrc.nist.rip/groups/ST/toolkit/BCM/documents/proposedmodes/gcm/gcm-spec.pdf
# test case 15
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

  # aes-gcm256
  ciphertext, mac = aes_gcm_encrypt(key, iv, data)
  plaintext = aes_gcm_decrypt(key, iv, ciphertext, mac)

  # result
  print("data       :" + data.hex())
  print("key        :" + key.hex())
  print("iv         :" + iv.hex())
  print("encrypted  :" + ciphertext.hex())
  print("tag        :" + mac.hex())
  print("decrypted  :" + plaintext.hex())

# encrypt
def aes_gcm_encrypt(key, iv, text):
  cipher = AES.new(key, AES.MODE_GCM, iv)
  ciphertext, mac = cipher.encrypt_and_digest(text)
  return ciphertext, mac

# decrypt
def aes_gcm_decrypt(key, iv, ciphertext, mac):
  plaintext = 0
  cipher = AES.new(key, AES.MODE_GCM, iv)
  try:
    plaintext = cipher.decrypt_and_verify(ciphertext, mac)
  except (ValueError, KeyError):
    print("Incorrect decryption")
  return plaintext

if __name__ == '__main__':
  main()
