import os
import platform

print("""
Python program to automate LVM
""")

if platform.system()=='Linux':
    print("Creating physical volumes....")
    vols=input("Give the volume names saparated by ',' which you want to make them as physical volumes : ")
    for i in vols.split(","):
        os.system("pvcreate {}".format(i))
        print("Created physical volume {}".format(i))
    print("Creating volume group...")
    vols=input("Give the volumes saparated by ',' that you wanted to group : ")
    vol_grp=input("Give the name of the volume group : ")
    cmd="vgcreate "+vol_grp
    for i in vols.split(","):
        cmd=cmd+' '+i
    os.system(cmd)
    print("Volume group is created...")
    print("Creating a logical volume...")
    lv=input("Give the logical volume that you wanted to create : ")
    size=input("Give the size of the logical volume you want to create in GiB : ")
    os.system('lvcreate --size {0} /dev/{}/{}'.format(size,vol_grp,lv))
    print("Created the logical volume...")
else:
    print("OS not supported")