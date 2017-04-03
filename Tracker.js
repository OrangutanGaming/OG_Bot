const request = require("request-promise");
const BotIDs = require("./BotIDs.js");
const botsDiscordPwToken = BotIDs.DiscordBotsToken;
const botsDiscordPwUser = "298041215650103296";
const updateInterval = 2600000;

class Tracker {

    constructor(logger, client, { shardId = 0, shardCount = 1 }) {
        this.logger = logger;
        this.client = client;
        this.shardId = shardId;
        this.shardCount = shardCount;
        if (botsDiscordPwToken && botsDiscordPwUser) {
            setInterval(() => this.updateDiscordBotsWeb(this.client.guilds.size), updateInterval);
        }
    }

    updateDiscordBotsWeb(guildsLen) {
        if (botsDiscordPwToken && botsDiscordPwUser) {
            this.logger.debug("Updating discord bots");
            this.logger.debug(`${this.client.username} is on ${guildsLen} servers`);
            const requestBody = {
                method: "POST",
                url: `https://bots.discord.pw/api/bots/${botsDiscordPwUser}/stats`,
                headers: {
                    Authorization: botsDiscordPwToken,
                    "Content-Type": "application/json",
                },
                body: {
                    shard_id: parseInt(this.shardId, 10),
                    shard_count: parseInt(this.shardCount, 10),
                    server_count: parseInt(guildsLen, 10),
                },
                json: true,
            };
            request(requestBody)
                .then((parsedBody) => {
                    this.logger.debug(parsedBody);
                })
                .catch(this.logger.error);
        }
    }

    updateAll(guildsLen) {
        this.updateDiscordBotsWeb(guildsLen);
    }
}
module.exports = Tracker;