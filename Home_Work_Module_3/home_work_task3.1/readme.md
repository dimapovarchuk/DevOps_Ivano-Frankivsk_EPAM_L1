1. Create networks as shown in Figure 1. The recommended switch models are Catalyst 2960, the wireless router is WRT300N. In the Data Center network, connect the servers to the ports according to Fig. 1.
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(1).png)
2. In the Enterprise network assign static addresses, formed according to the following rule: Network address 10.Y.D.0/24, where Y is the last two digits of your year of birth, D is your date of birth. The host part of the Client 1 address is 10, Client 2 is 20, DHCP Server is 100. For example, if you were born on April 25, 1999, your network address would be 10.99.25.0/24, and Client 1 would be 10.99.25.10/24
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(2).png)
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(3).png)
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(4).png)
3. Check the connection with ping
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(5).png)
4. In the Data Center network assign static addresses, formed according to the following rule: M.D.Y.0/24, where M is the number of the month of birth, D and Y are the same as the previous one. Web Server 1 host part is 50, Web Server 2 host part is 100, DNS Server is 150. So DNS Server address will be 4.25.99.150.
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(6).png)
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(7).png)
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(8).png)
5. Check the connection by using the ping command
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(9).png)
6. On the Client 3 computer, replace the Ethernet network adapter with the Wi-Fi module PT-HOST-NM-1W. The result of the successful substitution is the appearance of a wireless connection.
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(10).png)
7. Assign a static address of 192.168.0.(D+10) to the Client3. For our example this will be 192.168.0.35.
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(11).png)
8. Check the connection to the router using the ping command 192.168.0.1
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(12).png)
Additional task: Examination of the packet structure using Wireshark packet analyzer
1. Install and run the Wireshark application.
2. Select the interface to capture traffic (Capture/Interface menu) and
activate capture mode.
3. Copy a file of several tens of Mbytes in size through the network.
4. Finish capturing traffic and switch to analysis mode.
5. Find TCP segment in the captured stream. Make a screenshot of it.
![]( https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/photo%20(13).png)
6. In this segment find the headers of the data link, network and transport levels. Highlight them in the screenshot.
7. In each of these headers, find the sender and recipient, the IP addresses of the sender and the recipient, and the port numbers of the sender and
recipient.

Sender MAC address: f0:77:c3:85:d7:bb
Receiver MAC address: 90:9a:4a:24:fe:b8
Source IP address: 192.168.0.104
Receive IP address: 144.195.53.205
TCP port of the sender: 55971
Receiver TCP port: 8801
Link file: https://github.com/dimapovarchuk/DevOps_Ivano-Frankivsk_EPAM_L1/blob/main/Home_Work_Module_3/home_work_task3.1/3.1.pkt

![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.1/dst%20mac.png)
dst mac
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.1/src%20mac.png)
src mac
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.1/type.png)
type
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.1/src%20ip.png)
src ip
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.1/src%20port.png)
src port
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.1/dst%20port.png)

![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.1/dst%20ip.png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.1/dst%20ip%20(2).png)
dst ip
