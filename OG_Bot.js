const Discord = require("discord.js");
const Colours = require("colors");
const BotIDs = require("./BotIDs.js");

const bot = new Discord.Client();
const token = BotIDs.token;

const game = "with OG|o!help";
const prefixes = ["o!", "o."];
const prefix = "o!"

bot.on("ready", () => {
    /*
     @bot.event
     async def on_ready():
     print("Prefixes: " + Prefixes.Prefix('"'))
     */
    console.log("Logged in as:");
    console.log(`Name: ${bot.user.username}#${bot.user.discriminator}`);
    console.log("ID: " + bot.user.id);
    bot.user.setGame(game);
    console.log("Playing".bold, game);
    console.log(BotIDs.OAuth2);
    console.log(`Prefixes: ${prefixes.join(", ")}`);

});

bot.on("message", message => {
    if (message.author.bot) return;
    if (!message.content.startsWith(prefix)) return;

    let command = message.content.split(" ")[0];
    command = command.slice(prefix.length)

    if (command === "ping") {
        message.channel.sendMessage("pong");
    }
});

bot.login(token);
