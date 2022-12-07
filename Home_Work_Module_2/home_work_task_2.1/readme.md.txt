# PART 1. HYPERVISORS
1. VMware vSphere, Microsoft Hyper-V Server, Citrix XenServer are the most popular.
2. Hypervisors are divided into type 1 and type 2. Type 1 runs on pure hardware and Type 2 floors the operating system.
VMware vSphere provides a powerful, flexible and secure foundation for next-generation applications, helping to achieve effective digital transformation. Microsoft Hyper-V Server is an embedded hypervisor, with server virtualisation as its primary role. Citrix XenServer is based on the open source Xen hypervisor, widely used across industries and with a proven track record of stability and performance.


# PART 2. WORK WITH VIRTUALBOX
First run VirtualBox and Virtual Machine (VM). 1.1 Get acquainted with the structure of the user manual VirtualBox[1](see list of references in the end of the document)
1.2 From the official VirtualBox site [2] download the latest stable version of VirtualBox according to the host operating system (OS) installed on the student's workplace. For Windows, the file may be called, for example, VirtualBox-6.1.10-138449-Win.exe. Install VirtualBox.

1.3 Download the latest stable version of Ubuntu Desktop or Ubuntu Server from the official site [3].

1.4 Create VM1 and install Ubuntu using the instructions [1, chapter 1.8]. Set machine name as "host machine name"_"student last name"
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image1.4.png?raw=true)
 
1.5 Get acquainted with thepossibilities of VM1 control -start, stop, reboot, save state, use Host key and keyboard shortcuts, mouse capture, etc. [1, ch.1.9].
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image1.5.png)
1.6 Clone an existing VM1 by creating a VM2 [1, ch.1.14].
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image1.6.png)
1.7 Create a group of two VM: VM1, VM2 and learn the functions related to groups [1, ch.1.10].
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image1.7.png)
1.8 For VM1, changing its state, take several different snapshots, forming a branched tree of snapshots[1, ch.1.11].
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image1.8.png)
1.9 Export VM1. Save the *.ova file to disk. Import VM from *.ova file[1, ch.1.15].
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image1.9.png)
2.1 Explore VM configuration options (general settings, system settings, display, storage, audio, network, etc.).
 ![https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image2.1.png]
2.2 Configure the USB to connect the USB ports of the host machine to the VM [1, ch.3.11].
 ![https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image2.2.png]
2.3 Configure a shared folder to exchange data between the virtual machine and the host [1, ch.4.3].
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image2.3.png)
2.4 Configure different network modes for VM1, VM2. Check the connection between VM1, VM2, Host, Internet for different network modes. You can use the pingcommand to do this. Make a table of possible connections.

3.1 Run the cmd.exe command line.

3.2 Examine the purpose and execute the basic commands of VBoxManage list, showvminfo, createvm, startvm, modifyvm, clonevm, snapshot, controlvm[1, ch.8].
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image3.2.png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image3.2%201.png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image3.2%202.png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image3.2%203.png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image3.2%204.png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image3.2%205.png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image3.2%206.png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image3.2%207.png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image3.2%208.png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/image3.2%209.png)

# PART 3. WORK WITH VAGRANT

1.Download the required version of Vagrant according to the instructions [5] and according to the host operating system (OS) installed on the student's workplace. For Windows, the file may be called, for example, vagrant_2.2.0_x86_64.msi. Install Vagrant. Check the path to Vagrant bin in the Path variable (My computer -> Properties -> Advanced system settings -> Advanced -> Environment Variables).

2.Run the powershell. Create a folder "student name" (in English). In this example, create a folder vagrant_test. Next, go to the folder.

3.Initialize the environment with the default Vagrant box:init hashicorp/precise64
 ![]()
4.Run vagrant upand watch for messages during VM boot and startup.
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/imagePart3.4.png)
5.Connect to the VM using the program PuTTY (can be downloaded from [6]), using SSH, IP address and port listed above (127.0.0.1:2222). By default, login -vagrantand password are also vagrant
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/imagePart3.6.png)
6.Record the date and time by executing the datecommand
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/imagePart3.png)

7.Stop and delete the created VM.
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/imagePart3.7.png)

8.Create your own Vagrant box[7]
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/imagePart3.8.1.png)
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/imagePart3.8.2.png)


9.(optional)Createa test environment from a few servers. Servers' parameters are chosen independently by the student.
 https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/tree/main/m2/task2.1/multymachine
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/imagePart3.9.3.png)
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/imagePart3.9.2.png)
 ![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m2/task2.1/imagePart3.9.png)
