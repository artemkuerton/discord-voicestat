# Discord Voicestat

This Discord bot tracks the time users spend in voice chats. With it, you can find out how much time you spent voting on the channel.

## Installation

1. Make sure you have Python 3.8 or higher installed.
2. Install the `discord.py` library by running the following command:

   ```bash
   pip install discord.py
   ```

3. Create a new bot on [Discord Developer Portal](https://discord.com/developers/applications) and copy the token.

## Settings

1. Replace `TOKEN` in your bot code with your bot's token:

   ```python
   bot.run('TOKEN')
   ```

2. Make sure your bot has the necessary permissions to connect and read messages in voice channels on the Discord server.

## How to use

- Run the bot code.
- When entering or leaving a voice channel, the bot will automatically track the time.
- To find out how much time you spent in a voice channel, enter the command `!time` in a text channel.

### Example command

```plaintext
!time
```

**Bot response**: "You've spent X seconds in voice chat."

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.
