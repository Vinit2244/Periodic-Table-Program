# To download gtts(Google text to speech) use 'pip install gTTS' on the command prompt
# Run this file once if the audio files are not created

from gtts import gTTS
elemDict = {
    "1": "HYDROGEN",
    "2": "HELIUM",
    "3": "LITHIUM",
    "4": "BERYLLIUM",
    "5": "BORON",
    "6": "CARBON",
    "7": "NITROGEN",
    "8": "OXYGEN",
    "9": "FLUORINE",
    "10": "NEON",
    "11": "SODIUM",
    "12": "MAGNESIUM",
    "13": "ALUMINIUM",
    "14": "SILICON",
    "15": "PHOSPHORUS",
    "16": "SULPHUR",
    "17": "CHLORINE",
    "18": "ARGON",
    "19": "POTASSIUM",
    "20": "CALCIUM",
    "21": "SCANDIUM",
    "22": "TITANIUM",
    "23": "VANADIUM",
    "24": "CROMIUM",
    "25": "MANGANESE",
    "26": "IRON",
    "27": "COBALT",
    "28": "NICKEL",
    "29": "COPPER",
    "30": "ZINC",
    "31": "GALLIUM",
    "32": "GERMANIUM",
    "33": "ARSENIC",
    "34": "SELENIUM",
    "35": "BROMINE",
    "36": "KRYPTON",
    "37": "RUBIDIUM",
    "38": "STRONTIUM",
    "39": "YTTRIUM",
    "40": "ZIRCONIUM",
    "41": "NIOBIUM",
    "42": "MOLYBDENUM",
    "43": "TECHNETIUM",
    "44": "RUTHENIUM",
    "45": "RHODIUM",
    "46": "PALLADIUM",
    "47": "SILVER",
    "48": "CADMIUM",
    "49": "INDIUM",
    "50": "TIN",
    "51": "ANTIMONY",
    "52": "TELLURIUM",
    "53": "IODINE",
    "54": "XENON",
    "55": "CAESIUM",
    "56": "BARIUM",
    "57": "LANTHANUM",
    "58": "CERIUM",
    "59": "PRASEODYMIUM",
    "60": "NEODYMIUM",
    "61": "PROMETHIUM",
    "62": "SAMARIUM",
    "63": "EUROPIUM",
    "64": "GADOLINIUM",
    "65": "TERBIUM",
    "66": "DYSPROSIUM",
    "67": "HOLMIUM",
    "68": "ERBIUM",
    "69": "THULLIUM",
    "70": "YTTERBIUM",
    "71": "LUTETIUM",
    "72": "HAFNIUM",
    "73": "TANTALUM",
    "74": "TUNGSTEN",
    "75": "RHENIUM",
    "76": "OSMIUM",
    "77": "IRIDIUM",
    "78": "PLATINUM",
    "79": "GOLD",
    "80": "MERCURY",
    "81": "THALLIUM",
    "82": "LEAD",
    "83": "BISMUTH",
    "84": "POLONIUM",
    "85": "ASTATINE",
    "86": "RADON",
    "87": "FRANCIUM",
    "88": "RADIUM",
    "89": "ACTINIUM",
    "90": "THORIUM",
    "91": "PROTACTINIUM",
    "92": "URANIUM",
    "93": "NEPTUNIUM",
    "94": "PLUTONIUM",
    "95": "AMERICIUM",
    "96": "CURIUM",
    "97": "BERKELIUM",
    "98": "CALIFORNIUM",
    "99": "EINSTEINIUM",
    "100": "FERMIUM",
    "101": "MENDELEVIUM",
    "102": "NOBELIUM",
    "103": "LAWRENCIUM",
    "104": "RUTHERFORDIUM",
    "105": "DUBNIUM",
    "106": "SEABORGIUM",
    "107": "BOHRIUM",
    "108": "HASSIUM",
    "109": "MEITNERIUM",
    "110": "DARMSTADTIUM",
    "111": "ROENTGENIUM",
    "112": "COPERNICIUM",
    "113": "NIHONIUM",
    "114": "FLEROVIUM",
    "115": "MOSCOVIUM",
    "116": "LIVERMORIUM",
    "117": "TENNESSINE",
    "118": "OGANESSON"
}

for i in range(1,119):
    file = open("..\\Elements\\"+ elemDict[str(i)] +".txt", 'r')
    information = file.read()
    audio = gTTS(text = information)
    audio.save(elemDict[str(i)] + '.mp3')
    file.close()




















