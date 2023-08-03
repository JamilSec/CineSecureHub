from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from binascii import hexlify, unhexlify

class Padlook:
    def __init__(self):
        self.KEY = "".encode('utf-8')
        self.ivx = "".encode('utf-8')

    def encrypt(self, plaintext):
        cipher = AES.new(self.KEY, AES.MODE_CBC, self.ivx)
        padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
        ciphertext = cipher.encrypt(padded_data)
        return hexlify(ciphertext).decode('utf-8')

    def decrypt(self, ciphertext):
        cipher = AES.new(self.KEY, AES.MODE_CBC, self.ivx)
        ciphertext_bytes = unhexlify(ciphertext)
        decrypted_data = cipher.decrypt(ciphertext_bytes)
        unpadded_data = unpad(decrypted_data, AES.block_size)
        return unpadded_data.decode('utf-8')

    @staticmethod
    def bytes_to_hex(byte_array):
        return hexlify(byte_array).decode('utf-8')

    @staticmethod
    def hex_string_to_byte_array(hex_string):
        return unhexlify(hex_string)