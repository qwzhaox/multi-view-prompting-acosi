import json
from pathlib import Path
from ast import literal_eval

senttag2opinion = {"pos": "great", "neg": "bad", "neu": "ok"}
sentword2opinion = {
    "positive": "great",
    "negative": "bad",
    "neutral": "ok",
}

rest_aspect_cate_list = [
    "location general",
    "food prices",
    "food quality",
    "food general",
    "ambience general",
    "service general",
    "restaurant prices",
    "drinks prices",
    "restaurant miscellaneous",
    "drinks quality",
    "drinks style_options",
    "restaurant general",
    "food style_options",
]

laptop_aspect_cate_list = [
    "keyboard operation_performance",
    "os operation_performance",
    "out_of_scope operation_performance",
    "ports general",
    "optical_drives general",
    "laptop operation_performance",
    "optical_drives operation_performance",
    "optical_drives usability",
    "multimedia_devices general",
    "keyboard general",
    "os miscellaneous",
    "software operation_performance",
    "display operation_performance",
    "shipping quality",
    "hard_disc quality",
    "motherboard general",
    "graphics general",
    "multimedia_devices connectivity",
    "display general",
    "memory operation_performance",
    "os design_features",
    "out_of_scope usability",
    "software design_features",
    "graphics design_features",
    "ports connectivity",
    "support design_features",
    "display quality",
    "software price",
    "shipping general",
    "graphics operation_performance",
    "hard_disc miscellaneous",
    "display design_features",
    "cpu operation_performance",
    "mouse general",
    "keyboard portability",
    "hardware price",
    "support quality",
    "hardware quality",
    "motherboard operation_performance",
    "multimedia_devices quality",
    "battery design_features",
    "mouse usability",
    "os price",
    "shipping operation_performance",
    "laptop quality",
    "laptop portability",
    "fans&cooling general",
    "battery general",
    "os usability",
    "hardware usability",
    "optical_drives design_features",
    "fans&cooling operation_performance",
    "memory general",
    "company general",
    "power_supply general",
    "hardware general",
    "mouse design_features",
    "software general",
    "keyboard quality",
    "power_supply quality",
    "software quality",
    "multimedia_devices usability",
    "power_supply connectivity",
    "multimedia_devices price",
    "multimedia_devices operation_performance",
    "ports design_features",
    "hardware operation_performance",
    "shipping price",
    "hardware design_features",
    "memory usability",
    "cpu quality",
    "ports quality",
    "ports portability",
    "motherboard quality",
    "display price",
    "os quality",
    "graphics usability",
    "cpu design_features",
    "hard_disc general",
    "hard_disc operation_performance",
    "battery quality",
    "laptop usability",
    "company design_features",
    "company operation_performance",
    "support general",
    "fans&cooling quality",
    "memory design_features",
    "ports usability",
    "hard_disc design_features",
    "power_supply design_features",
    "keyboard miscellaneous",
    "laptop miscellaneous",
    "keyboard usability",
    "cpu price",
    "laptop design_features",
    "keyboard price",
    "warranty quality",
    "display usability",
    "support price",
    "cpu general",
    "out_of_scope design_features",
    "out_of_scope general",
    "software usability",
    "laptop general",
    "warranty general",
    "company price",
    "ports operation_performance",
    "power_supply operation_performance",
    "keyboard design_features",
    "support operation_performance",
    "hard_disc usability",
    "os general",
    "company quality",
    "memory quality",
    "software portability",
    "fans&cooling design_features",
    "multimedia_devices design_features",
    "laptop connectivity",
    "battery operation_performance",
    "hard_disc price",
    "laptop price",
]


def get_acosi_categories():
    unique_categories = set()

    def add_categories(file_path):
        with open(file_path, "r") as file:
            # Iterate through each line in the file
            for line in file:
                # Split the line by '####' to separate the review text from annotations
                parts = line.split("####")
                if len(parts) == 2:
                    # Extract the annotations part and split it by ','
                    annotations = literal_eval(parts[1].strip())
                    # Iterate through each annotation and extract the category
                    for annotation in annotations:
                        category = annotation[1].strip()
                        unique_categories.add(category)

