from encryption import get_encryption_key, encrypt, decrypt
from decorators import logged_in

@logged_in
def main(user: str, pw: str) -> None:
  print("login success")
  return None


if __name__ == "__main__":
  pass
  # msg_utf = "testing 1 2 3 in the place to be"
  # key = get_encryption_key()
  # msg_enc_b = encrypt(msg_utf, key)
  # print(msg_enc_b)
  # msg = decrypt(msg_enc_b, key)
  # print(msg)
  main(user='NeoPythonProjects', pw='LouNPP@17')
  