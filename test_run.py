import run


class MockMessage:
    reply_text = None
    send_text = None

    def reply(self, text):
        self.reply_text = text

    def send(self, text):
        self.send_text = text


def test_add_player():
    # Arrange
    run.players = set()
    message = MockMessage()

    # Act
    run.add_player(message, " ava")

    # Assert
    assert run.players == {"ava"}
    assert message.reply_text == "1/4 players: ava"


def test_add_two_players():
    # Arrange
    run.players = set()
    message = MockMessage()

    # Act
    run.add_player(message, " bob")
    run.add_player(message, " ava")

    # Assert
    assert run.players == {"ava", "bob"}
    assert message.reply_text == "2/4 players: ava, bob"


def test_add_three_players():
    # Arrange
    run.players = set()
    message = MockMessage()

    # Act
    run.add_player(message, " bob")
    run.add_player(message, " ava")
    run.add_player(message, " che")

    # Assert
    assert run.players == {"ava", "bob", "che"}
    assert message.reply_text == "3/4 players: ava, bob, che"


def test_add_four_players():
    # Arrange
    run.players = set()
    message = MockMessage()

    # Act
    run.add_player(message, " bob")
    run.add_player(message, " ava")
    run.add_player(message, " che")
    run.add_player(message, " dee")

    # Assert
    assert run.players == set()  # reset for next game
    assert message.reply_text == "4/4 players: ava, bob, che, dee"
    assert message.send_text == ":okgo: ava, bob, che, dee"


def test_add_five_players():
    # Arrange
    run.players = set()
    message = MockMessage()

    # Act
    run.add_player(message, " bob")
    run.add_player(message, " ava")
    run.add_player(message, " che")
    run.add_player(message, " dee")
    # okgo! new game:
    run.add_player(message, " eve")

    # Assert
    assert run.players == {"eve"}
    assert message.reply_text == "1/4 players: eve"


def test_add_same_twice():
    # Arrange
    run.players = set()
    message = MockMessage()

    # Act
    run.add_player(message, " bob")
    run.add_player(message, " bob")

    # Assert
    assert run.players == {"bob"}
    assert message.reply_text == "1/4 players: bob"


def test_add_and_remove_one_player():
    # Arrange
    run.players = set()
    message = MockMessage()
    run.add_player(message, " ava")
    run.add_player(message, " bob")

    # Act
    run.remove_player(message, " ava")

    # Assert
    assert run.players == {"bob"}


def test_add_and_remove_all_players():
    # Arrange
    run.players = set()
    message = MockMessage()
    run.add_player(message, " ava")
    run.add_player(message, " bob")

    # Act
    run.remove_player(message, " ava")
    run.remove_player(message, " bob")
    run.remove_player(message, " bob")

    # Assert
    assert run.players == set()


def test_info():
    # Arrange
    run.players = set()
    message = MockMessage()
    run.add_player(message, " ava")
    run.add_player(message, " bob")

    # Act
    run.info(message)

    # Assert
    assert run.players == {"ava", "bob"}
    assert message.reply_text == "2/4 players: ava, bob"


def test_player_names():
    # Arrange
    run.players = set()
    message = MockMessage()
    run.add_player(message, " ava")
    run.add_player(message, " bob")
    assert run.players == {"ava", "bob"}

    # Act
    output = run.player_names()

    # Assert
    assert output == "ava, bob"


def test_help():
    # Arrange
    message = MockMessage()

    # Act
    run.help(message)

    # Assert
    assert "Need help?" in message.reply_text
