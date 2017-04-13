from evennia.commands.default.muxcommand import MuxCommand


class CmdFind(MuxCommand):
    key = "+locate"
    locks = "cmd:all()"
    def func(self):
        skip = 1
        for ishere in self.caller.location.contents:
            if self.args == ishere.key:
                self.msg("It is right here!\n")
                skip = 0

        if skip:
            for arg in self.caller.location.exits:
                for matches in arg.destination.contents:
                    if self.args == matches.key:
                        self.msg("(1)You sense it is %s." % arg)
                        return
                    else:
                        for arg2 in matches.location.exits:
                           for matches2 in arg2.destination.contents:
                               if self.args == matches2.key:
                                   self.msg("(2)You sense it is %s." % arg)	                  
                                   return
                               else:
                                   for arg3 in matches2.location.exits:
                                       for matches3 in arg3.destination.contents:
                                           if self.args == matches3.key:
                                               self.msg("(3)You sense it is %s." % arg)	                  
                                               return
                                           else:
                                               for arg4 in matches3.location.exits:
                                                   for matches4 in arg4.destination.contents:
                                                       if self.args == matches4.key:
                                                           self.msg("(4)You sense it is %s." % arg)	                  
                                                           return
                                                   