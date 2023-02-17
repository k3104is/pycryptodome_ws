# https://telecom-engineer.blog/blog/2022/05/06/python-aes-gcm/
# https://csrc.nist.rip/groups/ST/toolkit/BCM/documents/proposedmodes/gcm/gcm-spec.pdf
# test case 15
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

VAR_PATH = "./var/"

def main():
  # read variables
  with  open(VAR_PATH + "key.txt") as fk, \
        open(VAR_PATH + "data.txt") as fd, \
        open(VAR_PATH + "iv.txt") as fi:
    key = bytearray.fromhex(fk.read())
    nonce = bytearray.fromhex(fi.read())
    data = bytearray.fromhex(fd.read())

  # aes-gcm256
  ciphertext, mac = aes_gcm_encrypt(key,nonce,data)
  plaintext = aes_gcm_decrypt(key,nonce,ciphertext,mac)

  # result
  print("data\t\t:" + data.hex())
  print("key\t\t:" + key.hex())
  print("iv\t\t:" + nonce.hex())
  print("encrypted\t:" + ciphertext.hex())
  print("tag\t\t:" + mac.hex())
  print("decrypted\t:" + plaintext.hex())

# encrypt
def aes_gcm_encrypt(key,iv,text):
  cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
  ciphertext, mac = cipher.encrypt_and_digest(text)
  return ciphertext, mac

# decrypt
def aes_gcm_decrypt(key,iv,ciphertext,mac):
  plaintext = 0
  cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
  try:
    plaintext = cipher.decrypt_and_verify(ciphertext,mac)
  except (ValueError, KeyError):
    print("Incorrect decryption")
  return plaintext

if __name__ == '__main__':
  main()
