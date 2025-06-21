import base64

def xor_cipher(text, key):
    # Repete a senha para cobrir o tamanho do texto
    key_repeated = (key * (len(text) // len(key) + 1))[:len(text)]
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key_repeated))

def encrypt(plain_text, key):
    encrypted = xor_cipher(plain_text, key)
    encrypted_b64 = base64.urlsafe_b64encode(encrypted.encode()).decode()
    return encrypted_b64

def decrypt(encrypted_b64, key):
    try:
        encrypted = base64.urlsafe_b64decode(encrypted_b64.encode()).decode()
        decrypted = xor_cipher(encrypted, key)
        return decrypted
    except Exception as e:
        return f"Erro ao descriptografar: {e}"

def main():
    print("O que você deseja fazer?")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    choice = input("Escolha (1 ou 2): ")

    if choice == "1":
        text = input("Digite o texto para criptografar: ")
        key = input("Digite uma senha para criptografar: ")
        encrypted = encrypt(text, key)
        print("\nTexto criptografado:")
        print(encrypted)

    elif choice == "2":
        encrypted = input("Digite o texto criptografado: ")
        key = input("Digite a senha usada na criptografia: ")
        decrypted = decrypt(encrypted, key)
        print("\nTexto descriptografado:")
        print(decrypted)

    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
