const fs = require("fs");
const path = require("path");
const decache = require("decache");

class CommandHandler {
    constructor(bot) {
        this.bot = bot;
        this.logger = bot.logger;

        this.commands = [];
    }

    loadCommands() {
        const commandDir = path.join(__dirname, "commands");
        const files = fs.readdirSync(commandDir);
        if (this.commands.length !== 0) {
            this.logger.debug("Decaching commands");
            files.forEach((f) => {
                decache(`${commandDir}/${f}`);
            });
        }
        this.logger.debug(`Loading commands: ${files}`);
        this.commands = files.map((f) => {
            try {
                const Cmd = require(`${commandDir}/${f}`);
                const command = new Cmd(this.bot);
                this.logger.debug(`Adding ${command.id}`);
                return command;
            } catch (err) {
                this.logger.error(err);
                return null;
            }
        })
            .filter(c => c !== null);
    }

    handleCommand(message) {
        this.logger.debug(`Handling \`${message.content}\``);
        this.commands.forEach((command) => {
            if (command.regex.test(message.content)) {
                if (this.checkCanAct(command, message.author)) {
                    this.logger.debug(`Matched ${command.id}`);
                    message.react("\u2705").catch(this.logger.error);
                    command.run(message);
                }
            }
        });
    }

    checkCanAct(command, author) {
        if(command.ownerOnly && author.id === this.bot.owner && this.bot.defcon > 1) {
            return true;
        }
        if (command.ownerOnly && author.id !== this.bot.owner) {
            return false;
        }

        if (this.bot.defcon < 3) {
            return false;
        }
        return true;
    }
}
module.exports = CommandHandler;