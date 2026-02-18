const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

const newsRoutes = require("./routes/news.routes");

app.use("/api", newsRoutes);

app.get("/", (req, res) => {
  res.json({ message: "Backend running 🚀" });
});

const PORT = 5000;

app.listen(PORT, () => {
  console.log(`Express running on http://localhost:${PORT}`);
});
