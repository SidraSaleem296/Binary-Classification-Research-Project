import os
import json
from idautils import *
from idaapi import *
from idc import *
from graph_analysis_ida import *
from preprocessing_ida import *
from raw_graphs import *
from cfg_constructor import getCfg

def process_exes():
    folder_path = r"C:\Users\sidra\MalGraph-main\raw-feature-extractor\Exes"  # Replace with the path to the folder containing the binary files

    exe_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.exe')]

    result = {}
    result['function_names'] = []
    result['function_edges'] = []
    result['acfg_list'] = []

    for exe_file in exe_files:
        binary_path = os.path.join(folder_path, exe_file)
        idc.SetInputFilePath(binary_path)
        idaapi.autoWait()

        # Construct CFG
        func = idaapi.get_func(idaapi.get_screen_ea())
        externs_eas = []  # Replace with the required externs_eas argument
        ea_externs = {}   # Replace with the required ea_externs argument
        cfg, start_node = getCfg(func, externs_eas, ea_externs)
        cfg_graph = nx.DiGraph(cfg)

        # Discover Re
        dr = DiscovRe()
        acfg = dr.discover_re(cfg_graph)
        acfg_dict = acfg.to_dict()

        # Graph Analysis
        graph_analysis = GraphAnalysisData()
        graph_analysis.analyze_graph(acfg)

        # Graph Property
        graph_property = GraphProperty()
        function_edges = graph_property.get_function_edges(acfg)
        result['function_edges'].append(function_edges)

        # Preprocessing
        preprocessing = PreprocessingIDA()
        acfg_list = preprocessing.process_acfg_list(acfg_dict)
        result['acfg_list'].extend(acfg_list)

        # Store function names
        for func in cfg.nodes():
            result['function_names'].append(func)

    # Calculate hash
    hash_value = calculate_hash(folder_path)
    result['hash'] = hash_value

    # Store function number
    result['function_number'] = len(result['function_names'])

    # Generate a unique output file name for each EXE file
    output_file = os.path.join(folder_path, f"{os.path.splitext(exe_file)[0]}.json")

    # Save result to JSON file
    json_output = json.dumps(result)
    with open(output_file, 'w') as f:
        f.write(json_output)

print(f"Saved JSON file: {output_file}")

    print("Transformation completed.")

def calculate_hash(folder_path):
    import hashlib
    hash_object = hashlib.sha256()

    exe_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.exe')]
    for exe_file in exe_files:
        binary_path = os.path.join(folder_path, exe_file)
        with open(binary_path, 'rb') as f:
            data = f.read()
            hash_object.update(data)

    return hash_object.hexdigest()

if __name__ == '__main__':
    process_exes()
