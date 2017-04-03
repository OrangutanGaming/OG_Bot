class Logger {
    constructor(ravenClient) {
        this.ravenClient = ravenClient;
    }
}
const logLevel = process.env.LOG_LEVEL || "ERROR";
const levels = [
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "FATAL",
];
levels.forEach((level) => {
    Logger.prototype[level.toLowerCase()] = function (message) {
        if (levels.indexOf(level) >= levels.indexOf(logLevel)) {
            console.log(`[${level}] ${message}`);
        }
        if (level === "fatal") {
            this.ravenClient.captureMessage(message, {
                level: "fatal",
            });
        }
        if (level === "error") {
            this.ravenClient.captureException(message);
        }
    };
});
module.exports = Logger;