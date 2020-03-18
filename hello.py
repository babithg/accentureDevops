import subprocess as sbp
print ("Hello Word from pavans project forked by Babith")
print("**"*10)
print("Script running with details")
result = sbp.check_output('top -n 1', shell=True)
print(result)
print("**"*10)

