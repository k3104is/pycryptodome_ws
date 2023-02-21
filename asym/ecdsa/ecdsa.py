# https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html
# https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
# https://www.ietf.org/rfc/rfc6979.txt
# A.2.5.  ECDSA, 256 Bits (Prime Field)
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

VAR_PATH = "./var/"
message = b'sample'

def main():

  # read variables
  with  open(VAR_PATH + "x.txt") as fx, \
        open(VAR_PATH + "ux.txt") as fux, \
        open(VAR_PATH + "uy.txt") as fuy:
    x = int("0x" + fx.read(), 16)
    ux = int("0x" + fux.read(), 16)
    uy = int("0x" + fuy.read(), 16)
  
  # build a ECC key
  ecckey = ECC.construct(curve='P-256', d = x, point_x = ux, point_y = uy)
  # create hash val from message
  h = SHA256.new(message)
  # create signature object
  signer = DSS.new(ecckey, 'deterministic-rfc6979')
  # sign
  signature = signer.sign(h)
  # result
  print("x  :" + format(x, 'x'))
  print("ux :" + format(ux, 'x'))
  print("uy :" + format(uy, 'x'))
  print("r  :" + signature.hex()[0:64])
  print("s  :" + signature.hex()[64:128])

if __name__ == '__main__':
  main()
