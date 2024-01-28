# --------------------------------------------------------------------------------
# Auteurs : Nassim HAMRI & Tristan RENAUD
# Date : Janvier 2024
# 
# Ce fichier est partie intégrante de Stent_design_and_construction écrit par les mêmes auteurs.
#
# Il a été adapté librement du travail de @roseengineering disponible ici https://github.com/roseengineering/igeswrite
# --------------------------------------------------------------------------------

import sys, os

def hollerith(s):
    return "{}H{}".format(len(s), s)

class Iges:

    def __init__(self):
        self.buffer = ["","","",""]
        self.buffer_D = [""]
        self.buffer_P = [""]
        self.lineno= [0,0,0,0]

    def get_section(self, section):
        if section == "D":
            return 0
        elif section == "P":
            return 1
        elif section == "S":
            return 2
        elif section == "G":
            return 3
        
    def add_line(self, section, line, index=""):
        index = str(index)
        self.lineno[self.get_section(section)] += 1
        lineno = self.lineno[self.get_section(section)]
        buf = "{:64s}{:>8s}{}{:7d}\n".format(line, index, section, lineno)
        self.buffer[self.get_section(section)] += buf
        
    def add_lineP(self, line, index=""):
        index = str(index)
        self.lineno[1] += 1
        lineno = self.lineno[1]
        buf = "{:64s}{:>8s}{}{:7d}\n".format(line, index, "P", lineno)
        self.buffer_P.append(buf)
            

    def update(self, section, params, index=""):
        line = None
        for s in params:
            s = str(s)
            if line is None:
                line = s
            elif len(line + s) + 1 < 64:
                line += "," + s
            else:
                self.add_line(section, line + ',', index=index)
                line = s
        self.add_line(section, line + ';', index=index)
        
    def updateP(self, params, index=""):
        line = None
        for s in params:
            s = str(s)
            if line is None:
                line = s
            elif len(line + s) + 1 < 64:
                line += "," + s
            else:
                self.add_lineP(line + ',', index=index)
                line = s
        self.add_lineP(line + ';', index=index)

    def start_section(self, comment=""):
        self.buffer[self.get_section("S")] = ""
        self.lineno[self.get_section("S")] = 0
        self.update("S", [comment])

    def global_section(self, filename=""):
        self.buffer[self.get_section("G")] = ""
        self.lineno[self.get_section("G")] = 0
        self.update("G", [
            "1H,",       # 1  parameter delimiter 
            "1H;",       # 2  record delimiter 
            "6HNoname",  # 3  product id of sending system
            hollerith(filename),  # 4  file name
            "6HNoname",  # 5  native system id
            "6HNoname",  # 6  preprocessor system  
            "32",        # 7  binary bits for integer
            "38",        # 8  max power represented by float
            "6",         # 9  number of significant digits in float
            "308",       # 10 max power represented in double
            "15",        # 11 number of significant digits in double
            "6HNoname",  # 12 product id of receiving system
            "1.00",      # 13 model space scale
            "2",         # 14 units flag (2=mm, 6=m)
            "2HMM",       # 15 units name (2HMM)
            "1",         # 16 number of line weight graduations
            "1.00",      # 17 width of max line weight
            "15H20181210.181412",  # 18 file generation time
            "1.0e-006",  # 19 min resolution
            "0.00",      # 20 max coordinate value
            "6HNoname",  # 21 author
            "6HNoname",  # 22 organization
            "11",        # 23 specification version
            "0",         # 24 drafting standard
            "15H20181210.181412",  # 25 time model was created
        ])

    def entity(self, code, params, label="", child=False):
        code = str(code)
        status = "00010001" if child else "1"
        dline = self.lineno[0] + 1
        pline = self.lineno[1] + 1
        self.buffer_D.append((
            "{:>8s}{:8d}{:8d}{:8d}{:8d}{:8d}{:8d}{:8d}{:>8s}D{:7d}\n".format(
            code, pline, 0, 0, 0, 0, 0, 0, status, dline) +
            "{:>8s}{:8d}{:8d}{:8d}{:8d}{:8d}{:8d}{:8s}{:8d}D{:7d}\n".format(
            code, 1, 0, 1, 0, 0, 0, label, 0, dline + 1)))
        self.updateP([code] + list(params), index=dline)
        self.lineno[0] = dline + 1
        return dline

    def pos(self, pt, origin):
        x, y, z = origin
        return (pt[0] + x, pt[1] + y, + pt[2] + z)

    def origin(self, size, origin, centerx=False, centery=False):
        w, h = size
        x, y, z = origin
        if centerx: x -= w / 2
        if centery: y -= h / 2
        return x, y, z

    ################

    def write(self, path, filename):
        self.start_section()
        self.global_section(filename)
        with open(path + filename, 'w') as f:
            f.write(self.buffer[2])
            f.write(self.buffer[3])
            f.write("".join(self.buffer_D))
            f.write("".join(self.buffer_P))
            f.write("S{:7d}G{:7d}D{:7d}P{:7d}{:40s}T{:7d}\n".format(
                self.lineno[2], self.lineno[3], 
                self.lineno[0], self.lineno[1], "", 1))

    def line(self, start, end, origin=(0,0,0), child=False):
        start = self.pos(start, origin)
        end = self.pos(end, origin)
        return self.entity(110, start + end, child=child)

