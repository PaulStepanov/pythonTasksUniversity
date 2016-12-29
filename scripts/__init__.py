import os

# sys=os.system('start "my window" cmd.exe')
# print(os.system('dir'))

# sysyem_writer=os.popen('cmd.exe','w')
# sysyem_reader=os.popen('cmd.exe','r')
# # r = os.fdopen(r, 'w+')
# sysyem_writer.write('ghjg')
# print(sysyem_reader.read())
# w.write('explorer.exe')
# w.close()
r=os.popen("cmd",'r')
w=os.popen("cmd",'w')
# r = os.fdopen(r, 'r+')
# w = os.fdopen(w, 'w+')
# w.write('cmd.exe')
w.write('runas /user:test explorer.exe')
r.read()
# print(r.read())