#    task = "acos"
    task = "acosi"

    train = Path(f"../data/{task}/shoes/train.txt")
    test = Path(f"../data/{task}/shoes/test.txt")
    dev = Path(f"../data/{task}/shoes/dev.txt")

    add_categories(
        train.resolve()
    )
    add_categories(
        test.resolve()
    )
    add_categories(
        dev.resolve()
    )
    # Convert the set of unique categories to a sorted list
    category_list = sorted(list(unique_categories))
    return category_list


shoes_aspect_cate_list = get_acosi_categories()

# force_tokens = {}

# if os.path.exists("./force_tokens.json"):
with open("force_tokens.json", "r") as f:
    force_tokens = json.load(f)

cate_list = {
    "rest14": rest_aspect_cate_list,
    "rest15": rest_aspect_cate_list,
    "rest": rest_aspect_cate_list,
    "rest16": rest_aspect_cate_list,
    "laptop": laptop_aspect_cate_list,
    "laptop14": laptop_aspect_cate_list,
    "shoes": shoes_aspect_cate_list,
}

task_data_list = {
    "aste": ["laptop14", "rest14", "rest15", "rest16"],
    "tasd": ["rest15", "rest16"],
    "acos": ["laptop16", "rest16"],
#    "acos": ["laptop16", "rest16", "shoes"],
    "acosi": ["shoes"],
    "asqp": ["rest15", "rest16"],
}

force_words = {
    "aste": {
        "rest15": list(senttag2opinion.values()) + ["[SSEP]"],
        "rest16": list(senttag2opinion.values()) + ["[SSEP]"],
        "rest14": list(senttag2opinion.values()) + ["[SSEP]"],
        "laptop14": list(senttag2opinion.values()) + ["[SSEP]"],
    },
    "tasd": {
        "rest15": rest_aspect_cate_list + list(sentword2opinion.values()) + ["[SSEP]"],
        "rest16": rest_aspect_cate_list + list(sentword2opinion.values()) + ["[SSEP]"],
    },
    "acos": {
        "rest": rest_aspect_cate_list + list(sentword2opinion.values()) + ["[SSEP]"],
        "laptop": laptop_aspect_cate_list
        + list(sentword2opinion.values())
        + ["[SSEP]"],
#        "shoes": shoes_aspect_cate_list + list(sentword2opinion.values()) + ["[SSEP]"],
    },
    "acosi": {
        "shoes": shoes_aspect_cate_list + list(sentword2opinion.values()) + ["[SSEP]"]
    },
    "asqp": {
        "rest15": rest_aspect_cate_list + list(sentword2opinion.values()) + ["[SSEP]"],
        "rest16": rest_aspect_cate_list + list(sentword2opinion.values()) + ["[SSEP]"],
    },
}


