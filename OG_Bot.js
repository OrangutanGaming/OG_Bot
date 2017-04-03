const Discord = require("discord.js");
// const Colours = require("colors");
const BotIDs = require("./BotIDs.js");
const Raven = require("raven");

const client = Raven.config(BotIDs.ravenURL);
client.install();
const Logger = require("./Logger.js");
const logger = new Logger(client);

/*
const bot = new Discord.Client();
const token = BotIDs.token;

const game = "with OG|o!help";
const prefixes = ["o!", "o."];

bot.on("ready", () => {
    console.log("Logged in as:");
    console.log(`Name: ${bot.user.username}#${bot.user.discriminator}`);
    console.log("ID: " + bot.user.id);
    bot.user.setGame(game);
    console.log("Playing".bold, game);
    console.log(BotIDs.OAuth2);
    console.log(`Prefixes: ${prefixes.join(", ")}`); // Not True
    // TODO Multiple Prefixes

});

bot.on("guildCreate", guild => {
    try {guild.defaultChannel.sendMessage("Welcome to the world of Orangutans! I was made by `OGaming#7135` Run `o!help` " +
        "for help");}
        catch (e) {return}
});

bot.on("message", message => {
    if (message.author.bot) return;
    if (!message.content.startsWith(prefix)) return;

    let command = message.content.split(" ")[0];
    command = command.slice(prefix.length);

    let args = message.content.split(" ").slice(1);

    if (command === "add") {
        let numArray = args.map(n => parseInt(n));
        let total = numArray.reduce((p, c) => p+c);

        Args = args.join(" + ");
        Args = `\`${Args}\``;

        message.channel.sendMessage(`${Args} is \`${total}\``)
    }

    if (command === "ping") {
        message.channel.sendMessage("pong");
    }

    if (command === "uptime") {
        message.channel.sendMessage("uptime: " + bot.uptime)
    }

});

bot.login(token);
*/
const Bot = require("./bot.js");
const bot = new Bot(BotIDs.token, logger, {
    prefix: BotIDs.prefix,
    logger,
    owner: BotIDs.Owner,
});

/*
this.onReady() {
    console.log("Logged in as:");
    console.log(`Name: ${bot.user.username}#${bot.user.discriminator}`);
    console.log("ID: " + bot.user.id);
    bot.user.setGame(game);
    console.log("Playing".bold, game);
    console.log(BotIDs.OAuth2);

});
*/

bot.start();