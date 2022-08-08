from pycoin.ecdsa.secp256k1 import secp256k1_generator
import hashlib, secrets

def sha3_256Hash(msg):
	   hashBytes = hashlib.sha3_256(msg.encode("utf8")).digest()
	   return int.from_bytes(hashBytes, byteorder="big")

def signECDSAsecp256k1(msg, privKey):
	    msgHash = sha3_256Hash(msg)
	    signature = secp256k1_generator.sign(privKey, msgHash)
	    return signature

def verifyECDSAsecp256k1(msg, signature, pubKey):
	    msgHash = sha3_256Hash(msg)
	    valid = secp256k1_generator.verify(pubKey, msgHash, signature)
	    return valid

def recoverPubKeyFromSignature(msg, signature):
    msgHash = sha3_256Hash(msg)
    recoveredPubKeys = secp256k1_generator.possible_public_pairs_for_signature(msgHash, signature)
    return recoveredPubKeys

msg = "Message for ECDSA signing"
privKey = secrets.randbelow(secp256k1_generator.order())
signature = signECDSAsecp256k1(msg, privKey)

recoveredPubKeys = recoverPubKeyFromSignature(msg, signature)
print("\nMessage:", msg)
print("Signature: r=" + hex(signature[0]) + ", s=" + hex(signature[1]))
for pk in recoveredPubKeys:
    print("Recovered public key from signature: (" +
          hex(pk[0]) + ", " + hex(pk[1]) + ")")