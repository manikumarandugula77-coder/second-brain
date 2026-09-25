/**
 * TelegramBot — Hermes Chat Bot for Notifications & Control
 *
 * Purpose:
 *     Telegram bot for receiving notifications, sending commands,
 *     and providing a conversational interface to other Hermes bots.
 *
 * Sandbox:
 *     This bot is isolated in hermes-workspace/telegram-bot/
 *     All data stays within this directory.
 *
 * Author: Hermes Agent
 */

const { Telegraf } = require('telegraf');
const dotenv = require('dotenv');
const path = require('path');
const fs = require('fs');

// Load environment variables
dotenv.config({ path: path.join(__dirname, '../../config/.env') });

// Setup logging
const logDir = path.join(__dirname, '../../logs');
if (!fs.existsSync(logDir)) {
    fs.mkdirSync(logDir, { recursive: true });
}
const logFile = path.join(logDir, 'telegram-bot.log');

function log(message) {
    const timestamp = new Date().toISOString();
    const logEntry = `[${timestamp}] ${message}\n`;
    fs.appendFileSync(logFile, logEntry);
    console.log(logEntry.trim());
}

class TelegramBot {
    constructor() {
        this.token = process.env.TELEGRAM_BOT_TOKEN;
        if (!this.token) {
            log('ERROR: TELEGRAM_BOT_TOKEN not set in environment variables');
            process.exit(1);
        }

        this.bot = new Telegraf(this.token);
        this.chatId = process.env.TELEGRAM_CHAT_ID;
        this.isRunning = false;
        this.setupCommands();
    }

    setupCommands() {
        // Start command
        this.bot.start((ctx) => {
            log(`User started bot: ${ctx.from.username} (id: ${ctx.from.id})`);
            if (!this.chatId) {
                this.chatId = ctx.chat.id;
                log(`Chat ID set to: ${this.chatId}`);
            }
            ctx.reply(
                '🤖 Hermes Telegram Bot is online!\n\n' +
                'Available commands:\n' +
                '/start - Show this message\n' +
                '/status - Check bot status\n' +
                '/ping - Test bot connectivity\n' +
                '/help - Show help\n' +
                '/send <message> - Send a notification\n'
            );
        });

        // Status command
        this.bot.command('status', (ctx) => {
            log(`Status check from ${ctx.from.username}`);
            ctx.reply('✅ TelegramBot is running\n📡 Connected to Telegram\n🕒 Uptime: Active');
        });

        // Ping command
        this.bot.command('ping', (ctx) => {
            log(`Ping from ${ctx.from.username}`);
            ctx.reply('🏓 Pong!');
        });

        // Help command
        this.bot.command('help', (ctx) => {
            log(`Help requested from ${ctx.from.username}`);
            ctx.reply(
                '📖 Hermes Telegram Bot Help\n\n' +
                'Commands:\n' +
                '/start - Show welcome message\n' +
                '/status - Check bot status\n' +
                '/ping - Test connectivity\n' +
                '/help - Show this help\n' +
                '/echo <text> - Repeat text\n\n' +
                'Notifications:\n' +
                'You will receive automated notifications from other Hermes bots.'
            );
        });

        // Echo command
        this.bot.command('echo', (ctx) => {
            const text = ctx.message.text.replace('/echo ', '');
            log(`Echo request: "${text}"`);
            ctx.reply(text);
        });

        // Handle errors
        this.bot.catch((err, ctx) => {
            log(`Error: ${err.message}`);
            if (ctx) {
                ctx.reply('❌ An error occurred. Check logs for details.');
            }
        });
    }

    async start() {
        log('Starting TelegramBot...');
        try {
            await this.bot.launch();
            this.isRunning = true;
            log('TelegramBot started successfully!');

            // Keep the process running
            process.on('SIGINT', () => {
                this.stop();
            });
        } catch (error) {
            log(`Failed to start bot: ${error.message}`);
            process.exit(1);
        }
    }

    async stop() {
        log('Stopping TelegramBot...');
        await this.bot.stop();
        this.isRunning = false;
        log('TelegramBot stopped.');
    }

    async sendMessage(message) {
        if (!this.chatId) {
            log('Cannot send message: chatId not set. Waiting for /start command.');
            return false;
        }

        try {
            await this.bot.telegram.sendMessage(this.chatId, message);
            log(`Message sent: "${message.substring(0, 50)}..."`);
            return true;
        } catch (error) {
            log(`Failed to send message: ${error.message}`);
            return false;
        }
    }
}

// Export the class for use in other modules
module.exports = TelegramBot;

// Run if called directly
if (require.main === module) {
    const bot = new TelegramBot();
    bot.start().then(() => {
        log('Bot is running. Press Ctrl+C to stop.');
        log('Send /start to your bot in Telegram to initialize.');
    });
}
