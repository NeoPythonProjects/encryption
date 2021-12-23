from cryptography.fernet import Fernet


def create_encryption_key() -> None:
  # using symmetric encryption
  # generate a key for encryption and decryption
  # store this key safely
  with open('files/scratch.txt','w') as f:
    f.write(Fernet.generate_key()) 
    f.close()
  # don't recreate every time
  return None


def get_encryption_key():
  #read from textt file for now, but read from USB
  # in GUI ask user to select text fiel to upload
  # for now, we use the scratch File
  src_file = 'files/scratch.txt'
  with open(src_file,'r') as f:
    key = f.readline()
    f.close()
    return key


def encrypt(msg_utf: str, key: str):
  # Instance the Fernet class with the key

  fernet = Fernet(key)

  # then use the Fernet class instance
  # to encrypt the byte version of the string
  msg_enc_b = fernet.encrypt(msg_utf.encode())
  return (msg_enc_b, fernet)
  #print("original string: ", msg_utf)
  #print("encrypted string: ", msg_enc_b)

def decrypt(msg_enc_b, fernet):
  # decrypt the encrypted string with the
  # Fernet instance of the key,
  # that was used for encrypting the string
  # encoded byte string is returned by decrypt method,
  # so decode it to string with decode methods
  msg_dec_utf = fernet.decrypt(msg_enc_b).decode()
  return msg_dec_utf


if __name__ == "__main__":
  pass
  msg_utf = "test string to encrypt"
  msg_enc_b, fernet = encrypt(msg_utf)
  print(msg_enc_b)
  msg = decrypt(msg_enc_b, fernet)
  print(msg)

  