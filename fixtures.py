import string
import random

class Fixtures:
    # Base sample record with 501 different words
    BASE_SAMPLE = [
        "certain", "careful", "imagine", "zesty", "ethereal", "stranger", "relax", "ground", "hospitable", "money", "hellish", "female", "animal", "beg", "sin", \
        "lick", "faded", "nose", "stick", "cook", "draconian", "effect", "ill-fated", "happy", "color", "naughty", "destruction", "receipt", "committee", "onerous", \
        "moaning", "pray", "craven", "bed", "literate", "neighborly", "distance", "energetic", "spicy", "authority", "start", "unknown", "open", "scrub", "legs", "pink", \
        "lucky", "wandering", "decorous", "phobic", "full", "symptomatic", "gabby", "file", "cloudy", "milk", "drunk", "shy", "limit", "competition", "expensive", "flower", \
        "bouncy", "brawny", "faulty", "panicky", "mess up", "answer", "condemned", "polish", "unable", "barbarous", "deafening", "foregoing", "drop", "trouble", "big", "top", \
        "taboo", "sail", "scissors", "oranges", "voyage", "smoggy", "scene", "cactus", "last", "train", "identify", "hurry", "mend", "dysfunctional", "spiffy", "expand", "birthday", \
        "bomb", "hateful", "damaged", "reduce", "brake", "clap", "approve", "aggressive", "balance", "squirrel", "soft", "magenta", "curly", "statement", "milky", "strap", "four", \
        "wound", "cream", "sneaky", "electric", "fence", "prick", "kindhearted", "extend", "deadpan", "scared", "past", "command", "gentle", "didactic", "lewd", "dramatic", "stay", \
        "poor", "grass", "stimulating", "share", "prefer", "test", "elastic", "pies", "judicious", "rod", "wren", "steel", "futuristic", "questionable", "fireman", "scary", "boil", \
        "shock", "guiltless", "tap", "surround", "simple", "upbeat", "arithmetic", "pan", "punch", "cheap", "elite", "oval", "numerous", "humdrum", "steam", "delirious", "toe", \
        "hilarious", "compare", "petite", "mist", "lettuce", "eggnog", "suggest", "real", "pat", "adamant", "alert", "post", "monkey", "yell", "branch", "ratty", "trade", "soda", \
        "spectacular", "size", "assorted", "doll", "valuable", "brainy", "rightful", "happen", "plain", "wholesale", "writer", "grandfather", "feigned", "house", "wrestle", "cold", \
        "bad", "watch", "spotty", "collar", "fax", "teeny-tiny", "travel", "imperfect", "rejoice", "fabulous", "voracious", "jeans", "nosy", "believe", "shirt", "handsomely", "dream", \
        "pear", "blind", "drawer", "flight", "labored", "squalid", "weight", "develop", "fixed", "absent", "volcano", "hang", "reflect", "mug", "agreement", "irritating", "label", \
        "troubled", "damage", "pets", "excuse", "quick", "chase", "narrow", "kittens", "gaudy", "obedient", "adorable", "camp", "enchanted", "spoon", "search", "thought", "shave", \
        "functional", "quilt", "classy", "chilly", "vein", "passenger", "rake", "chew", "lighten", "lavish", "fold", "possible", "supply", "ants", "uncovered", "school", "near", "curl", \
        "bleach", "chubby", "silky", "analyze", "dear", "friend", "continue", "argument", "outgoing", "pancake", "disappear", "horse", "education", "sprout", "lackadaisical", "kindly", \
        "small", "unarmed", "seashore", "unlock", "dusty", "crowded", "gray", "tasteful", "tip", "breezy", "stove", "gaping", "eminent", "amused", "knife", "railway", "cows", "harm", \
        "hobbies", "hop", "sour", "poised", "sock", "awake", "veil", "dizzy", "crook", "gleaming", "sea", "tick", "tickle", "misty", "signal", "wonder", "love", "pipe", "vigorous", \
        "tiger", "false", "materialistic", "watery", "jumbled", "minor", "subdued", "rare", "oceanic", "seemly", "grin", "match", "sad", "adventurous", "hospital", "sidewalk", "texture", \
        "soap", "testy", "madly", "rose", "treat", "best", "bells", "befitting", "inexpensive", "efficacious", "eggs", "raise", "yoke", "dust", "sun", "uncle", "alike", "shade", "pigs", \
        "inquisitive", "staking", "jobless", "nifty", "giants", "superb", "bucket", "call", "practice", "offend", "alive", "temporary", "alluring", "intend", "fine", "repeat", \
        "representative", "undesirable", "sophisticated", "violet", "close", "innocent", "vegetable", "adjustment", "guitar", "aftermath", "wander", "pretend", "tremendous", \
        "cannon", "payment", "rule", "support", "solid", "button", "remarkable", "demonic", "grip", "illustrious", "heat", "frightening", "scrape", "industrious", "grandmother", \
        "throat", "new", "sudden", "special", "coast", "collect", "debonair", "straw", "wry", "spotless", "innate", "sip", "salty", "tiresome", "help", "spill", "rings", "uptight", \
        "youthful", "pleasure", "mysterious", "chop", "thin", "pull", "two", "common", "zoo", "army", "windy", "bow", "smiling", "snake", "toad", "time", "erratic", "tree", "cast", \
        "separate", "leg", "mother", "back", "halting", "actually", "nippy", "tomatoes", "middle", "brick", "robust", "wakeful", "action", "bruise", "spurious", "outstanding", \
        "thoughtless", "cross", "stage", "baby", "sweater", "stupid", "impolite", "dead", "stretch", "rinse", "foamy", "library", "board", "carve", "defeated", "sordid", "girl", \
        "show", "elderly", "place", "sparkle", "invite", "winter", "miss", "like", "tin", "woman", "measure", "suit", "little", "describe", "psychedelic", "delay", "sick", "sense", \
        "sleep", "guide", "harass", "object", "rain", "curvy", "loaf", "knowledgeable", "possessive", "cover", "synonymous", "ablaze", "wind", "lethal"
        ] 

    COUNT = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"
    ]

    SAMPLE_WITH_MAX_RECORD = [
        "this_string_is_oversized_" + ''.join(random.choices(string.ascii_letters,
                             k=1000000)),
        "this_string_is_not_oversized_1",
        "this_string_is_oversized_" + ''.join(random.choices(string.ascii_letters,
                             k=1000000)),
        "this_string_is_not_oversized_2"
    ]

    SAMPLE_WITH_MAX_BATCH = [
    ''.join(random.choices(string.ascii_letters,
                                k=1000000)),
    ''.join(random.choices(string.ascii_letters,
                                k=1000000)),
    ''.join(random.choices(string.ascii_letters,
                                k=1000000)),
    ''.join(random.choices(string.ascii_letters,
                                k=1000000)),
    ''.join(random.choices(string.ascii_letters,
                                k=1000000)),
    ''.join(random.choices(string.ascii_letters,
                                k=500000)),
    ''.join(random.choices(string.ascii_letters,
                                k=500000)),
    ]

    SAMPLE_WITH_501_ENTRIES =  [ ''.join(random.choices(string.ascii_letters,
                                k=5)) for x in range(550) ]

    SAMPLE_COMBINATION = SAMPLE_WITH_MAX_RECORD + SAMPLE_WITH_MAX_BATCH + SAMPLE_WITH_501_ENTRIES
