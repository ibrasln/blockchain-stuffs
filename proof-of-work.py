from hashlib import sha256
import time

def proof_of_work(prev_nonce):
    new_nonce = 1
    nonce = 1
    difficulty = 4
    
    while True:
        computed_hash = sha256(str(new_nonce ** 2 - prev_nonce ** 2).encode()).hexdigest() 
        print(f"Nonce {nonce} : {computed_hash}")
        if computed_hash.startswith('0' * difficulty):
            congratulations(nonce, computed_hash)
            print("Get ready, we are starting..")
            prev_nonce = new_nonce
            new_nonce = 1
            nonce = 1
            time.sleep(2)
        else:
            new_nonce += 1
            nonce += 1

def congratulations(nonce, hash):
    print('Congratulations, you found the Golden Nonce!!')
    time.sleep(2)
    print(f"The Golden Nonce is {nonce}")
    time.sleep(2)
    print(f"The hash is {hash}")    
    time.sleep(2)


proof_of_work(1)