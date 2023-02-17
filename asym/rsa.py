# https://self-development.info/【python暗号化】pycryptoではなくpycryptodomeを使う/
from Crypto.PublicKey import RSA
 
# 秘密鍵の作成
key = RSA.generate(2048)
private_key = key.export_key()
print(private_key)
#file_out = open("private.pem", "wb")
#file_out.write(private_key)
#file_out.close()
 
# 公開鍵の作成
public_key = key.publickey().export_key()
print(public_key)
#file_out = open("public.pem", "wb")
#file_out.write(public_key)
#file_out.close()
