#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 01:01:30 2020

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

# Part 2 - Mining our Blockchain