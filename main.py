from encryption import get_encryption_key, encrypt, decrypt



if __name__ == "__main__":
  msg_utf = "testing 1 2 3 in the place to be"
  key = get_encryption_key()
  msg_enc_b = encrypt(msg_utf, key)
  print(msg_enc_b)
  msg = decrypt(msg_enc_b, key)
  print(msg)

  