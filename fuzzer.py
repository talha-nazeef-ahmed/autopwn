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
	
	
def check_crash():
	for i in range(10, 210, 10):
		payload = b"A" * i
		check = run_binary(payload)
		print(f"[*] Checking crash With {i} bytes...")
		if check:
			print(f"[+] Crashed at size between {i-10} - {i} bytes")
			for j in range(i-10, i+1, 1):
				new_payload = b"A" * j
				recheck = run_binary(new_payload)
				print(f"[*] Pin pointing exact crash bytes...")
				print(f"[*] Checking crash With {j} bytes...")
				if recheck:
					print(f"[+] Crashed at {j} bytes")
					return j
			
		else:
			print(f"[-] Bytes {i} OK")
			
	print("[-] No Crash found\nFuzzer Ended!")
	return -1


print("\n")
print("=" * 40)
print("[*] Starting the Fuzzer")
print("=" * 40)
print("\n")
size = check_crash()

#Size don't have any function for now but maybe for future, for now its there to just store the size where crashed if any 


			
			


	
		
