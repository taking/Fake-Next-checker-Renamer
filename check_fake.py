#!/usr/bin/env python
#-*- coding:utf-8 -*-

from subprocess import check_output
import re, os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="target directory. ex) python check_fake.py /Downloads/", default="")

args = parser.parse_args()

PATH = args.dir

print("Check Library Path:", PATH)
notfake=[]
fake=[]
print("finding and renaming started...")
for p,w,f in os.walk(PATH):
	for file_name in f:
		if file_name[-9:]=='-NEXT.mp4':
			print('processing %s' %os.path.join(p,file_name))
			path = os.path.join(p,file_name)
			a = str(check_output('ffmpeg -i "'+path+'" 2>&1 | grep "encoder"', shell=True))
			a = a.split(',')[0].split("encoder")[1].strip()
			if(a[2] == "M"):
				print("NOT FAKE")
				notfake.append(file_name)	# NOT FAKE NEXT
			else:
				print("FAKE")
				fake.append(file_name) 		# FAKE NEXT
				rename = re.sub('-NEXT', '', file_name)
				os.rename(os.path.join(p,file_name), os.path.join(p,rename))

check_list = list(set(notfake) | set(fake))
print('\nfound NEXT files:')
for check in check_list:
	print(check)

print('\n(found FAKE) renamed files:')
for check in fake:
	print(check)
