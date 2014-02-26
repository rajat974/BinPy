import math

class MUX:
    """
    This class can be used to create MUX in your circuit.
    It takes 2^n inputs and has n select lines, which are used to select which input line to send to the output.
    """
    def __init__(self, inputs):
        if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
	    raise Exception("ERROR: Number inputs should be a power of 2")
	    return None
	self.inputs = inputs[:]

    def output(self, select):
        try:
            int(select, 2)
    	except ValueError:
	    raise Exception("Invalid Input String")
            return None
	if pow(2, len(select)) == len(self.inputs):
	    return self.inputs[int(select, 2)]
	else:
	    raise Exception("ERROR: Number of select lines not consistent with inputs")
	    return None

    def setInputs(self, inputs):
        if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
	    raise Exception("ERROR: Number inputs should be a power of 2")
	    return None
	self.inputs = inputs[:]

class DEMUX:
    """
    This class can be used to create de-multiplexer in your circuit.
    It has one input, n select lines and returns the 2^n output. In case of high input,
    it works as decoder.
    """
    def __init__(self, inputs):
        if not (inputs==0 or inputs==1):
	    raise Exception("ERROR: Input should be 0/1")
	    return None
	self.inputs = inputs

    def output(self, select):
        try:
            int(select, 2)
    	except ValueError:
	    raise Exception("Invalid Input String")
            return None
	out=[]
	for i in range(pow(2, len(select))):
	    out.append(0)
	out[int(select, 2)] = self.inputs
	return out

    def setInputs(self,inputs):
        if not (inputs==0 or inputs==1):
	    raise Exception("ERROR: Input should be 0/1")
	    return None
	self.inputs = inputs

class Decoder:
    """
    This class can be used to create decoder in your circuit.
    Input is taken as Binary String and returns the 2^n output.
    """
    def __init__(self, inputs):
        if not (len(inputs) != 0):
	    raise Exception("ERROR: Number inputs should be greater than zero")
	    return None
	try:
            int(inputs, 2)
       	    self.inputs = inputs
    	except ValueError:
	    raise Exception("Invalid Input String")
            return None
		
    def output(self):
	out=[]
	for i in range(pow(2, len(self.inputs))):
	    out.append(0)
	out[int(self.inputs, 2)] = 1
	return out

    def setInputs(self, inputs):
        if not (len(inputs) != 0):
	    raise Exception("ERROR: Number inputs should be greater than zero")
	    return None
	try:
            int(inputs, 2)
       	    self.inputs = inputs
    	except ValueError:
	    raise Exception("Invalid Input String")
            return None

class Encoder:
    """
    This class can be used to create encoder in your circuit.
    Input is taken as an array and returns the binary coded output.
    """
    def __init__(self, inputs):
        if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
	    raise Exception("ERROR: Number inputs should be a power of 2")
	    return None
        if not (inputs.count(1) == 1):
	    raise Exception("Invalid Input")
            return None
	self.inputs = inputs[:]
        	
    def output(self):
        out=bin(self.inputs.index(1))[2:]
	while len(out) < math.log(len(self.inputs), 2):
	    out = '0' + out
	return out

    def setInputs(self, inputs):
        if not (len(inputs) != 0 and (len(inputs) & (len(inputs) - 1) == 0)):
	    raise Exception("ERROR: Number inputs should be a power of 2")
	    return None
        if not (inputs.count(1) == 1):
	    raise Exception("Invalid Input")
            return None
	self.inputs = inputs[:]
