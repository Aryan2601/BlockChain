#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: aryan
"""
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building a Blockchain
class BlockChain:
    
    def __init__(self): # here we are initializing the block chain
        self.chain = [] #it is a list where we will append diffrent blocks that will be mined
        
        self.create_block(proof = 1, previous_hash = '0' ) #genesis block created by create block with proof 1 and prevous hash 0 
    
    def create_block(self, proof, previous_hash):#here previous hash is the key element that links two blocks in a row here we will take proof as this is what our create block function will give us
        block = {'index': len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),#to check at what date and time the changes where made
                 'proof': proof,
                 'previous_hash': previous_hash,}
        self.chain.append(block)
        return block 
    def get_previous_block(self):
        return self.chain[-1] 
    
    def proof_of_work(self, previous_proof): # it is a piece of data where minors have to in oreder to mine a new block here function takes two argument self and previuos 
    #proof which is element of problem to be solved by minors
        new_proof = 1                        # here we will define a problem which minors have to solve and mine inside the block
        check_proof = False                  #here it will check if the new proof is the right proof
        while check_proof is False:          #here the wile loop will work unless the checkproof becomes true
            hash_operation = str(hashlib.sha256(new_proof**2 - previous_proof**2).encode()).hexdigest   # here this is the operation for finding the value by solving this         
            #here this will be a string of 64 character it will take new proof and checkproof
             #by adding here hexdigest we get the encode value in hexadecimal if we solve newproof and previuos proof and encode it then we will convert it to hexdecimal
            if hash_operation[:4] == "0000":    #if first four character of this hash are 0000 if that happens minor wins and check proof will be set to true  
                check_proof = True 
            else: 
                new_proof += 1
        return new_proof 
    def hash(self, block): #it will take a block as input and return the sha256
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    def is_chain_valid(self,chain):
        previous_block = chain(0)
        block_index = 1
        while block_index < len(chain):
            
            block = chain(block_index)                # here we will check if the hash of the block is equal to the previuos hash of the other block
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            #now we will check if previous proof and the proof of the block starts with 4 leading zeros
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest
            if hash_operation[:4] != '0000':
                return False 
            previous_block = block
            block_index += 1
        return True
# Part 2 - Mining our Blockchain