import os
import sys
import time


try:
    import pyzipper
except ImportError:
    print("[!] Module 'pyzipper' tidak ditemukan. Install dulu: pip install pyzipper")
    sys.exit(1)

try:
    import rarfile
except ImportError:
    print("[!] Module 'rarfile' tidak ditemukan. Install dulu: pip install rarfile")
    sys.exit(1)

try:
    from tqdm import tqdm
except ImportError:
    print("[!] Module 'tqdm' tidak ditemukan. Install dulu: pip install tqdm")
    sys.exit(1)

try:
    import argparse
except ImportError:
    print("[!] Module 'argparse' tidak ditemukan. Install dulu: pip install argparse")
    sys.exit(1)

try:
    from multiprocessing import Pool
except ImportError:
    print("[!] Module 'multiprocessing' tidak ditemukan. Install dulu:  pip install multiprocess")
    sys.exit(1)

def try_password_zip(args):
    zip_file, password = args
    try:
        with pyzipper.AESZipFile(zip_file) as zf:
            zf.extractall(pwd=password.encode('utf-8'))
        return password
    except Exception:
        return None

def try_password_rar(args):
    rar_file, password = args
    try:
        with rarfile.RarFile(rar_file) as rf:
            rf.extractall(pwd=password)
        return password
    except Exception:
        return None

def brute_force_file(file_path, passwords, max_workers, is_zip=True):
    start_time = time.time()
    task = try_password_zip if is_zip else try_password_rar
    total = len(passwords)
    found = False

    with Pool(max_workers) as pool:
        with tqdm(total=total, desc="Brute Force Progress", unit="pass", ncols=80) as pbar:
            for idx, result in enumerate(pool.imap_unordered(task, [(file_path, p) for p in passwords])):
                pbar.update(1)
                if result is not None:
                    elapsed = time.time() - start_time
                    pbar.close()         # Menutup progress bar agar tidak lanjut
                    pool.terminate()     # Stop semua worker
                    pool.join()          # Tunggu proses berhenti

                    print("\n" + "="*40)
                    print(f"[✓] {'ZIP' if is_zip else 'RAR'}: Password ditemukan: {result}")
                    print(f"\nTotal Attempt : {idx + 1} Percobaan")
                    print(f"[⏱️] Waktu eksekusi: {elapsed:.2f} detik")
                    print("="*40)
                    found = True
                    break

    if not found:
        print(f"\n[✗] {'ZIP' if is_zip else 'RAR'}: Password tidak ditemukan.")
    return found

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Brute Force ZIP/RAR Password (dengan progress & estimasi waktu)")
        parser.add_argument("-f", "--file", required=True, help="Nama file ZIP atau RAR")
        parser.add_argument("-w", "--wordlist", required=True, help="File wordlist")
        parser.add_argument("-t", "--threads", type=int, default=2, help="Jumlah worker (default: 2)")
        args = parser.parse_args()

        if not os.path.exists(args.file):
            print(f"[!] File tidak ditemukan: {args.file}")
            sys.exit(1)
        if not os.path.exists(args.wordlist):
            print(f"[!] Wordlist tidak ditemukan: {args.wordlist}")
            sys.exit(1)

        max_workers = max(1, args.threads)
        with open(args.wordlist, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]

        if args.file.lower().endswith(".zip"):
            brute_force_file(args.file, passwords, max_workers, is_zip=True)
        elif args.file.lower().endswith(".rar"):
            brute_force_file(args.file, passwords, max_workers, is_zip=False)
        else:
            print("[!] Format file tidak didukung. Gunakan .zip atau .rar")

    except KeyboardInterrupt:
        print("\n[!] Dihentikan oleh pengguna.")
        sys.exit(0)
