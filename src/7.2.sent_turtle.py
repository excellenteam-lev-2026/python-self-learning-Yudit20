class PostOffice:
    """
    A Post Office class that manages message boxes for users.
    Supports sending, reading, and searching messages.
    """

    def __init__(self, usernames):
        """
        Initialize the PostOffice with a list of usernames.

        :param usernames: List of usernames to create inboxes for
        """
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, body, urgent=False):
        """
        Send a message to a recipient.

        :param sender: The sender's username
        :param recipient: The recipient's username
        :param title: The message title
        :param body: The message body
        :param urgent: If True, insert at the beginning of the inbox
        :return: The message ID
        """
        self.message_id += 1
        message = {
            'id': self.message_id,
            'title': title,
            'body': body,
            'sender': sender,
            'read': False,          # New message -> unread by default
        }
        if urgent:
            self.boxes[recipient].insert(0, message)
        else:
            self.boxes[recipient].append(message)
        return self.message_id

    def read_inbox(self, username, count=None):
        """
        Return unread messages from the user's inbox and mark them as read.

        :param username: The user whose inbox to read
        :param count: Number of messages to read (all if not specified)
        :return: List of unread messages (up to count)
        """
        # Retrieve only unread messages
        messages_non_lus = [m for m in self.boxes[username] if not m['read']]

        # Limit to the requested number (or all if count=None)
        messages_a_lire = messages_non_lus[:count]

        # Mark as read (modifies dicts directly in self.boxes)
        for message in messages_a_lire:
            message['read'] = True

        return messages_a_lire

    def search_inbox(self, username, query):
        """
        Search all messages (read and unread) for a query string.
        Searches both title and body of each message.

        :param username: The user whose inbox to search
        :param query: The string to search for
        :return: List of matching messages
        """
        return [
            message for message in self.boxes[username]
            if query in message['title'] or query in message['body']
        ]


# =====================
#        TESTS
# =====================

po = PostOffice(['Alice', 'Bob'])

# Sending messages
po.send_message('Bob', 'Alice', 'Hello', 'How are you?')
po.send_message('Bob', 'Alice', 'Meeting', 'Tomorrow at 9am')
po.send_message('Bob', 'Alice', 'Urgent!', 'Call me now!', urgent=True)
po.send_message('Bob', 'Alice', 'News', 'Python 4 is out!')

# Test read_inbox with count
print("--- Lire 2 messages ---")
messages = po.read_inbox('Alice', count=2)
for m in messages:
    print(f"[{m['id']}] {m['title']} — lu: {m['read']}")
# [3] Urgent! — lu: True
# [1] Hello  — lu: True

# Test read_inbox without count (all remaining unread)
print("\n--- Lire tous les messages restants ---")
messages = po.read_inbox('Alice')
for m in messages:
    print(f"[{m['id']}] {m['title']} — lu: {m['read']}")
# [2] Meeting — lu: True
# [4] News    — lu: True

# Test read_inbox when everything is read
print("\n--- Boîte vide (tout déjà lu) ---")
print(po.read_inbox('Alice'))
# []

# Test search_inbox
print("\n--- Recherche 'Python' ---")
results = po.search_inbox('Alice', 'Python')
for m in results:
    print(f"[{m['id']}] {m['title']}: {m['body']}")
# [4] News: Python 4 is out!