# https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html
# https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
# https://www.ietf.org/rfc/rfc6979.txt
# A.2.5.  ECDSA, 256 Bits (Prime Field)
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

VAR_PATH = "./var/"
# Q = FFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551
X = 0xC9AFA9D845BA75166B5C215767B1D6934E50C3DB36E89B127B8A622B120F6721
UX = 0x60FED4BA255A9D31C961EB74C6356D68C049B8923B61FA6CE669622E60F29FB6
UY = 0x7903FE1008B8BC99A41AE9E95628BC64F2F1B20C2D7E9F5177A3C294D4462299
k = 0xA6E3C57DD01ABE90086538398355DD4C3B17AA873382B0F24D6129493D8AAD60
message = b'sample'

def main():

  # read variables
  # with  open(VAR_PATH + "key.txt") as fk, \
  #       open(VAR_PATH + "data.txt") as fd, \
  #       open(VAR_PATH + "iv.txt") as fi:
    # key_org = bytearray.fromhex(fk.read())
#     iv = bytearray.fromhex(fi.read())
#     data = bytearray.fromhex(fd.read())
  # key = ECC.generate(curve='P-256')
  ecckey = ECC.construct(curve='P-256', d = X, point_x = UX, point_y = UY)
  # ecckey = ECC.EccKey(curve='P-256', pointQ.x = UX, pointQ.y = UY, d = X)

  print(ecckey)
  h = SHA256.new(message)
  print(h)
  signer = DSS.new(ecckey, 'deterministic-rfc6979')
  signature = signer.sign(h)
  print(signature.hex())

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
