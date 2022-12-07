1.Connect the networks created in the previous task with each other, as shown in Fig. 1. Use the PT-Empty routers to build the Internet network, first inserting the 5 1CGE modules, as shown in Figure 2. Switch Enterprise network to interface GigabitEthernet0/0 (GE0/0) Router ISP1, Switch Data Center network to interface GigabitEthernet0/0 (GE0/0) Router ISP3, WAN port Home Router Home Office network to interface GigabitEthernet0/0 (GE0/0), as shown in Figure 1. Connect the routers through the interfaces as shown in Figure 1.
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(1).png)

2.To implement the network Internet to use a network with an address of (D+10).M.Y.0/24, dividing it into subnets with the prefix /26.
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(2).png)
3.Assign IP addresses to router interfaces according to the following rules: Router ISP1 GE0/0 to 10.Y.D.1/24, Router ISP3 GE0/0 to M.D.Y.1/24. Addresses for Other interfaces of routers to be assigned in accordance with the address division (D+10).M.Y.0/24 into subnets. Example of interface IP address assignment router ISP1 GE0/0 is shown in Fig. 3. Warning - it is imperative that you enable the interface by checking the "On" box.
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(3).png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(4).png)

4.On the computers, specify the addresses of the corresponding gateway addresses (Default Gateway)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(5).png)
5.Check the connection of computers with their own gateways using the command ping
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(6).png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(7).png)

Configuring VLAN in Data Center

6.Verify communication between servers using the ping command and route Passing the packet using tracert
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(8).png)
7.Change the subnet mask on the servers to 255.255.255.192
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(9).png)
8.Repeat point 6 and document and explain the changes
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(10).png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(11).png)
9.Change the Switch Data Center VLAN port affiliation as follows: FE0/2 -
VLAN2, FE0/3 - VLAN3, FE0/4 - VLAN4. To do this on the Switch Data Center create the appropriate additional VLANs as shown in Figure 4, and enter the appropriate
ports into the corresponding VLANs, as shown in Fig. 5.
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(12).png)
10.Repeat step 6 and record and explain the changes
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(13).png)
11.For those who will do an additional task, go to step 12, in the other case, you must return the FE0/2, FE0/3, and FE0/4 ports to VLAN1. Also it is desirable to restore the subnet mask on the servers to 255.255.255.0
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(14).png)
Configuring routing between VLANs (optional task)

12.To configure the routing between VLANs you need to switch the FE0/1 Data Center switch to trunk mode, as shown in Figure 6
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(15).png)
13.Warning. The following settings must be made on the router Router ISP3 in CLI mode. Before you can perform the following steps you must Delete the IP address on the Router ISP3 interface GE0/0, as shown in Fig. 7.
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(16).png)
14.Go to CLI mode on the router, create three subinterfaces and configure them as shown below. In the IP addresses, instead of the first three units, put M.D.Y.
Router(config-if)# interface GigabitEthernet0/0.2
Router(config-subif)#encapsulation dot1Q 2
Router(config-subif)#ip address 4.25.99.1 255.255.255.192
Router(config-if)# interface GigabitEthernet0/0.3
Router(config-subif)#encapsulation dot1Q 3
Router(config-subif)#ip address 4.25.99.65 255.255.255.192
Router(config-if)# interface GigabitEthernet0/0.4
Router(config-subif)#encapsulation dot1Q 4
Router(config-subif)#ip address 4.25.99.129 255.255.255.192
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(17).png)
15.On Web Server1, Web Server2, and DNS Server, specify M.D.Y.1 as the gateway address, M.D.Y.65 and M.D.Y.129 addresses by default.
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(18).png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(19).png)



16.Check operability by ping from one server to the other
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(20).png)
![](https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/image%20(21).png)

File link:https://github.com/Dmitriy282/DevOps_online_Vinnytsia_2022Q1Q2/blob/main/m3/task3.2/3.2.pkt
