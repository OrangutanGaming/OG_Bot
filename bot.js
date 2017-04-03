const CommandHandler = require("./CommandHandler.js");
const Discord = require("discord.js");
const md = require("node-md-config");
const Tracker = require("./Tracker.js");
const BotIDs = require("./BotIDs");

class Bot {

    constructor(discordToken, logger, { shardId = 0, shardCount = 1, prefix = BotIDs.prefix,
                    mdConfig = md, owner = null } = {}) {

        this.client = new Discord.Client({
            fetchAllMembers: true,
            ws: {
                compress: true,
                large_threshold: 1000,
            },
            shardId,
            shardCount,
        });
        this.shardId = shardId;
        this.shardCount = shardCount;

        this.token = discordToken;

        this.logger = logger;

        this.escapedPrefix = prefix.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&");

        this.prefix = prefix;

        this.md = mdConfig;

        this.readyToExecute = false;

        this.commandHandler = new CommandHandler(this);

        this.owner = owner;
        this.tracker = new Tracker(this.logger, this.client, { shardId, shardCount });
        this.commandHandler.loadCommands();
        this.setupHandlers();
        this.defcon = 5;
    }
    setupHandlers() {
        this.client.on("ready", () => this.onReady());
        this.client.on("message", message => this.onMessage(message));
        this.client.on("guildCreate", guild => this.onGuildCreate(guild));
        this.client.on("guildDelete", guild => this.onGuildDelete(guild));
        this.client.on("channelCreate", channel => this.onChannelCreate(channel));
        this.client.on("channelDelete", channel => this.onChannelDelete(channel));
        // kill on disconnect so a new instance can be spawned
        this.client.on("disconnect", (event) => {
            this.logger.debug(`Disconnected with close event: ${event.code}`);
            process.exit(4);
        });
        this.client.on("error", error => this.logger.error(error));
        this.client.on("warn", warning => this.logger.warning(warning));
        this.setUpStatuses();
    }
    setUpStatuses() {
        setTimeout(() => {
            if(this.defcon > 4) {
                this.client.user.setGame("with OG|o.help" + ` (${this.shardId + 1}/${this.shardCount})`);
            }
        }, 120000);
    }

     // Creates the database schema and logs in the bot to Discord

    start() {
        this.logger.debug("Schema created");
        this.client.login(this.token).catch((e) => {
            this.logger.error(e.message);
            this.logger.fatal(e);
            process.exit(1);
        });
    }

    onReady() {
        this.logger.debug(`${this.client.user.username} ready!`);
        this.logger.debug(`Bot: ${this.client.user.username}#${this.client.user.discriminator}`);

        console.log("Logged in as:");
        console.log(`Name: ${this.client.user.username}#${this.client.user.discriminator}`);
        console.log("ID: " + this.client.user.id);
        // this.client.user.setGame(game);
        // console.log("Playing".bold, game);
        console.log(BotIDs.OAuth2);

        this.readyToExecute = true;
    }

    onMessage(message) {
        if (this.readyToExecute && message.author.id !== this.client.user.id) {
            this.commandHandler.handleCommand(message);
        }
    }

    onGuildCreate(guild) {
        if (!guild.available) {
            return;
        }
    }

    onGuildDelete(guild) {
        if (!guild.available) {
            return;
        }
    }

    onChannelCreate(channel) {
        if (channel.type === "voice") {
            return;
        }
    }

    onChannelDelete(channel) {
        if (channel.type === "voice") {
            return;
        }
    }
}
module.exports = Bot;