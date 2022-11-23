import os, sys
from binascii import hexlify, unhexlify
sys.path.append('../libraries')
import utils
import ed25519
import base58

def generate_random_address():
    ## generate 32 bytes (256 bits) of pseudo-random data
    seed = hexlify(os.urandom(32))

    ## reduce random data to make it a valid ed25519 scalar
    secret_spend_key = utils.sc_reduce32(seed)

    ## use a reduced hash of the secret spend key for the deterministic secret view key
    secret_view_key = utils.hash_to_scalar(secret_spend_key)

    ## multiply by the generator point to get public keys from private keys
    public_spend_key = utils.publickey_to_privatekey(secret_spend_key)
    public_view_key  = utils.publickey_to_privatekey(secret_view_key)

    ## the network byte, public spend key, and public view key are all concatenated together
    ## 0x12 is the Monero mainnet network byte
    network_byte = b'12'
    ## Concatenate the three strings
    data = network_byte + public_spend_key + public_view_key
    hash = utils.keccak_256(data)
    ## checksum is the first 4 bytes (8 hex characters) of the hash of the previous data
    checksum = hash[0:8]
    print("checksum : " + checksum)
    address = base58.encode(data + checksum.encode('utf-8'))
    
    ## Priting the keys
    
    print("Secret_spend_key : " + secret_spend_key.decode('utf-8'))
    print("Secret_view_key : " + secret_view_key.decode('utf-8'))
    print("Public_spend_key : " + public_spend_key.decode('utf-8'))
    print("Public_view_key : " + public_view_key.decode('utf-8'))
    
    ## Returning address generated
    print("Monero address : " + address)
    return address

generate_random_address()

