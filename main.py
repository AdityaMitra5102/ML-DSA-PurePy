from dilithium_py.ml_dsa import ML_DSA_44
print('import done')
pk, sk = ML_DSA_44.keygen()
print('keygen done')
print('public key')
print(pk)
print('private key')
print(sk)
msg=b'dummy msg'
sig = ML_DSA_44.sign(sk, msg)
print('signing complete')
print('signature')
print(sig)
assert ML_DSA_44.verify(pk, msg, sig)