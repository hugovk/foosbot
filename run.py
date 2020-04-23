from slackbot.bot import Bot, respond_to

players = set()


@respond_to("help")
def help(message):
    message.reply(
        """
    Need help?
    `@foosbot help`

    Create a new game and add yourself:
    `@foosbot new game`

    Add yourself:
    `@foosbot +1`

    Add someone else:
    `@foosbot +1 bob`

    Remove yourself:
    `@foosbot -1`

    Remove someone else:
    `@foosbot -1 bob`

    Check status:
    `@foosbot info`
""".strip()
    )


def user_name(message):
    return message._client.users.get(message.body["user"])["name"]


def player_names():
    global players
    return ", ".join(sorted(players))


def get_info():
    if players:
        return f"{len(players)}/4 players: {player_names()}"
    else:
        return "0/4 players"


@respond_to("new game")
def new_game(message):
    global players
    players = set(user_name(message))
    message.reply(get_info())


@respond_to(r"\+1(.*)")
def add_player(message, name):
    global players

    name = name.strip() if name else user_name(message)

    players.add(name)
    message.reply(get_info())

    if len(players) == 4:
        message.send(f":okgo: {player_names()}")
        players = set()


@respond_to(r"\-1(.*)")
def remove_player(message, name):
    global players

    name = name.strip() if name else user_name(message)

    if name in players:
        players.remove(name)
    message.reply(get_info())


@respond_to("info")
def info(message):
    message.reply(get_info())


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
