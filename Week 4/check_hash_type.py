import re
import sys

HASH_TYPE_REGEX = {
    re.compile(r"^[a-f0-9]{32}(:.+)?$", re.IGNORECASE):  ["MD5", "MD4", "MD2", "Double MD5",
                                                          "LM", "RIPEMD-128", "Haval-128",
                                                          "Tiger-128", "Skein-256(128)", "Skein-512(128",
                                                          "Lotus Notes/Domino 5", "Skype", "ZipMonster",
                                                          "PrestaShop"],
    re.compile(r"^[a-f0-9]{64}(:.+)?$", re.IGNORECASE):  ["SHA-256", "RIPEMD-256", "SHA3-256", "Haval-256",
                                                          "GOST R 34.11-94", "GOST CryptoPro S-Box",
                                                          "Skein-256", "Skein-512(256)", "Ventrilo"],
    re.compile(r"^[a-f0-9]{128}(:.+)?$", re.IGNORECASE): ["SHA-512", "Whirlpool", "Salsa10",
                                                          "Salsa20", "SHA3-512", "Skein-512",
                                                          "Skein-1024(512)"],
    re.compile(r"^[a-f0-9]{56}$", re.IGNORECASE):        ["SHA-224", "Haval-224", "SHA3-224",
                                                          "Skein-256(224)", "Skein-512(224)"],
    re.compile(r"^[a-f0-9]{40}(:.+)?$", re.IGNORECASE):  ["SHA-1", "Double SHA-1", "RIPEMD-160",
                                                          "Haval-160", "Tiger-160", "HAS-160",
                                                          "LinkedIn", "Skein-256(160)", "Skein-512(160)",
                                                          "MangoWeb Enhanced CMS"],
    re.compile(r"^[a-f0-9]{96}$", re.IGNORECASE):        ["SHA-384", "SHA3-384", "Skein-512(384)",
                                                          "Skein-1024(384)"],
    re.compile(r"^[a-f0-9]{16}$", re.IGNORECASE):        ["MySQL323", "DES(Oracle)", "Half MD5",
                                                          "Oracle 7-10g", "FNV-164", "CRC-64"],
    re.compile(r"^\*[a-f0-9]{40}$", re.IGNORECASE):      ["MySQL5.x", "MySQL4.1"],
    re.compile(r"^[a-f0-9]{48}$", re.IGNORECASE):        ["Haval-192", "Tiger-192", "SHA-1(Oracle)",
                                                          "XSHA (v10.4 - v10.6)"]
}


class HashChecker(object):

    def __init__(self, check_hash):
        self.hash = check_hash
        self.found = False

    def obtain_hash_type(self):
        for algorithm in HASH_TYPE_REGEX:
            if algorithm.match(self.hash):
                self.found = True
                self.enumerate_hash_types(HASH_TYPE_REGEX[algorithm])
        if self.found is False:
            error_message = "Unable to verify hash type "
            error_message += "for hash: '{}'. This could mean ".format(self.hash)
            error_message += "that this is not a valid hash, or that "
            error_message += "this hash is not supported by Pybelt "
            error_message += "yet. If you feel this should be supported "
            error_message += "make an issue regarding this hash."
            print(error_message)
            return

    @staticmethod
    def enumerate_hash_types(items):
        print("{} possible hash types found..".format(len(items)))
        count = 0
        for item in items:
            count += 1
            if count <= 3:
                print("\033[92m[*] Most likely possible hash type: {}\033[0m".format(item))
                if count == 3:
                    print("")
            else:
                print("\033[33m[*] Least likely possible hash type: {}\033[0m".format(item))


if __name__ == '__main__':
    print("Analyzing hash: {}".format(sys.argv[1]))
    HashChecker(str(sys.argv[1])).obtain_hash_type()