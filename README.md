# Real-Time Stock Exchange API

### 📷 Image Gallery

<div style="display: flex; gap: 10px; overflow-x: auto;">
  <img src="https://github.com/UmeshSamartapu/Simple_Stock_Exchange_Server_API/blob/main/assets/1%20Post%20Register%20.png" width="250" />
  <img src="https://github.com/UmeshSamartapu/Simple_Stock_Exchange_Server_API/blob/main/assets/2%20Post%20TokenGen.png" width="250" />
  <img src="https://github.com/UmeshSamartapu/Simple_Stock_Exchange_Server_API/blob/main/assets/3%20Authenticate_Me.png" width="250" />
  <img src="https://github.com/UmeshSamartapu/Simple_Stock_Exchange_Server_API/blob/main/assets/4%20Place%20Oder.png" width="250" />
  <img src="https://github.com/UmeshSamartapu/Simple_Stock_Exchange_Server_API/blob/main/assets/5%20Get%20PortFolio%20details.png" width="250" />
</div>

A FastAPI-based backend simulating a stock exchange with:

- 🔐 JWT Auth & user accounts  
- 📈 Live stock price via WebSocket  
- 🛒 Buy/sell order placement  
- 📊 Portfolio management  
- ☁️ MongoDB Atlas for cloud DB  
- 🐳 Dockerized & deployable on Render/VPS  

## Tech Stack

- FastAPI + WebSockets  
- JWT Auth (OAuth2) + bcrypt  
- MongoDB Atlas + motor  
- Docker + Render  

## Run Locally

```bash
docker build -t stock-app .
docker run -p 8000:8000 --env-file .env stock-app
```
### API Endpoints
```bash
Docs: /docs
Auth: /auth/signup, /auth/token
Orders: /orders/buy, /orders/sell
Portfolio: /portfolio
WebSocket: /ws/stocks
```

### .env Example
```bash
MONGODB_URI=mongodb+srv://<user>:<pass>@.../stock_db
SECRET_KEY=your_jwt_secret
Auto-generated docs at /docs | Simulated stock prices: AAPL, TSLA, MSFT
```

- Let me know if you want a medium-length version with architecture diagram and setup steps!


## 👨‍💻 Author

**Umesh Samartapu**  
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umeshsamartapu/)  
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:umeshsamartapu@gmail.com)

## 📫 Let's Connect

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umeshsamartapu/)
[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://x.com/umeshsamartapu)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:umeshsamartapu@gmail.com)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/umeshsamartapu/)
[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-FBAD19?style=flat-square&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/umeshsamartapu)

---

🔥 Always exploring new technologies and solving real-world problems with code!



