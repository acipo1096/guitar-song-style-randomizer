const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const app = express();
const dotenv = require("dotenv").config();
const port = process.env.PORT;

app.use(cors());
app.use(bodyParser.urlencoded({ extended: false }));

app.use("/request", (req, res) => {
  res.sendFile(__dirname + "/song.json");
});

app.use("/licks", (req, res) => {
  res.sendFile(__dirname + "/static/licks.html");
});

app.use("/songs", (req, res) => {
  res.sendFile(__dirname + "/static/index.html");
});

app.use("/guitar", (req, res) => {
  async function getSong() {
    const createPromise = new Promise((res, rej) => {
      let spawn = require("child_process").spawn;
      let process = spawn("/bin/python3", [__dirname + "/guitar_songs.py"]);

      process.stdout.on("data", function (data) {
        let msg = data.toString();
        res(msg);
      });
    });
    const output = await createPromise;
    return output;
  }
  getSong().then(function (result) {
    res.send(result);
  });
});

app.use("/guitar-styles", (req, res) => {
  async function getStyle() {
    const createPromise = new Promise((res, rej) => {
      let spawn = require("child_process").spawn;
      let process = spawn("/bin/python3", [__dirname + "/guitar_styles.py"]);

      process.stdout.on("data", function (data) {
        let msg = data.toString();
        res(msg);
      });
    });
    const output = await createPromise;
    return output;
  }
  getStyle().then(function (result) {
    res.send(result);
  });
});

app.use(express.static("./static"));

app.listen(5000, () => {
  console.log(`Server is listening on port ${port}....`);
});
