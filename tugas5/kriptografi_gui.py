import streamlit as st
from Crypto.Cipher import DES, AES
from Crypto.PublicKey import RSA, ElGamal
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import GCD, getPrime

st.title("Aplikasi Kriptografi: DES, AES, RSA, ElGamal")

menu = st.sidebar.selectbox("Pilih Algoritma", ["DES", "AES", "RSA", "ElGamal"])

# === DES ===
if menu == "DES":
    st.header("Algoritma DES")
    key = st.text_input("Kunci (8 karakter)", max_chars=8, value="8bytekey")
    data = st.text_input("Pesan (8 karakter)", max_chars=8, value="hello123")

    if st.button("Enkripsi DES"):
        cipher = DES.new(key.encode(), DES.MODE_ECB)
        encrypted = cipher.encrypt(data.encode())
        st.success(f"Ciphertext (hex): {encrypted.hex()}")

    if st.button("Dekripsi DES"):
        try:
            cipher = DES.new(key.encode(), DES.MODE_ECB)
            ciphertext_hex = st.text_input("Masukkan ciphertext (hex)")
            decrypted = cipher.decrypt(bytes.fromhex(ciphertext_hex))
            st.success(f"Plaintext: {decrypted.decode()}")
        except:
            st.error("Dekripsi gagal.")

# === AES ===
elif menu == "AES":
    st.header("Algoritma AES")
    key = st.text_input("Kunci (16 karakter)", max_chars=16, value="thisisakey123456")
    data = st.text_input("Pesan", value="pesan rahasia")

    if st.button("Enkripsi AES"):
        cipher = AES.new(key.encode(), AES.MODE_ECB)
        padded_data = pad(data.encode(), AES.block_size)
        encrypted = cipher.encrypt(padded_data)
        st.success(f"Ciphertext (hex): {encrypted.hex()}")

    if st.button("Dekripsi AES"):
        try:
            ciphertext_hex = st.text_input("Masukkan ciphertext (hex)")
            cipher = AES.new(key.encode(), AES.MODE_ECB)
            decrypted = unpad(cipher.decrypt(bytes.fromhex(ciphertext_hex)), AES.block_size)
            st.success(f"Plaintext: {decrypted.decode()}")
        except:
            st.error("Dekripsi gagal.")

# === RSA ===
elif menu == "RSA":
    st.header("Algoritma RSA")
    text = st.text_input("Masukkan pesan teks", value="pesan")

    if st.button("Generate Kunci & Enkripsi RSA"):
        rsa_key = RSA.generate(2048)
        public_key = rsa_key.publickey()
        ciphertext = public_key.encrypt(text.encode(), None)[0]
        st.session_state["rsa_key"] = rsa_key
        st.session_state["rsa_cipher"] = ciphertext
        st.success(f"Ciphertext (hex): {ciphertext.hex()}")

    if "rsa_key" in st.session_state and st.button("Dekripsi RSA"):
        private_key = st.session_state["rsa_key"]
        decrypted = private_key.decrypt(st.session_state["rsa_cipher"])
        st.success(f"Plaintext: {decrypted.decode()}")

# === ElGamal ===
elif menu == "ElGamal":
    st.header("Algoritma ElGamal")
    number = st.number_input("Masukkan angka sebagai pesan", min_value=1, value=123456)

    if st.button("Generate Kunci & Enkripsi ElGamal"):
        key = ElGamal.generate(1024, get_random_bytes)
        public_key = key.publickey()
        k = getPrime(512)
        while GCD(k, key.p - 1) != 1:
            k = getPrime(512)
        ciphertext = public_key.encrypt(number, k)
        st.session_state["elgamal_key"] = key
        st.session_state["elgamal_cipher"] = ciphertext
        st.success(f"Ciphertext: {ciphertext}")

    if "elgamal_key" in st.session_state and st.button("Dekripsi ElGamal"):
        key = st.session_state["elgamal_key"]
        decrypted = key.decrypt(st.session_state["elgamal_cipher"])
        st.success(f"Plaintext: {decrypted}")
