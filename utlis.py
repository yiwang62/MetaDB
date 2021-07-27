import os
import shutil


def exfilelist(_outdir):
  if not os.path.exists(_outdir):
    os.mkdir(_outdir)
  list = os.listdir(_outdir)
  list = [i for i in list if i.endswith('.VASP')]
  return list


def outputfiles(spname, _exfilelist, outdir):
  head,tail = os.path.split(spname)
  ff0=tail.split('+')
  pname = ff0[0]+'+'+ff0[1]
  for file in _exfilelist:
    if file.startswith(pname) : return
  shutil.copy(spname, os.path.join(outdir,tail))


def setoutdir(pdir):
  if pdir=="":
    pdir = "MP"
    i = 0
    posdir = pdir + str(i)
    #print ( os.path.isdir(posdir), os.path.isfile(posdir), os.path.exists(posdir) )
    while ( os.path.exists(posdir) ):
      i += 1
      posdir = pdir + str(i)
    os.mkdir(posdir)
  elif (os.path.isdir(pdir)):
    posdir = pdir
  elif os.path.isfile(pdir):
    print("file with the same name exist! please give another name!")
    sys.exit(1)
  elif not os.path.exists(pdir):
    posdir = pdir
    os.mkdir(posdir)
  return posdir