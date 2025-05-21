const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.post("/login", (req, res) => {
    const { username, password } = req.body;
    if (username === "testUser" && password === "password123") {
        res.json({ success: true, server_ip: "mc.example.server" });
    } else {
        res.json({ success: false, error: "Invalid login!" });
    }
});

app.listen(8080, () => console.log("Server running on port 8080!"));
