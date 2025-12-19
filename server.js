const express = require("express");
const fs = require("fs");
const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// CORS 許可
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Content-Type");
    next();
});

// データ読み込み
function loadData() {
    return JSON.parse(fs.readFileSync("data.json", "utf8"));
}

// データ保存
function saveData(data) {
    fs.writeFileSync("data.json", JSON.stringify(data, null, 2));
}

// 全データ取得
app.get("/requests", (req, res) => {
    res.json(loadData());
});

// 新規追加
app.post("/requests", (req, res) => {
    const data = loadData();
    const newItem = {
        id: Date.now(),
        ...req.body
    };
    data.push(newItem);
    saveData(data);
    res.json({ status: "ok", id: newItem.id });
});

app.listen(PORT, () => {
    console.log("API server running on port " + PORT);
});
