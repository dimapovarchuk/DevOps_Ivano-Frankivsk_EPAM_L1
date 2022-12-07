1. Configuring the DHCP Server in the Enterprise network (Fig. 1). To do this, enter the DHCP Server configuration
2. Configure the DHCP Pool, specifying the starting address 10.Y.D.10 and the Default Gateway address - the address of the GE0/0 Router ISP1 interface. Save the settings (button Save) and switch on the DHCP service (mark On) in fig.2.
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task2.png)
3. Check service operability by setting Client 1 and Client 2 DHCP as shown in Fig. 3
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task3.png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task3.1.png)
4. Setting DHCP on Home Router and checking the service on Client 3
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task4.png)
5. To configure and test the DNS service, assign Web Server1 and Web Server2 domain names such as domain1.com and domain2.com according to.
6. Make the appropriate entries in the DNS server setup as shown in Fig. 4. And turn on the DNS Service.
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task6.png)
7. Add the DNS server address to the DHCP server settings and update the settings on the clients (by switching from DHCP to Static and back to DHCP).
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task7.png)
8. Verify operability by sending a ping from the Client to the domain name, as shown in Fig. 5
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task8.png)
Configuring Port Forwarding on the Home Router (optional task)

9. Add the Home Office Home Server to the network and assign it a static address, as shown in Fig. 6
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task9.png)
10. On the Home Server, for the HTTP service, edit the index.html, as shown in Fig. 7
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task10.png)
11. adjust the Port Forwarding on the Home Router, as shown in picture 8.
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task11.png)
12. Add an entry on the DNS Server for the Home Server, as shown in Fig.9
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task12.png)
13. Check the functionality by entering on Client1 in Desktop/Web Browser - domain3.com, as shown in Fig. 10
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/task13.png)
File link: https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.4/3.4.pkt
