import types

def local_activate(val):
	return 1 if val >= 1 else 0

def test_activation(*answ):
    assert len(answ) == 1, "The function activate should be the only argument passed here."
    assert type(answ[0]) == types.FunctionType, "Expected function to be passed, but got " + str(type(answ[0]))
    
    
    def generate_solution(entry):
        if(entry >= 1):
            return 1
        return 0
    
    params = [0, 0.5, 1, 2, 1.5, -1, (2/3), 0.9]
    
    mistake = False
    for p in params:
        resp = generate_solution(p)
        res = answ[0](p)
        
    
        assert type(res) == type(resp), "Expected return type "+str(type(resp))+", but got " + str(type(res))
        
        if(resp != res):
            print("Oops! Your activation function did not work properly in the following case:\n"+str(p)+" -> "+str(res)+" (instead of "+str(resp)+")")
            mistake = True
            return
            
    if(not mistake):
        print("Well done!")

        
        

def test_not_gate(*answ):
    assert len(answ) == 1, "The function not_gate should be the only argument passed here."
    assert type(answ[0]) == types.FunctionType, "Expected function to be passed, but got " + str(type(answ[0]))
    
    
    def generate_solution(entry):
        if(entry >= 1):
            return 0
        return 1
    
    params = [0, 0.5, 1, 2, 1.5, -1, (2/3), 0.9]
    
    mistake = False
    for p in params:
        resp = generate_solution(p)
        res = answ[0](p)
        
    
        assert type(res) == type(resp), "Expected return type "+str(type(resp))+", but got " + str(type(res))
        
        if(resp != res):
            print("Oops! Your activation function did not work properly in the following case:\n"+str(p)+" -> "+str(res)+" (instead of "+str(resp)+")")
            mistake = True
            return
            
    if(not mistake):
        print("Well done!")
def test_or_gate(*answ):
    assert len(answ) == 1, "The function or_gate should be the only argument passed here."
    assert type(answ[0]) == types.FunctionType, "Expected function to be passed, but got " + str(type(answ[0]))
    
    
    def generate_solution(entry_1, entry_2):

        weight_neuron_1 = 1
        weight_neuron_2 = 1

        su = entry_1 * weight_neuron_1 + entry_2 * weight_neuron_2

        return local_activate(su)
    
    params = [(0,0),
                (0,1),
                (1,0),
                (1,1)]
    mistake = False
    for p in params:
        resp = generate_solution(p[0],p[1])
        res = answ[0](p[0],p[1])
        
    
        assert type(res) == type(resp), "Expected return type "+str(type(resp))+", but got " + str(type(res))
        
        if(resp != res):
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" (should be "+str(resp)+")")
            mistake = True
        else:
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" Ok")
            
    if(not mistake):
        print("Well done!")
    else:
        print("Oops, this is not the good weights...")

def test_and_gate(*answ):
    assert len(answ) == 1, "The function and_gate should be the only argument passed here."
    assert type(answ[0]) == types.FunctionType, "Expected function to be passed, but got " + str(type(answ[0]))
    
    
    def generate_solution(entry_1, entry_2):

        weight_neuron_1 = 0.5
        weight_neuron_2 = 0.5

        su = entry_1 * weight_neuron_1 + entry_2 * weight_neuron_2

        return local_activate(su)
    
    params = [(0,0),
                (0,1),
                (1,0),
                (1,1)]
    mistake = False
    for p in params:
        resp = generate_solution(p[0],p[1])
        res = answ[0](p[0],p[1])
        
    
        assert type(res) == type(resp), "Expected return type "+str(type(resp))+", but got " + str(type(res))
        
        if(resp != res):
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" (should be "+str(resp)+")")
            mistake = True
        else:
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" Ok")
            
    if(not mistake):
        print("Well done!")
    else:
        print("Oops, this is not the good weights...")
        
        
