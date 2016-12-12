storage = {}

def add(channel, message):
	if channel in storage:
		storage[channel].append(message)
		return len(storage[channel])
	else:
		storage[channel] = [message]
		return 1

def get(channel, fromDate=None, toDate=None):
	if channel in storage:
		return storage[channel]
	else:
		return None