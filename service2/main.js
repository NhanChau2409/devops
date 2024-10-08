const express = require("express");
const { execSync } = require("child_process");

const app = express();

function getContainerInfo() {
	const ipAddress = execSync("hostname -I").toString().trim();
	const processes = execSync("ps -ax").toString().trim();
	const diskSpace = execSync("df").toString().trim();
	const uptime = execSync("uptime").toString().trim();

	return {
		Service2: {
			ip_address: ipAddress,
			processes: processes,
			disk_space: diskSpace,
			uptime: uptime,
		},
	};
}

app.get("/", (req, res) => {
	const containerInfo = getContainerInfo();
	console.log(containerInfo);
	res.json(containerInfo);
});

app.listen("80", "0.0.0.0", () => {
	console.log(`Server is running on port 80`);
});
