#𝗔 𝗨 𝗧 𝗢 𝗦 𝗛 𝗔 𝗥 𝗘 𝗧 𝗢 𝗢 𝗟 

#𝗢 𝗣 𝗘 𝗡  𝗦 𝗢 𝗨 𝗥 𝗖 𝗘  𝗖 𝗢 𝗗 𝗘  

#𝗠 𝗢 𝗗 𝗜 𝗙 𝗜 𝗘 𝗗  𝗕 𝗬 : 𝗬 𝗔 𝗦



import os, sys, subprocess, argparse, random, time, marshal, lzma, gzip, bz2, binascii, zlib

def encode(source: str) -> str:
    mode = random.choice((lzma, gzip, bz2, binascii, zlib))
    obf = marshal.dumps(compile(source, "Komachi", "exec"))
    if mode is binascii:
        return "import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64({})))".format(binascii.b2a_base64(obf))
    return "import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads({}.decompress({})))".format(mode.__name__, mode.compress(obf))

def inputs():
    file1 = input(" Enter input filename : ")
    file2 = input(" Enter output filename : ")
    complexity = int(input(" Enter Complexity (recommended: 100): "))
    return file1, file2, complexity

def main():
    file1, file2, complexity = inputs()
    print(f' Encrypting : {file1} => {file2}')
    with open(file1) as iput:
        for i in range(complexity):
            if i == 0:
                encoded = encode(source=iput.read())
            else:
                encoded = encode(source=encoded)
                time.sleep(0.1)
    with open(file2, "w") as output:
        output.write(f'try:\n\t{encoded}\nexcept KeyboardInterrupt:\n\texit()')
    print(f' Encrypted successful! saved as : {file2}\n — yas')

main()
