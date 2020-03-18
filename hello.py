#!/usr/bin/python
import subprocess as sbp
print ("Hello Word from pavans project forked by Babith")
print("**"*30)
print("Script running with details")
result = sbp.check_output('top -n 1', stderr = sbp.STDOUT, shell=True)
print("**"*30)
print(result)
print("**"*30)

