class Command {

    constructor(bot, id, call, description) {

        this.id = id;
        this.call = call;

        this.regex = new RegExp(`^${bot.escapedPrefix}${call}`, "i");

        this.usages = [
            { description, parameters: [] },
        ];

        this.logger = bot.logger;

        this.bot = bot;

        this.md = bot.md;

        this.zSWC = "\u200B";

        this.commandHandler = bot.commandHandler;

        this.ownerOnly = false;
    }

    run(message) {
        message.reply("This is a basic Command")
            .then((msg) => {
                this.logger.debug(`Sent ${msg}`);
            })
            .catch((error) => {
                this.logger.error(`Error: ${error}`);
            });
    }
}
module.exports = Command;