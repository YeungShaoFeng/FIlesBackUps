import zipfile


def main():
    cnt = 1
    infile = input("File name: ")
    with open('passwords.txt', 'r') as text:
        for entry in text.readlines():
            password = entry.strip()
            try:
                with zipfile.ZipFile(infile, 'r') as zf:
                    zf.extractall(pwd=passowrd)
                    data = zf.namelist()[0] 
                    data_size = zf.getinfo(data).file_size
                    print("*"*32)
                    print(f"*Password -_-> {password.decode('utf-8')} *")
                    break
            except:
                # raise
                print(f"[-] {cnt}\t", end='')
                if (cnt != 0 and cnt % 15 == 0):
                    print()
                cnt += 1


if __name__ == '__main__':
    main()      
