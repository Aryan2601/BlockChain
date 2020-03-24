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
            hash_operation = str(hashlib.sha256(new_proof**2 - previous_proof**2).encode())   # here this is the operation for finding the value by solving this         #here this will be a string of 64 character it will take new proof and checkproof

# Part 2 - Mining our Blockchain