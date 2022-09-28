import razorpay

key_id = "rzp_test_NQsdA9rMMdMTBG"
key_secret = "EAqs7MSB83Ky4X4oaZWNrRWd"

client = razorpay.Client(auth=(key_id,key_secret))

data = {
	'amount': 100*100,
	'currency': "INR",
	'receipt': "SirdaCollegeSemFees"
}

order = client.order.create(data=data)
print(order)


{'id': 'order_IXOwQzOZznsp8B', 'entity': 'order', 'amount': 10000, 'amount_paid': 0, 'amount_due': 10000, 'currency': 'INR', 'receipt': 'SirdaCollegeSemFees', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1639495019}

