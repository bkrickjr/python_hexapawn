class Log():
    def __init__(self, first: str):
        '''
        #* Creates a Log object to keep track of the things that are happening instead of using print messages.add()\n
        # @param first: String - The first line of the log.
        '''
        self.first = first
        self.log = '%s'%(first)
    # __init__ end

    def add(self, addition: str):
        '''
        #* Add a new line to the log with the addition parameter.\n
        # @param addition: String - The addition to the log.
        '''
        self.log = '%s\n%s'%(self.log, addition)
    # add end

    def clear(self):
        '''
        #* Clear the log.\n
        '''
        self.log = '%s'%(first)
    # clear end

    def __str__(self):
        return self.log
    # __str__ end
# Log end