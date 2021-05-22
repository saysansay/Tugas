import hashlib, binascii, os
'Fungsi encrypt password dengan hash dan salt python'
def encrypt_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    passhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    passhash = binascii.hexlify(passhash)
    'Menampilkan hasil sumber text dan Salt serta Hash'
    print('password ='+password +' salt ='+(salt).decode('ascii')+' Hash='+(passhash).decode('ascii'))
    'Mengambungkan salt dan hash sebagai hasil enskripsi'
    return (salt + passhash).decode('ascii')
'fungsi validasi password hash dan salt'
def validasi_password(saved_password, source_password):
    'mendapatkan nilai salt dari password yang terenkripsi'
    salt = saved_password[:64]
    saved_password = saved_password[64:]
    'mendapatkan nilai hash dari source password'
    passhash = hashlib.pbkdf2_hmac('sha512', 
                                  source_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    passhash = binascii.hexlify(passhash).decode('ascii')
    return passhash == saved_password