def test_xor_gate(*answ):
    assert len(answ) == 1, "The function and_gate should be the only argument passed here."
    assert type(answ[0]) == types.FunctionType, "Expected function to be passed, but got " + str(type(answ[0]))
    
    
    def generate_solution(entry_1, entry_2):

        su = local_activate(entry_1 + entry_2)-local_activate(entry_1 * 0.5 + entry_2 * 0.5)

        return local_activate(su)
    
    params = [(0,0),
                (0,1),
                (1,0),
                (1,1)]
    mistake = False
    for p in params:
        resp = generate_solution(p[0],p[1])
        res = answ[0](p[0],p[1])
        
    
        assert type(res) == type(resp), "Expected return type "+str(type(resp))+", but got " + str(type(res))
        
        if(resp != res):
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" (should be "+str(resp)+")")
            mistake = True
        else:
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" Ok")
            
    if(not mistake):
        print("Well done!")
    else:
        print("Oops, this is not the good weights...")
        
def test_nand_gate(*answ):
    assert len(answ) == 1, "The function and_gate should be the only argument passed here."
    assert type(answ[0]) == types.FunctionType, "Expected function to be passed, but got " + str(type(answ[0]))
    
    
    def generate_solution(entry_1, entry_2):

        return 0 if entry_1 + entry_2 == 2 else 1
    
    params = [(0,0),
                (0,1),
                (1,0),
                (1,1)]
    mistake = False
    for p in params:
        resp = generate_solution(p[0],p[1])
        res = answ[0](p[0],p[1])
        
    
        assert type(res) == type(resp), "Expected return type "+str(type(resp))+", but got " + str(type(res))
        
        if(resp != res):
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" (should be "+str(resp)+")")
            mistake = True
        else:
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" Ok")
            
    if(not mistake):
        print("Well done!")
    else:
        print("Oops, this is not the good weights...")

def test_nor_gate(*answ):
    assert len(answ) == 1, "The function and_gate should be the only argument passed here."
    assert type(answ[0]) == types.FunctionType, "Expected function to be passed, but got " + str(type(answ[0]))
    
    
    def generate_solution(entry_1, entry_2):

        return 0 if entry_1 ==1 or entry_2 == 1 else 1
    
    params = [(0,0),
                (0,1),
                (1,0),
                (1,1)]
    mistake = False
    for p in params:
        resp = generate_solution(p[0],p[1])
        res = answ[0](p[0],p[1])
        
    
        assert type(res) == type(resp), "Expected return type "+str(type(resp))+", but got " + str(type(res))
        
        if(resp != res):
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" (should be "+str(resp)+")")
            mistake = True
        else:
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" Ok")
            
    if(not mistake):
        print("Well done!")
    else:
        print("Oops, this is not the good weights...")
        

def test_xnor_gate(*answ):
    assert len(answ) == 1, "The function and_gate should be the only argument passed here."
    assert type(answ[0]) == types.FunctionType, "Expected function to be passed, but got " + str(type(answ[0]))
    
    
    def generate_solution(entry_1, entry_2):

        su = local_activate(entry_1 + entry_2)-local_activate(entry_1 * 0.5 + entry_2 * 0.5)

        return 0 if local_activate(su) == 1 else 1
    
    params = [(0,0),
                (0,1),
                (1,0),
                (1,1)]
    mistake = False
    for p in params:
        resp = generate_solution(p[0],p[1])
        res = answ[0](p[0],p[1])
        
    
        assert type(res) == type(resp), "Expected return type "+str(type(resp))+", but got " + str(type(res))
        
        if(resp != res):
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" (should be "+str(resp)+")")
            mistake = True
        else:
            print(str(p[0])+" & "+str(p[1])+" -> "+str(res)+" Ok")
            
    if(not mistake):
        print("Well done!")
    else:
        print("Oops, this is not the good weights...")
        
        
def table_truth(*args):
    network = args[0]
    for i in range(2):
        for j in range(2):
            print(str(i)+" & "+str(j)+" -> "+str(network(i,j)))