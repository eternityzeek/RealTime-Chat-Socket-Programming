𝐑𝐞𝐚𝐥-𝐓𝐢𝐦𝐞 𝐂𝐡𝐚𝐭 𝐀𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐰𝐢𝐭𝐡 𝐆𝐔𝐈 𝐮𝐬𝐢𝐧𝐠 𝐒𝐨𝐜𝐤𝐞𝐭 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐦𝐢𝐧𝐠  

This project is a real-time chat application built with **Python sockets** and a **tkinter GUI**. It allows multiple clients to connect to a server, send messages to each other, and engage in personal chats. The server manages the communication and provides a log of connected users. 


𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 

𝐁𝐚𝐬𝐢𝐜 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬  
- 𝐒𝐞𝐫𝐯𝐞𝐫 𝐒𝐭𝐚𝐫𝐭/𝐒𝐭𝐨𝐩:  
  The server can be started and stopped using GUI buttons, managing all connections.
- 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐚𝐧𝐝 𝐂𝐥𝐢𝐞𝐧𝐭𝐬 𝐒𝐞𝐜𝐭𝐢𝐨𝐧:  
  Server displays real-time messages and a list of connected clients.
- 𝐂𝐥𝐢𝐞𝐧𝐭 𝐋𝐨𝐠𝐢𝐧:  
  Clients can provide the server’s IP and port, and must enter a username to connect.
- 𝐒𝐞𝐧𝐝/𝐑𝐞𝐜𝐞𝐢𝐯𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬:  
  Clients can exchange real-time messages within the chatroom.
- 𝐋𝐨𝐠𝐨𝐮𝐭:  
  A logout button lets users disconnect from the chatroom.

𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬  
- 𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥 𝐂𝐡𝐚𝐭:  
  Clients can send private messages to specific users by entering their usernames.
- 𝐂𝐥𝐞𝐚𝐫 𝐂𝐡𝐚𝐭:  
  Clients can clear their chat window using a "Clear Chat" button.

𝐅𝐮𝐭𝐮𝐫𝐞 𝐄𝐧𝐡𝐚𝐧𝐜𝐞𝐦𝐞𝐧𝐭𝐬 
- 𝐅𝐢𝐥𝐞 𝐓𝐫𝐚𝐧𝐬𝐟𝐞𝐫: 
  Enable clients to upload/download files from the server.
- 𝐄𝐧𝐜𝐫𝐲𝐩𝐭𝐢𝐨𝐧:  
  Add encryption for secure communication between server and clients.
- 𝐀𝐮𝐭𝐡𝐞𝐧𝐭𝐢𝐜𝐚𝐭𝐢𝐨𝐧:  
  Implement user authentication to enhance security.



𝐏𝐫𝐞𝐫𝐞𝐪𝐮𝐢𝐬𝐢𝐭𝐞𝐬 
1. Python 3.x  
2. tkinter (comes pre-installed with Python)


𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐚𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞  
1. Clone the repository from GitHub:  
   bash
   git clone https://github.com/eternityzeek/RealTime-Chat-Socket-Programming.git
   cd RealTime-Chat-Socket-Programming

2. Update the 𝐈𝐏 𝐀𝐝𝐝𝐫𝐞𝐬𝐬 𝐚𝐧𝐝 𝐏𝐨𝐫𝐭 in `client.py` and `server.py` as needed:
   
   HOST = '192.168.X.X'  # Replace with your IP address
   PORT = 5555  # Update if needed
   

3. 𝐑𝐮𝐧 𝐭𝐡𝐞 𝐒𝐞𝐫𝐯𝐞𝐫:  
   bash
   python server.py
   - The server GUI will display connected clients and messages.

4. 𝐑𝐮𝐧 𝐭𝐡𝐞 𝐂𝐥𝐢𝐞𝐧𝐭:  
   bash
   python client.py
   - Enter the server's IP, port, and a username to connect.

𝐔𝐬𝐚𝐠𝐞 𝐄𝐱𝐚𝐦𝐩𝐥𝐞𝐬  

𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐚 𝐌𝐞𝐬𝐬𝐚𝐠𝐞  
- Type a message in the text box and click "Send" to broadcast it to everyone.

𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥 𝐂𝐡𝐚𝐭  
- Click "Personal Chat" and enter the recipient’s username and message.  
- The message will be sent privately to the specified user.

𝐋𝐨𝐠𝐨𝐮𝐭  
- Use the "Logout" button to disconnect from the server.

𝐂𝐥𝐞𝐚𝐫 𝐂𝐡𝐚𝐭 
- Use the "Clear Chat" button to erase the chat history in the client’s window.



𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐅𝐢𝐥𝐞𝐬  
- `𝐬𝐞𝐫𝐯𝐞𝐫.𝐩𝐲`: Manages client connections, broadcasts messages, and handles private messaging.  
- `𝐜𝐥𝐢𝐞𝐧𝐭.𝐩𝐲`: Connects to the server and provides the chat GUI for users to send and receive messages.

