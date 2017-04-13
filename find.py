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
                        self.msg("You sense it is %s." % arg)
                        return
                    else:
                        for arg2 in matches.location.exits:
                           for matches2 in arg2.destination.contents:
                               if self.args == matches2.key:
                                   self.msg("You sense it is %s." % arg)	                  
                                   return
                               else:
                               	self.msg("test")
                                   for arg3 in matches2.location.exits:
                                       for matches3 in arg3.destination.contents:
                                           if self.args == matches3.key:
                                               self.msg("You sense it is %s." % arg)	                  
                                               return