# https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html
# https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
# https://www.ietf.org/rfc/rfc6979.txt
# A.2.5.  ECDSA, 256 Bits (Prime Field)
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

VAR_PATH = "./var/"
Q = FFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551
X = C9AFA9D845BA75166B5C215767B1D6934E50C3DB36E89B127B8A622B120F6721
UX = 60FED4BA255A9D31C961EB74C6356D68C049B8923B61FA6CE669622E60F29FB6
UY = 7903FE1008B8BC99A41AE9E95628BC64F2F1B20C2D7E9F5177A3C294D4462299
def main():

  # read variables
  # with  open(VAR_PATH + "key.txt") as fk, \
  #       open(VAR_PATH + "data.txt") as fd, \
  #       open(VAR_PATH + "iv.txt") as fi:
    # key_org = bytearray.fromhex(fk.read())
#     iv = bytearray.fromhex(fi.read())
#     data = bytearray.fromhex(fd.read())
  # key = ECC.generate(curve='P-256')
  key = ECC.EccKey(curve='P-256', point_x = UX, point_y = UY, d = Q, seed = 32)

  print(key)
  # message = b'I give my permission to order #4355'
  # key = ECC.import_key(open('privkey.der').read())
  # key = ECC.import_key(key_org)
  # h = SHA256.new(message)
  # signer = DSS.new(key, 'fips-186-3')
  # signature = signer.sign(h)
  # print(signature)
#   # aes-cbc
#   ciphertext = aes_cbc_encrypt(key, iv, data)
#   plaintext = aes_cbc_decrypt(key, iv, ciphertext)

#   # result
#   print("data       :" + data.hex())
#   print("key        :" + key.hex())
#   print("iv         :" + iv.hex())
#   print("encrypted  :" + ciphertext.hex())
#   print("decrypted  :" + plaintext.hex())

# # encrypt
# def aes_cbc_encrypt(key, iv, text):
#   cipher = AES.new(key, AES.MODE_CBC, iv)
#   ciphertext = cipher.encrypt(text)
#   return ciphertext

# # decrypt
# def aes_cbc_decrypt(key, iv, ciphertext):
#   plaintext = 0
#   cipher = AES.new(key, AES.MODE_CBC, iv)
#   try:
#     plaintext = cipher.decrypt(ciphertext)
#   except (ValueError, KeyError):
#     print("Incorrect decryption")
#   return plaintext

if __name__ == '__main__':
  main()
