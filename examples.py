"""Example usage of mania2json package"""

from mania2json import mania_file_parser, mania_mapset_parser


# example use with a single file
maniap = mania_file_parser()
maniap.light_parse(file_path="xi - .357 Magnum (Akali) [4K Hyper].osu")
print(maniap.__dict__)


# example use with a songs directory
dir = "C:\\Users\\phile\\AppData\\Local\\osu!\\Songs\\" 
parser = mania_mapset_parser()  
mapset_data = parser.get_mania_mapsets_from_folder(directory=dir, max_workers=1)
print(f"Found {len(mapset_data)} mania mapsets in {dir} ({sum(len(maps) for maps in mapset_data.values())} maps)")


# save all mapsets to a single JSON file
parser.save_mapsets_to_json(mapset_data, "all_mapsets.json")


# or save individual mapsets
for mapset_id, mapset_content in mapset_data.items():
    parser.save_mapsets_to_json({mapset_id: mapset_content}, f"songs\\{mapset_id}.json")
