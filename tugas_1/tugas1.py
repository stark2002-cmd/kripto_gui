import os
import hashlib

# Daftar ekstensi file mencurigakan (sering digunakan oleh malware/trojan)
SUSPICIOUS_EXTENSIONS = ['.exe', '.bat', '.vbs', '.scr', '.pif', '.js']

# Daftar hash file yang diketahui berbahaya (simulasi)
KNOWN_BAD_HASHES = {
    'e99a18c428cb38d5f260853678922e03',  # Contoh hash md5
}

def scan_directory(path):
    print(f"🔍 Memindai direktori: {path}")
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            check_file(file_path)

def check_file(file_path):
    _, ext = os.path.splitext(file_path)

    # Deteksi berdasarkan ekstensi
    if ext.lower() in SUSPICIOUS_EXTENSIONS:
        print(f"[⚠️] File mencurigakan berdasarkan ekstensi: {file_path}")

    # Deteksi berdasarkan hash file
    file_hash = calculate_md5(file_path)
    if file_hash in KNOWN_BAD_HASHES:
        print(f"[🚨] File terdeteksi sebagai malware berdasarkan hash: {file_path}")

def calculate_md5(file_path):
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()
            return hashlib.md5(file_data).hexdigest()
    except Exception as e:
        print(f"[❌] Gagal membaca file: {file_path} | Error: {e}")
        return None

if __name__ == "__main__":
    target_folder = input("Masukkan path folder yang ingin dipindai: ")
    if os.path.exists(target_folder):
        scan_directory(target_folder)
    else:
        print("Folder tidak ditemukan.")
