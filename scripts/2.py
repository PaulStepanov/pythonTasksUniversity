import subprocess,os
# p1 = subprocess.Popen(["cmd.exe", "This_is_a_testing"], stdout=subprocess.PIPE)
# var = subprocess.Popen('', stdin=p1.stdout, stdout=subprocess.PIPE)
# os.system(cmd)
# os.fdopen(var, 'w+')
# print(help(var))
import os, sys,subprocess
#
# using command mkdir
task = subprocess.Popen("cd E:\stuff", shell=True, stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE,)
print(task.communicate())
task = subprocess.Popen("npm init", shell=True, stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE,)
print(task.stdin.write('gjl'.encode('CP1251')))
print(task.stdin.flush())
print(task.stdout.readline(-1))
print(task.stdin.write('1.0.0'.encode('CP1251')))
print(task.stdin.flush())
# print(task.communicate('^C'.encode('CP1251'))[0])
task = subprocess.Popen("name", shell=True, stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE,)

# task.stdin.write(bytearray('dir',encoding='CP1251'))
# task.stdin.close()
# print(task.stdout.readline())
# print(task.stdout.readline())
# print(task.stdout.readline())
# print(task.stdout.readline())
# print(task.stdout.readline())
# print(task.stdout.readline())
# print(task.stdout.readline())
# print(task.stdout.readline())
# b = subprocess.Popen(a,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)

