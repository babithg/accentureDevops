#!/usr/bin/python
import subprocess as sbp
print ("Hello Word from pavans project forked by Babith")
print("**"*30)
print("Script running with details")
try:
	result = sbp.check_output('top -n 1', stderr = sbp.STDOUT, shell=True)
except sbp.CalledProcessError as e:
	raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

print("**"*30)
print(result)
print("**"*30)

