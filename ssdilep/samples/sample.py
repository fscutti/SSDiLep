# encoding: utf-8
'''
sample.py

description:

simple sample class. 

'''

## modules
import metaroot
import xsections
import copy

# - - - - - - - - - - - class defs  - - - - - - - - - - - - #
#------------------------------------------------------------------------------
# Sample Class
#------------------------------------------------------------------------------
class Sample(object):
    """
    basic sample class
    """
    #__________________________________________________________________________
    def __init__(self,
                 name          = '',
                 suffix        = '',
                 tlatex        = None,
                 infile        = None,
                 xsec          = None,
                 feff          = 1.0, 
                 kfactor       = 1.0,
                 files         = [],
                 type          = "mc",
                 config        = None,
                 daughters     = [],
                 estimator     = None,
                 **kw):

        ## Attach attributes.
        ## -------------------------------------------------------
        self.name          = name
        self.suffix        = suffix
        self.infile        = infile or name
        self.tlatex        = tlatex or name
        self.xsec          = xsec
        self.feff          = feff
        self.kfactor       = kfactor
        self.files         = files
        self.type          = type
        self.config        = config or {}
        self.daughters     = daughters
        self.estimator     = estimator
        ## for stylying histograms
        self.plotopts      = metaroot.hist.PlotOptions(**kw)
       
        #if not self.xsec and not "data" in self.type:
        if (not self.xsec) and (self.name in xsections.xsdict.keys()):
          self.xsec = xsections.xsdict[self.name]

        ## set additional key-word args
        ## -------------------------------------------------------
        for k,w in kw.iteritems():
            setattr(self, k, w)

    #__________________________________________________________________________
    def copy(self):
        """ Return a new sample, with all the same attributes."""
        return Sample(**self.__dict__)
    
    #__________________________________________________________________________
    def duplicate(self,**kw):
        """ 
        Returns a duplicate of the samples with modified attributes.
        NB: do not use this to update the list of daughters!
        """
        new_daughters = []
        if self.daughters:
          for d in self.daughters: new_daughters.append(d.duplicate(**kw))
          kw['daughters'] = new_daughters 
        
        # change name of duplicate sample
        if 'suffix' in kw.keys(): kw['name'] = self.name+"_"+kw['suffix']
        dict_copy = copy.deepcopy(self.__dict__)
        dict_copy.update(kw)
        return Sample(**dict_copy)

    #__________________________________________________________________________
    def get_active_samples(self):
        """
        get end samples (ie. that dont have daughters)
        """
        samples = []
        if self.daughters: 
            for d in self.daughters: samples += d.get_active_samples()
        else:
            samples.append(self)

        return samples

    #____________________________________________________________
    def hist(self,**kw): 
        assert self.estimator, "ERROR - sample %s missing estimator!" % self.name

        h = self.estimator.hist(**kw)
        return h





## EOF
