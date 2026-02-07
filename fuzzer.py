#!/usr/bin/env

import subprocess

def run_binary(payload):
	result = subprocess.run(
		['./binaries/vuln1'],
		input = payload,
		capture_output = True,
		timeout = 5
	)
	return result.returncode == -11
	
# Test 1, normal input
for i in range(2):
	usr_str = ""
	if i == 0:
		print("Test 1: Sending 'Hello'")
		usr_str = b"hello"
	if i == 1:
		print("Test 2: Sending buffer of 100 A's")
		usr_str = b"A" * 100
	crashed = run_binary(usr_str)
	if crashed:
		print("Result: The program crashed!")
	else:
		print("Result: The program didn't crash!")


	
		
