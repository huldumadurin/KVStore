import md5

hashtable = []
blob = []
numBuckets = 0xF

def add(key, value):
	hashedKey = hashKey(key)
	i = hashKey(key)
	looking = True
	while looking:
		if hashtable[hashedKey] != -1:
			if getValueAtAddress(hashtable[hashedKey]) == key:
				print("Overwriting!")
				looking = False
			else:
				print("Spot Taken!")
				i = (i + 1) % numBuckets
				if hashedKey == i:
					return None 
		else:
			looking = False

	hashtable[hashedKey] = blobAppend(key, value)
	print("Added " + key + "with Value " + value)

def get(key):

	print("Looking for: " + key)

	#Hash key
	hashedKey = hashKey(key)
	i = hashKey(key)
	suspectedAddress = hashtable[hashedKey]
	#if exists, follow
	if suspectedAddress != -1:
		while True:
			print("Value might be at " + str(suspectedAddress))
	                print("Key: " + str(getValueAtAddress(suspectedAddress)))
        	        print("Value: " + str(getValueAtAddress(suspectedAddress + 1)))


			if getValueAtAddress(suspectedAddress) == key:
				return getValueAtAddress(suspectedAddress + 1)
			else:
				print("Nope!")
			i = (i + 1) % numBuckets
			if hashedKey == i:
				return None
			suspectedAddress = hashtable[hashedKey]


	return None
	#if entry matches key, return value
	
	#else, follow next until empty bucket reached

def blobAppend(key, value):
	global blob
	address = len(blob)

	print(key)
	print(value)

	#blob.append([ord(char) for char in key])
	#blob.append([ord(char) for char in value])
	blob.append(key)
	blob.append(value)

	return address

def getValueAtAddress(address):
	return blob[address]

def hashKey(key):
	fullHash = md5.new(key).hexdigest()
	return int(fullHash, 16) % numBuckets


def load():
	print("Not implemented!")



def init():
	global hashtable
	global addressBytes

	hashtable = [-1] * numBuckets
	addressBytes = 1

#WIP program code

init()

print hashtable
print blob
print(get("Blargh"))
add("Gron", "Gront")
add("Brun", "Brunt")
add("Reyd", "Reytt")
add("Bla", "Blatt")
add("Gra", "Gratt")
add("Svort", "Svart")
add("Morreyd", "Morreytt")
add("Lillavordin", "Lillavordid")
add("Ljosareyd", "Ljosareytt")
print hashtable
print blob
get("SGron")
get("Brun")
get("Reyd")
get("Bla")
get("Gra")
get("Svort")
get("Morreyd")
get("Lillavordin")
get("Ljosareyd")
