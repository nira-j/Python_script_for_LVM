import os
import subprocess

def menu():
    print("{:<10}to check disk attached with system".format("press 1"))
    print("{:<10}to create physical volume".format("press 2"))
    print("{:<10}to create volume group".format("press 3"))
    print("{:<10}to create logical volume".format("press 4"))
    print("{:<10}to display status of physical volume".format("press 5"))
    print("{:<10}to display status of volume group".format("press 6"))
    print("{:<10}to display status of logical volume".format("press 7"))

if __name__=="__main__":
    
    print("{:<10}for help".format("press h"))
    print("{:<10}for quit".format("press q"))
    while True:
        inp=input("Enter your choice:")
        if "1" in inp:
            os.system("fdisk -l")
        elif "2" in inp:
            i=input("Enter path of disk:")
            c="pvcreate "+i 
            os.system("c")

        elif "3" in inp:
            p_n=""
            v_n=input("Enter name of volume group:")
            i=int(input("Enter no. of physical volume to create volume group:"))
            for j in i:
                p_n +=input("Enter path of physical volume:")
                p_n=p_n+" "
            c="vgcreate "+v_n+p_n
            os.system(c)
        elif "4" in inp:
            lv_n=input("Enter name of logical volume:")
            vg_n=input("Enter name of volume group:")
            si=input("Enter size of logical volume:")
            c="lvcreate --size "+si+" --name "+lv_n+" "+vg_n
            os.system(c)
        elif "5" in inp:
            p_n=input("Enter name of physical volume:")
            os.system("pvdisplay "+p_n)
    
        elif "6" in inp:
            v_n=input("Enter name of volume group:")
            os.system("vgdisplay "+v_n)

        elif "7" in inp:
            l_n=input("Enter name of logical volume:")
            os.system("vgdisplay "+l_n)
        
        elif "h" in inp:
            menu()

        elif "q" in inp:
            break

        else:
            print("Invalid option choosed by you.")