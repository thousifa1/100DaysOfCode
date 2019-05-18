import sys
"""
Script      : decimal_to_baseN.py
Description : This script computes the Base N of a decimal integer 
usage       : python decimal_to_baseN.py number base
Author      : Thousif Ameer Khan  
"""
def compute_N (m,n):
	res=''
	while(m>0):
		rem=m%n
		m=m//n
		res=str(rem)+res
	return res	

def main():
	number=int(sys.argv[1])
	base=int(sys.argv[2])
	print (compute_N(number,base))

if __name__ == '__main__':
	main()