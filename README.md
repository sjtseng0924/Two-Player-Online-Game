# **Two-Player Online Game - Enhanced Lobby System**

## **Overview**
Welcome to the **Two-Player Online Game**! This project is an enhanced online gaming platform with a fully interactive game lobby, advanced file management, and a seamless room-based gaming experience. It is designed to emulate real-world gaming servers, offering persistent storage, multiple player interactions, and customizable game features.

---

## **Features**

### **Lobby Features**
1. **User Registration and Login**
   - Secure account creation and authentication.
   - Persistent user data storage using external files (CSV/txt) or databases.

2. **Lobby Broadcasting**
   - Real-time notifications for:
     - User login/logout
     - Room creation/deletion
   - All users in the lobby receive updates automatically.

3. **Invitation Management**
   - Players can receive multiple invitations.
   - An invitation management interface allows users to view and respond to pending invitations.
   - Automatic handling of closed or full rooms when responding to invitations.

4. **Room Roles**
   - Hosts have special privileges:
     - Invite idle players to the room.
     - Start the game when all required players join.
     - Transfer the host role when leaving or assign it dynamically.
   - Rooms adjust dynamically based on player activity (e.g., deletion of empty rooms).

5. **Bonus - Chat Room**
   - A multi-user chatroom for real-time player communication.
   - Broadcast messages moved to the chatroom to declutter the lobby interface.

---

### **Game File Management**
1. **Upload**
   - Players can upload game scripts to the server.
   - Uploaded files are stored persistently and include metadata (e.g., publisher, description).
   - Automatic version control ensures that users always download the latest version.

2. **Download**
   - Required game files are downloaded when creating or joining a room.
   - Files are saved to the user's local game folder.

3. **Game Execution**
   - Players can execute the game script directly from their local folder after starting a game in the room.
   - The system gracefully handles errors (e.g., missing files or script bugs) by returning users to the room.

4. **Persistence**
   - All game files and metadata are stored in the server’s game folder and external data sources to ensure availability after server restarts.

---

## **Setup and Execution**

### **Prerequisites**
- Python 3.x
- Required modules (`socket`, `os`, `csv`, etc.)
- Network connectivity

### **How to Run**

1. **Start the Lobby Server**
   Run the server on a designated machine:
   ```bash
   ./lobby

2. **Run the Client**
   Execute the client on your machine::
   ```bash
   ./client
   
---

## **Built-in Games**
The system comes with two preloaded games available in the user folders:

- **UserA**: `attack_game.py`
- **UserB**: `number_guessing.py`

To upload these games to the lobby server:
1. Log in with the corresponding account (`UserA` or `UserB`).
2. Use the **Game Management Interface** to upload the game from your local game folder to the lobby.

These games serve as examples to demonstrate the upload, download, and game execution functionalities.

