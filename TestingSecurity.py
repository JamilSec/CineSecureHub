from Padlook import Padlook
padlook = Padlook()

# Crear una instancia de la clase Padlook
padlook = Padlook()

# Cadena de texto a cifrar
texto_original = "Hola, esta es una cadena de texto que será cifrada."

# Cifrar el texto
texto_cifrado = padlook.encrypt(texto_original)
print("Texto cifrado:", texto_cifrado)

# Descifrar el texto
texto_descifrado = padlook.decrypt(texto_cifrado)
print("Texto descifrado:", texto_descifrado)