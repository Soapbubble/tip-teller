from collections import defaultdict

tip_declarator = "^\[tip\]\s*$" # everything that follows after a line matching this regex is considered a new tip 

class tipdb(object):
    """description of class"""

    def __init__(self):
        self._tips_in_files = defaultdict(list)

    def __setitem__(self, key, value):
        self._tips_in_files[key].append(value)

    def  __getitem__(self, key):
        return self._tips_in_files.get(key, '')

    def __str__(self):
        return '\n'.join(["{}: {} tip(s)".format(str(item), len(self._tips_in_files[item])) for item in self._tips_in_files])

    def __repr__(self):
        return self.__str__()

    def nb_tips(self):
        return sum([len(self._tips_in_files[item]) for item in self._tips_in_files])

    def get_tip_from_file(self, file, tip):
        import re
        pattern = re.compile(tip_declarator)
        
        with open(file,  'r') as f:
            current_tip=0
            tip_lines = []
            read_current_tip = False
            for line_nb, line in enumerate(f):
                if (pattern.match(line)):
                    current_tip+=1
                    if (current_tip == tip):
                        read_current_tip = True
                    elif (current_tip > tip):
                        read_current_tip = False
                        break;
                elif (read_current_tip is True):
                    tip_lines.append(line)

        return ''.join(tip_lines)

    def get_tip_content(self, tip_to_display):
        nb_tips = 0
        tip_file = ''
        for key, values in self._tips_in_files.items():
            nb_tips_in_current_file = len(values)
            if (nb_tips+nb_tips_in_current_file >= tip_to_display):
                tip_file = key
                break
            else:
                nb_tips += len(values)
        
        tip_in_file = tip_to_display - nb_tips
        return self.get_tip_from_file(tip_file, tip_in_file)