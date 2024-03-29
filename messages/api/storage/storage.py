storage = {}

def add(channel, message):
	if channel in storage:
		storage[channel].append(message)
		return message
	else:
		storage[channel] = [message]
		return message

def get(channel, fromDate=None, toDate=None):
	if channel in storage:
		return storage[channel]
	else:
		return None