optim_orders_all = {
    "aste": {
        "laptop14": [
            "[O] [A] [S]",
            "[A] [O] [S]",
            "[O] [S] [A]",
            "[A] [S] [O]",
            "[S] [O] [A]",
            "[S] [A] [O]",
        ],
        "rest14": [
            "[O] [A] [S]",
            "[O] [S] [A]",
            "[A] [O] [S]",
            "[A] [S] [O]",
            "[S] [O] [A]",
            "[S] [A] [O]",
        ],
        "rest15": [
            "[A] [O] [S]",
            "[O] [A] [S]",
            "[O] [S] [A]",
            "[A] [S] [O]",
            "[S] [O] [A]",
            "[S] [A] [O]",
        ],
        "rest16": [
            "[O] [A] [S]",
            "[A] [O] [S]",
            "[O] [S] [A]",
            "[A] [S] [O]",
            "[S] [O] [A]",
            "[S] [A] [O]",
        ],
    },
    "tasd": {
        "rest15": [
            "[A] [C] [S]",
            "[A] [S] [C]",
            "[C] [S] [A]",
            "[C] [A] [S]",
            "[S] [C] [A]",
            "[S] [A] [C]",
        ],
        "rest16": [
            "[A] [C] [S]",
            "[A] [S] [C]",
            "[C] [S] [A]",
            "[C] [A] [S]",
            "[S] [C] [A]",
            "[S] [A] [C]",
        ],
    },
    "acos": {
        "laptop16": [  # ot null -> sp
            "[A] [O] [S] [C]",
            "[A] [S] [O] [C]",
            "[A] [O] [C] [S]",
            "[O] [A] [S] [C]",
            "[O] [A] [C] [S]",
            "[A] [S] [C] [O]",
            "[A] [C] [O] [S]",
            "[O] [C] [A] [S]",
            "[O] [S] [A] [C]",
            "[A] [C] [S] [O]",
            "[O] [C] [S] [A]",
            "[O] [S] [C] [A]",
            "[S] [A] [O] [C]",
            "[C] [O] [A] [S]",
            "[C] [S] [A] [O]",
            "[C] [A] [O] [S]",
            "[C] [S] [O] [A]",
            "[C] [O] [S] [A]",
            "[S] [O] [A] [C]",
            "[C] [A] [S] [O]",
            "[S] [O] [C] [A]",
            "[S] [C] [O] [A]",
            "[S] [A] [C] [O]",
            "[S] [C] [A] [O]",
        ],
        "rest16": [  # ot null -> sp
            "[A] [O] [S] [C]",
            "[A] [O] [C] [S]",
            "[A] [S] [O] [C]",
            "[O] [A] [C] [S]",
            "[O] [A] [S] [C]",
            "[O] [S] [C] [A]",
            "[A] [C] [O] [S]",
            "[O] [C] [A] [S]",
            "[O] [S] [A] [C]",
            "[A] [S] [C] [O]",
            "[A] [C] [S] [O]",
            "[O] [C] [S] [A]",
            "[C] [O] [A] [S]",
            "[C] [A] [O] [S]",
            "[C] [S] [O] [A]",
            "[C] [O] [S] [A]",
            "[S] [A] [O] [C]",
            "[C] [S] [A] [O]",
            "[C] [A] [S] [O]",
            "[S] [O] [A] [C]",
            "[S] [C] [O] [A]",
            "[S] [O] [C] [A]",
            "[S] [C] [A] [O]",
            "[S] [A] [C] [O]",
        ],
        "shoes": [
            "[A] [O] [S] [C]",
            "[A] [O] [C] [S]",
            "[A] [S] [O] [C]",
            "[O] [A] [C] [S]",
            "[O] [A] [S] [C]",
            "[O] [S] [C] [A]",
            "[A] [C] [O] [S]",
            "[O] [C] [A] [S]",
            "[O] [S] [A] [C]",
            "[A] [S] [C] [O]",
            "[A] [C] [S] [O]",
            "[O] [C] [S] [A]",
            "[C] [O] [A] [S]",
            "[C] [A] [O] [S]",
            "[C] [S] [O] [A]",
            "[C] [O] [S] [A]",
            "[S] [A] [O] [C]",
            "[C] [S] [A] [O]",
            "[C] [A] [S] [O]",
            "[S] [O] [A] [C]",
            "[S] [C] [O] [A]",
            "[S] [O] [C] [A]",
            "[S] [C] [A] [O]",
            "[S] [A] [C] [O]",
        ]
    },
    "acosi": {
       "shoes": [
           "[A] [O] [S] [C] [I]",
           "[A] [O] [S] [I] [C]",
           "[A] [O] [C] [S] [I]",
           "[A] [O] [C] [I] [S]",
           "[A] [O] [I] [S] [C]",
           "[A] [O] [I] [C] [S]",
           "[A] [S] [O] [C] [I]",
           "[A] [S] [O] [I] [C]",
           "[A] [S] [C] [O] [I]",
           "[A] [S] [C] [I] [O]",
           "[A] [S] [I] [O] [C]",
           "[A] [S] [I] [C] [O]",
           "[A] [C] [O] [S] [I]",
           "[A] [C] [O] [I] [S]",
           "[A] [C] [S] [O] [I]",
           "[A] [C] [S] [I] [O]",
           "[A] [C] [I] [O] [S]",
           "[A] [C] [I] [S] [O]",
           "[A] [I] [O] [S] [C]",
           "[A] [I] [O] [C] [S]",
           "[A] [I] [S] [O] [C]",
           "[A] [I] [S] [C] [O]",
           "[A] [I] [C] [O] [S]",
           "[A] [I] [C] [S] [O]",
           "[O] [A] [S] [C] [I]",
           "[O] [A] [S] [I] [C]",
           "[O] [A] [C] [S] [I]",
           "[O] [A] [C] [I] [S]",
           "[O] [A] [I] [S] [C]",
           "[O] [A] [I] [C] [S]",
           "[O] [S] [A] [C] [I]",
           "[O] [S] [A] [I] [C]",
           "[O] [S] [C] [A] [I]",
           "[O] [S] [C] [I] [A]",
           "[O] [S] [I] [A] [C]",
           "[O] [S] [I] [C] [A]",
           "[O] [C] [A] [S] [I]",
           "[O] [C] [A] [I] [S]",
           "[O] [C] [S] [A] [I]",
           "[O] [C] [S] [I] [A]",
           "[O] [C] [I] [A] [S]",
           "[O] [C] [I] [S] [A]",
           "[O] [I] [A] [S] [C]",
           "[O] [I] [A] [C] [S]",
           "[O] [I] [S] [A] [C]",
           "[O] [I] [S] [C] [A]",
           "[O] [I] [C] [A] [S]",
           "[O] [I] [C] [S] [A]",
           "[S] [A] [O] [C] [I]",
           "[S] [A] [O] [I] [C]",
           "[S] [A] [C] [O] [I]",
           "[S] [A] [C] [I] [O]",
           "[S] [A] [I] [O] [C]",
           "[S] [A] [I] [C] [O]",
           "[S] [O] [A] [C] [I]",
           "[S] [O] [A] [I] [C]",
           "[S] [O] [C] [A] [I]",
           "[S] [O] [C] [I] [A]",
           "[S] [O] [I] [A] [C]",
           "[S] [O] [I] [C] [A]",
           "[S] [C] [A] [O] [I]",
           "[S] [C] [A] [I] [O]",
           "[S] [C] [O] [A] [I]",
           "[S] [C] [O] [I] [A]",
           "[S] [C] [I] [A] [O]",
           "[S] [C] [I] [O] [A]",
           "[S] [I] [A] [O] [C]",
           "[S] [I] [A] [C] [O]",
           "[S] [I] [O] [A] [C]",
           "[S] [I] [O] [C] [A]",
           "[S] [I] [C] [A] [O]",
           "[S] [I] [C] [O] [A]",
           "[C] [A] [O] [S] [I]",
           "[C] [A] [O] [I] [S]",
           "[C] [A] [S] [O] [I]",
           "[C] [A] [S] [I] [O]",
           "[C] [A] [I] [O] [S]",
           "[C] [A] [I] [S] [O]",
           "[C] [O] [A] [S] [I]",
           "[C] [O] [A] [I] [S]",
           "[C] [O] [S] [A] [I]",
           "[C] [O] [S] [I] [A]",
           "[C] [O] [I] [A] [S]",
           "[C] [O] [I] [S] [A]",
           "[C] [S] [A] [O] [I]",
           "[C] [S] [A] [I] [O]",
           "[C] [S] [O] [A] [I]",
           "[C] [S] [O] [I] [A]",
           "[C] [S] [I] [A] [O]",
           "[C] [S] [I] [O] [A]",
           "[C] [I] [A] [O] [S]",
           "[C] [I] [A] [S] [O]",
           "[C] [I] [O] [A] [S]",
           "[C] [I] [O] [S] [A]",
           "[C] [I] [S] [A] [O]",
           "[C] [I] [S] [O] [A]",
           "[I] [A] [O] [S] [C]",
           "[I] [A] [O] [C] [S]",
           "[I] [A] [S] [O] [C]",
           "[I] [A] [S] [C] [O]",
           "[I] [A] [C] [O] [S]",
           "[I] [A] [C] [S] [O]",
           "[I] [O] [A] [S] [C]",
           "[I] [O] [A] [C] [S]",
           "[I] [O] [S] [A] [C]",
           "[I] [O] [S] [C] [A]",
           "[I] [O] [C] [A] [S]",
           "[I] [O] [C] [S] [A]",
           "[I] [S] [A] [O] [C]",
           "[I] [S] [A] [C] [O]",
           "[I] [S] [O] [A] [C]",
           "[I] [S] [O] [C] [A]",
           "[I] [S] [C] [A] [O]",
           "[I] [S] [C] [O] [A]",
           "[I] [C] [A] [O] [S]",
           "[I] [C] [A] [S] [O]",
           "[I] [C] [O] [A] [S]",
           "[I] [C] [O] [S] [A]",
           "[I] [C] [S] [A] [O]",
           "[I] [C] [S] [O] [A]",
       ]
    },
    "asqp": {
        "rest15": [
            "[A] [O] [S] [C]",
            "[O] [A] [C] [S]",
            "[A] [O] [C] [S]",
            "[O] [A] [S] [C]",
            "[O] [S] [C] [A]",
            "[A] [S] [O] [C]",
            "[O] [C] [A] [S]",
            "[O] [S] [A] [C]",
            "[A] [C] [O] [S]",
            "[O] [C] [S] [A]",
            "[A] [C] [S] [O]",
            "[C] [O] [A] [S]",
            "[A] [S] [C] [O]",
            "[C] [A] [O] [S]",
            "[C] [S] [O] [A]",
            "[C] [O] [S] [A]",
            "[C] [S] [A] [O]",
            "[C] [A] [S] [O]",
            "[S] [A] [O] [C]",
            "[S] [O] [A] [C]",
            "[S] [C] [O] [A]",
            "[S] [O] [C] [A]",
            "[S] [C] [A] [O]",
            "[S] [A] [C] [O]",
        ],
        "rest16": [
            "[O] [A] [C] [S]",
            "[A] [O] [S] [C]",
            "[O] [A] [S] [C]",
            "[O] [S] [C] [A]",
            "[A] [O] [C] [S]",
            "[O] [S] [A] [C]",
            "[O] [C] [A] [S]",
            "[A] [S] [O] [C]",
            "[O] [C] [S] [A]",
            "[A] [C] [O] [S]",
            "[A] [C] [S] [O]",
            "[C] [O] [A] [S]",
            "[A] [S] [C] [O]",
            "[C] [A] [O] [S]",
            "[C] [O] [S] [A]",
            "[C] [S] [O] [A]",
            "[C] [S] [A] [O]",
            "[S] [A] [O] [C]",
            "[C] [A] [S] [O]",
            "[S] [O] [A] [C]",
            "[S] [O] [C] [A]",
            "[S] [C] [O] [A]",
            "[S] [C] [A] [O]",
            "[S] [A] [C] [O]",
        ],
    },
}


heuristic_orders = {
    "aste": ["[A] [O] [S]"],
    "tasd": ["[A] [C] [S]"],
    "asqp": ["[A] [O] [C] [S]"],
    "acos": ["[A] [O] [C] [S]"],
    "acosi": ["[A] [O] [C] [S] [I]"],
}
