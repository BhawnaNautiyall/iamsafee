const express = require("express");
const axios = require("axios");

const router = express.Router();

router.get("/heatmap", async (req, res) => {

  console.log("\n=================================");
  console.log(" NODE RECEIVED /api/heatmap ");
  console.log("=================================\n");

  try {

    const response = await axios.get(
      "http://localhost:8000/heatmap"
    );

    console.log("DATA RECEIVED FROM PYTHON:");
    console.log(JSON.stringify(response.data, null, 2));

    res.json(response.data);

  } catch (error) {

    console.error("NODE ERROR:", error.message);
    res.status(500).json({ error: "Python server error" });
  }
});

module.exports = router;
