'''
Created on Nov 17, 2010

@author: kaifox
'''

from conversions import tofl
from conversions import tostr 
from globals import GCont

def twiss(model, madxvarnames, elementpatterns=['.*']):
    
    # create the request
    madxvars = []
    outnames = []
    for name in madxvarnames:
        var = GCont.enums.MadxTwissVariable.fromMadxName(name) #@UndefinedVariable
        if not var == None:
            madxvars.append(var)
            outnames.append(name)
     
    tfsResultRequest = GCont.java_gateway.jvm.cern.accsoft.steering.jmad.domain.result.tfs.TfsResultRequestImpl() #@UndefinedVariable
    
    for pattern in elementpatterns:
        tfsResultRequest.addElementFilter(pattern)
    
    for var in madxvars:
        tfsResultRequest.addVariable(var)
    
    # do the twiss
    tfsResult = model.twiss(tfsResultRequest)
    
    results = dict()
    for idx, var in enumerate(madxvars):
        vartype = tfsResult.getVarType(var)
        if vartype == GCont.enums.MadxVarType.STRING: #@UndefinedVariable
            values = tostr(tfsResult.getStringData(var))
        else:
            values = tofl(tfsResult.getDoubleData(var))
        results[outnames[idx]] = values
    
    return results
    