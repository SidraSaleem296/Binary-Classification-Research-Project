# import os
# import json
# import pickle
# from glob import glob
# import networkx as nx
# from networkx.drawing.nx_agraph import graphviz_layout
# 
# # Directory path to convert JSON to pickle
# directory_path = "D:\Downloads(D)\Testing"
# 
# # Output directory for the pickle files
# output_dir = "D:\Downloads(D)\Testing\Output"
# 
# # Create the output directory if it doesn't exist
# os.makedirs(output_dir, exist_ok=True)
# 
# # List the JSON files in the directory
# json_files = glob(directory_path)
# 
# # Process each JSON file
# for json_file in json_files:
#     try:
#         # Load the JSON data
#         with open(json_file, 'r') as file:
#             graph_data = json.load(file)
# 
#         # Extract the necessary information from the graph_data dictionary
#         node_dict = graph_data['node_dict']
#         edge_list = graph_data['edge_list']
#         label = graph_data['label']
# 
#         # Create a NetworkX graph from the extracted data
#         graph = nx.DiGraph()
#         for node_addr, node_data in node_dict.items():
#             graph.add_node(node_addr, **node_data)
#         graph.add_edges_from(edge_list)
# 
#         # Apply Graphviz layout to the graph to prevent node overlap
#         pos = graphviz_layout(graph, prog='dot')
# 
#         # Save the processed graph in pickle format
#         pickle_file = os.path.join(output_dir, os.path.basename(json_file) + '.pickle')
#         with open(pickle_file, 'wb') as file:
#             pickle.dump((graph, pos, label), file)
# 
#     except Exception as e:
#         print(f"Error processing {json_file}: {e}")
# 
# print("Conversion completed.")
# import json
# 
# def parse_asm_file(asm_file_path, json_file_path):
#     functions = {}  # Store function definitions
#     nodes = []      # Store nodes
#     edges = []      # Store edges
# 
#     with open(asm_file_path, "r", encoding="utf-8") as asm_file:
#         # Step 1: Identify Functions
#         for line in asm_file:
#             if line.strip().startswith("sub_"):
#                 function_name = line.split()[0].strip()
#                 functions[function_name] = len(nodes)  # Store the function name and its corresponding node index
# 
#         asm_file.seek(0)  # Reset the file pointer to the beginning
# 
#         # Step 2: Create Nodes
#         for function_name, node_index in functions.items():
#             nodes.append({
#                 "name": function_name,
#                 "type": "function",
#                 "instructions": [],
#                 "num_instructions": 0
#                 # Include other relevant attributes for the node
#             })
# 
#         # Step 3: Extract Instructions
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 continue
#             if current_function is not None:
#                 if line.startswith("loc_"):
#                     instruction_address = line.split(":")[0].strip()
#                     opcode = line.split(":")[1].strip()
#                     nodes.append({
#                         "name": opcode,
#                         "type": "instruction",
#                         "address": instruction_address
#                         # Include other relevant attributes for the node
#                     })
#                     nodes[functions[current_function]]["instructions"].append(instruction_address)
#                     nodes[functions[current_function]]["num_instructions"] += 1
# 
#         asm_file.seek(0)  # Reset the file pointer to the beginning
# 
#         # Step 4: Identify Edges
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 continue
#             if current_function is not None:
#                 if "jmp" in line or "call" in line:
#                     source_address = line.split(":")[0].strip()
#                     target_address = line.split()[-1].strip()
#                     edges.append({
#                         "source": source_address,
#                         "target": target_address
#                         # Include other relevant attributes for the edge
#                     })
# 
#     # Build the JSON representation
#     cfg = {
#         "nodes": nodes,
#         "edges": edges
#     }
#     json_data = json.dumps(cfg, indent=4)
# 
#     # Save the JSON file
#     with open(json_file_path, "w") as json_file:
#         json_file.write(json_data)
# 
# # Usage example
# asm_file_path = "D:\Downloads(D)\Testing\Windows.asm"
# json_file_path = "D:\\Downloads\\Testing\\asm2json.json"
# parse_asm_file(asm_file_path, json_file_path)
# import json
# import os
# 
# def parse_asm_file(asm_file_path):
#     # Extract the directory and filename from the ASM file path
#     asm_directory = os.path.dirname(asm_file_path)
#     asm_filename = os.path.splitext(os.path.basename(asm_file_path))[0]
# 
#     # Construct the JSON file path in the same directory as the ASM file
#     json_file_path = os.path.join(asm_directory, f"{asm_filename}.json")
# 
#     functions = {}  # Store function definitions
#     nodes = []      # Store nodes
#     edges = []      # Store edges
# 
#     with open(asm_file_path, "r", encoding="utf-8") as asm_file:
#         # Step 1: Identify Functions
#         for line in asm_file:
#             if line.strip().startswith("sub_"):
#                 function_name = line.split()[0].strip()
#                 functions[function_name] = len(nodes)  # Store the function name and its corresponding node index
# 
#         asm_file.seek(0)  # Reset the file pointer to the beginning
# 
#         # Step 2: Create Nodes
#         for function_name, node_index in functions.items():
#             nodes.append({
#                 "name": function_name,
#                 "type": "function",
#                 "instructions": [],
#                 "num_instructions": 0
#                 # Include other relevant attributes for the node
#             })
# 
#         # Step 3: Extract Instructions
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 continue
#             if current_function is not None:
#                 if line.startswith("loc_"):
#                     instruction_address = line.split(":")[0].strip()
#                     opcode = line.split(":")[1].strip()
#                     nodes.append({
#                         "name": opcode,
#                         "type": "instruction",
#                         "address": instruction_address
#                         # Include other relevant attributes for the node
#                     })
#                     nodes[functions[current_function]]["instructions"].append(instruction_address)
#                     nodes[functions[current_function]]["num_instructions"] += 1
# 
#         asm_file.seek(0)  # Reset the file pointer to the beginning
# 
#         # Step 4: Identify Edges
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 continue
#             if current_function is not None:
#                 if "jmp" in line or "call" in line:
#                     source_address = line.split(":")[0].strip()
#                     target_address = line.split()[-1].strip()
#                     edges.append({
#                         "source": source_address,
#                         "target": target_address
#                         # Include other relevant attributes for the edge
#                     })
# 
#     # Build the JSON representation
#     cfg = {
#         "nodes": nodes,
#         "edges": edges
#     }
#     json_data = json.dumps(cfg, indent=4)
# 
#     # Save the JSON file in the same directory as the ASM file
#     with open(json_file_path, "w") as json_file:
#         json_file.write(json_data)
# 
# # Usage example
# asm_file_path = r"D:\Downloads(D)\Testing\Windows.asm"
# parse_asm_file(asm_file_path)


# import json
# import os
# 
# def parse_asm_file(asm_file_path):
#     # Extract the directory and filename from the ASM file path
#     asm_directory = os.path.dirname(asm_file_path)
#     asm_filename = os.path.splitext(os.path.basename(asm_file_path))[0]
# 
#     # Construct the JSON file path in the same directory as the ASM file
#     json_file_path = os.path.join(asm_directory, f"{asm_filename}.json")
# 
#     functions = {}  # Store function definitions
#     nodes = []      # Store nodes
#     edges = []      # Store edges
# 
#     with open(asm_file_path, "r", encoding="utf-8") as asm_file:
#         # Step 1: Identify Functions
#         for line in asm_file:
#             if line.strip().startswith("sub_"):
#                 function_name = line.split()[0].strip()
#                 functions[function_name] = len(nodes)  # Store the function name and its corresponding node index
# 
#         asm_file.seek(0)  # Reset the file pointer to the beginning
# 
#         # Step 2: Create Nodes
#         for function_name, node_index in functions.items():
#             nodes.append({
#                 "name": function_name,
#                 "type": "function",
#                 "instructions": [],
#                 "num_instructions": 0
#                 # Include other relevant attributes for the node
#             })
# 
#         # Step 3: Extract Instructions
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 continue
#             if current_function is not None:
#                 if line.startswith("loc_"):
#                     instruction_address = line.split(":")[0].strip()
#                     opcode = line.split(":")[1].strip()
#                     nodes.append({
#                         "name": opcode,
#                         "type": "instruction",
#                         "address": instruction_address
#                         # Include other relevant attributes for the node
#                     })
#                     nodes[functions[current_function]]["instructions"].append(instruction_address)
#                     nodes[functions[current_function]]["num_instructions"] += 1
# 
#         asm_file.seek(0)  # Reset the file pointer to the beginning
# 
#         # Step 4: Identify Edges
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 continue
#             if current_function is not None:
#                 if "jmp" in line or "call" in line:
#                     source_address = line.split(":")[0].strip()
#                     target_address = line.split()[-1].strip()
#                     edges.append((source_address, target_address))
# 
#     # Build the JSON representation
#     cfg = {
#         "nodes": nodes,
#         "edges": edges
#     }
#     json_data = json.dumps(cfg, indent=4)
# 
#     # Save the JSON file in the same directory as the ASM file
#     with open(json_file_path, "w") as json_file:
#         json_file.write(json_data)
# 
#     # Save the edge list file in the same directory as the ASM file
#     edge_list_file_path = os.path.join(asm_directory, f"{asm_filename}_edge_list.txt")
#     with open(edge_list_file_path, "w") as edge_list_file:
#         for edge in edges:
#             edge_list_file.write(f"{edge[0]} -> {edge[1]}\n")
# 
# # Usage example
# asm_file_path = r"D:\Downloads(D)\Testing\Windows.asm"
# parse_asm_file(asm_file_path)







# 
# import os
# import json
# import networkx as nx
# 
# def parse_asm_file(asm_file_path, json_file_path):
#     G = nx.DiGraph()
# 
#     with open(asm_file_path, "r", encoding="utf-8") as asm_file:
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 G.add_node(current_function, type="function", instructions=[], num_instructions=0)
#             elif current_function is not None and line.startswith("loc_"):
#                 instruction_address = line.split(":")[0].strip()
#                 opcode = line.split(":")[1].strip()
#                 G.add_node(instruction_address, type="instruction", address=instruction_address)
#                 G.add_edge(current_function, instruction_address)
#                 G.nodes[current_function]["instructions"].append(instruction_address)
#                 G.nodes[current_function]["num_instructions"] += 1
#             elif current_function is not None and ("jmp" in line or "call" in line):
#                 source_address = line.split(":")[0].strip()
#                 target_address = line.split()[-1].strip()
#                 G.add_edge(source_address, target_address)
# 
#     # Convert the graph to JSON format
#     graph_data = nx.node_link_data(G)
#     json_data = json.dumps(graph_data, indent=4)
# 
#     # Create the directory if it doesn't exist
#     os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
# 
#     # Save the JSON file
#     with open(json_file_path, "w") as json_file:
#         json_file.write(json_data)
# 
# # Usage example
# asm_file_path = "D:\Downloads(D)\Testing\Windows.asm"
# json_file_path = "D:\\Downloads\\Testing\\Windows1.json"
# parse_asm_file(asm_file_path, json_file_path)




#
# import pickle
# import networkx as nx
#
# def parse_asm_file(asm_file_path, pickle_file_path):
#     G = nx.DiGraph()
#
#     with open(asm_file_path, "r", encoding="utf-8") as asm_file:
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 G.add_node(current_function, type="function", instructions=[], num_instructions=0)
#             elif current_function is not None and line.startswith("loc_"):
#                 instruction_address = line.split(":")[0].strip()
#                 opcode = line.split(":")[1].strip()
#                 G.add_node(instruction_address, type="instruction", address=instruction_address)
#                 G.add_edge(current_function, instruction_address)
#                 G.nodes[current_function]["instructions"].append(instruction_address)
#                 G.nodes[current_function]["num_instructions"] += 1
#             elif current_function is not None and ("jmp" in line or "call" in line):
#                 source_address = line.split(":")[0].strip()
#                 target_address = line.split()[-1].strip()
#                 G.add_edge(source_address, target_address)
#
#     # Save the NetworkX graph as a pickle file
#     with open(pickle_file_path, "wb") as pickle_file:
#         pickle.dump(G, pickle_file)
#
# # Usage example
# asm_file_path = "D:\Downloads(D)\Testing\Windows.asm"
# pickle_file_path = "D:\\Downloads(D)\\Testing\\asm2graph.pickle"
# parse_asm_file(asm_file_path, pickle_file_path)

#
#
#
# import json
# import networkx as nx
# import pickle
#
# def generate_pickle(json_file_path, pickle_file_path):
#     # Load the JSON file
#     with open(json_file_path, "r") as json_file:
#         graph_data = json.load(json_file)
#
#     # Create a graph from the JSON data
#     G = nx.node_link_graph(graph_data)
#
#     # Check for node overlapping
#     is_planar, embedding = nx.check_planarity(G)
#     if is_planar:
#         print("No node overlapping detected. The graph is planar.")
#     else:
#         print("Node overlapping detected. The graph is not planar.")
#
#     # Save the graph as a pickle file
#     with open(pickle_file_path, "wb") as pickle_file:
#         pickle.dump(G, pickle_file)
#
# # Usage example
# json_file_path = "D:\\Downloads(D)\\Testing\\Windows.json"
# pickle_file_path = "D:\\Downloads(D)\\Testing\\asm2graph1.pickle"
# generate_pickle(json_file_path, pickle_file_path)

# 
# 
# 
# import json
# import networkx as nx
# import matplotlib.pyplot as plt
# import pickle
# 
# def generate_pickle(json_file_path, pickle_file_path):
#     with open(json_file_path, "r") as json_file:
#         data = json.load(json_file)
# 
#     nodes = data["nodes"]
#     edges = data["edges"]
# 
#     # Create a directed graph
#     G = nx.DiGraph()
# 
#     # Add nodes to the graph
#     for node in nodes:
#         name = node["name"]
#         G.add_node(name)
# 
#     # Add edges to the graph
#     for edge in edges:
#         source = edge["source"]
#         target = edge["target"]
#         G.add_edge(source, target)
# 
#     # Check for node overlapping
#     is_overlapping = any(count > 1 for count in G.in_degree().values())
# 
#     # Generate pickle file
#     with open(pickle_file_path, "wb") as pickle_file:
#         pickle.dump(G, pickle_file)
# 
#     # Print node overlapping status
#     if is_overlapping:
#         print("Node overlapping detected.")
#     else:
#         print("No node overlapping.")
# 
#     # Draw the graph
#     nx.draw(G, with_labels=True)
#     plt.show()
# 
# # Usage example
# json_file_path = "D:\\Downloads(D)\\Testing\\Windows1.json"
# pickle_file_path = "D:\\Downloads(D)\\Testing\\cfg.pickle"
# generate_pickle(json_file_path, pickle_file_path)








#
#
# import json
# import networkx as nx
# import matplotlib.pyplot as plt
#
# def generate_pickle(json_file_path, pickle_file_path):
#     # Load JSON data
#     with open(json_file_path, "r") as json_file:
#         cfg_data = json.load(json_file)
#
#     nodes = cfg_data.get("nodes", [])
#     edges = cfg_data.get("edges", [])
#
#     # Create a directed graph
#     G = nx.DiGraph()
#
#     # Add nodes to the graph
#     for node in nodes:
#         name = node.get("name", "")  # Use default value if "name" key is missing
#         G.add_node(name, **node)
#
#     # Add edges to the graph
#     for edge in edges:
#         G.add_edge(edge["source"], edge["target"])
#
#     # Check for node overlapping
#     overlapping_nodes = [node for node, degree in G.degree() if degree > 1]
#
#     if overlapping_nodes:
#         print("Node overlapping detected!")
#         print("Overlapping nodes:", overlapping_nodes)
#     else:
#         print("No node overlapping detected.")
#
#     # Save the graph as a pickle file
#     nx.write_gpickle(G, pickle_file_path)
#
#     # Plot the graph
#     nx.draw(G, with_labels=True)
#     plt.show()
#
# # Usage example
# json_file_path = "D:\\Downloads(D)\\Testing\\Windows1.json"
# pickle_file_path = "D:\\Downloads(D)\\Testing\\cfg.pkl"
# generate_pickle(json_file_path, pickle_file_path)
#
#
#

#
#
#
# import os
# import pickle
# import networkx as nx
#
# def parse_asm_file(asm_file_path, output_dir):
#     # Create output directory if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)
#
#     # Generate the pickle file path
#     asm_file_name = os.path.splitext(os.path.basename(asm_file_path))[0]
#     pickle_file_path = os.path.join(output_dir, asm_file_name + ".pickle")
#
#     G = nx.DiGraph()
#
#     with open(asm_file_path, "r", encoding="utf-8") as asm_file:
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 G.add_node(current_function, type="function", instructions=[], num_instructions=0)
#             elif current_function is not None and line.startswith("loc_"):
#                 instruction_address = line.split(":")[0].strip()
#                 opcode = line.split(":")[1].strip()
#                 G.add_node(instruction_address, type="instruction", address=instruction_address)
#                 G.add_edge(current_function, instruction_address)
#                 G.nodes[current_function]["instructions"].append(instruction_address)
#                 G.nodes[current_function]["num_instructions"] += 1
#             elif current_function is not None and ("jmp" in line or "call" in line):
#                 source_address = line.split(":")[0].strip()
#                 target_address = line.split()[-1].strip()
#                 G.add_edge(source_address, target_address)
#
#     # Save the NetworkX graph as a pickle file
#     with open(pickle_file_path, "wb") as pickle_file:
#         pickle.dump(G, pickle_file)
#
# def check_node_overlapping(pickle_file_path):
#     # Load the graph from the pickle file
#     with open(pickle_file_path, "rb") as pickle_file:
#         G = pickle.load(pickle_file)
#
#     # Check for node overlapping
#     is_planar, embedding = nx.check_planarity(G)
#     if is_planar:
#         print("No node overlapping detected. The graph is planar.")
#     else:
#         print("Node overlapping detected. The graph is not planar.")
#
# # Directory paths
# asm_directory = "D:\\Downloads(D)\\Testing\\asm_files"
# output_directory = "D:\\Downloads(D)\\Testing\\pickle_files"
#
# # Get all ASM files in the directory
# asm_files = [f for f in os.listdir(asm_directory) if f.endswith(".asm")]
#
# # Process each ASM file
# for asm_file in asm_files:
#     asm_file_path = os.path.join(asm_directory, asm_file)
#     parse_asm_file(asm_file_path, output_directory)
#
#     # Generate the corresponding pickle file path
#     asm_file_name = os.path.splitext(asm_file)[0]
#     pickle_file_path = os.path.join(output_directory, asm_file_name + ".pickle")
#
#     # Check for node overlapping
#     check_node_overlapping(pickle_file_path)






























# import os
# import pickle
# import networkx as nx
#
# def parse_asm_file(asm_file_path, output_dir):
#     # Create output directory if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)
#
#     # Generate the pickle file path
#     asm_file_name = os.path.splitext(os.path.basename(asm_file_path))[0]
#     pickle_file_path = os.path.join(output_dir, asm_file_name + ".pickle")
#
#     G = nx.DiGraph()
#
#     with open(asm_file_path, "r", encoding="utf-8") as asm_file:
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 G.add_node(current_function, type="function", instructions=[], num_instructions=0)
#             elif current_function is not None and line.startswith("loc_"):
#                 instruction_address = line.split(":")[0].strip()
#                 opcode = line.split(":")[1].strip()
#                 G.add_node(instruction_address, type="instruction", address=instruction_address)
#                 G.add_edge(current_function, instruction_address)
#                 G.nodes[current_function]["instructions"].append(instruction_address)
#                 G.nodes[current_function]["num_instructions"] += 1
#             elif current_function is not None and ("jmp" in line or "call" in line):
#                 source_address = line.split(":")[0].strip()
#                 target_address = line.split()[-1].strip()
#                 G.add_edge(source_address, target_address)
#
#     # Save the NetworkX graph as a pickle file
#     with open(pickle_file_path, "wb") as pickle_file:
#         pickle.dump(G, pickle_file)
#
# def check_node_overlapping(pickle_file_path):
#     # Load the graph from the pickle file
#     with open(pickle_file_path, "rb") as pickle_file:
#         G = pickle.load(pickle_file)
#
#     # Check for node overlapping
#     is_planar, embedding = nx.check_planarity(G)
#     if is_planar:
#         print("No node overlapping detected. The graph is planar.")
#     else:
#         print("Node overlapping detected. The graph is not planar.")
#
# # Directory paths
# asm_directory = "D:\\Downloads(D)\\Testing1\\asm_files"
# output_directory = "D:\\Downloads(D)\\Testing1\\pickle_files"
#
# # Check if the ASM directory exists
# if not os.path.isdir(asm_directory):
#     print(f"ASM directory '{asm_directory}' does not exist.")
#     exit()
#
# # Get all ASM files in the directory
# asm_files = [f for f in os.listdir(asm_directory) if f.endswith(".asm")]
#
# # Process each ASM file
# for asm_file in asm_files:
#     asm_file_path = os.path.join(asm_directory, asm_file)
#     parse_asm_file(asm_file_path, output_directory)
#
#     # Generate the corresponding pickle file path
#     asm_file_name = os.path.splitext(asm_file)[0]
#     pickle_file_path = os.path.join(output_directory, asm_file_name + ".pickle")
#
#     # Check for node overlapping
#     check_node_overlapping(pickle_file_path)

#
# import os
# import json
# import pickle
# from collections import defaultdict
#
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     # Create the pickle directory if it doesn't exist
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     # Iterate over the JSON files in the directory
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             # Load the JSON file
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             # Save the data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def check_node_overlapping(pickle_dir):
#     # Create a defaultdict to store the counts of each node
#     node_counts = defaultdict(int)
#
#     # Iterate over the pickle files in the directory
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             # Load the pickle file
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             # Count the number of occurrences of each node
#             for node in data['nodes']:
#                 node_counts[node] += 1
#
#     # Check if there are any nodes with overlapping occurrences
#     overlapping_nodes = [node for node, count in node_counts.items() if count > 1]
#
#     # Print the overlapping nodes
#     if overlapping_nodes:
#         print("Nodes with overlapping occurrences:")
#         for node in overlapping_nodes:
#             print(node)
#     else:
#         print("No overlapping nodes found.")
#
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Check for node overlapping in pickle files
# check_node_overlapping(pickle_dir)





#
# import os
# import json
# import pickle
# from collections import defaultdict
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def check_node_overlapping(pickle_dir):
#     node_counts = defaultdict(int)
#
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             for node in data['nodes']:
#                 # Convert the node dictionary to a tuple before using it as a key
#                 node_key = tuple(node.items())
#                 node_counts[node_key] += 1
#
#     overlapping_nodes = [node for node, count in node_counts.items() if count > 1]
#
#     if overlapping_nodes:
#         print("Nodes with overlapping occurrences:")
#         for node in overlapping_nodes:
#             print(dict(node))
#     else:
#         print("No overlapping nodes found.")
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Check for node overlapping in pickle files
# check_node_overlapping(pickle_dir)




#
# import os
# import json
# import pickle
# from collections import defaultdict
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def check_node_overlapping(pickle_dir):
#     node_counts = defaultdict(int)
#
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             for node in data['nodes']:
#                 # Convert the node list to a tuple before using it as a key
#                 node_key = tuple(node)
#                 node_counts[node_key] += 1
#
#     overlapping_nodes = [node for node, count in node_counts.items() if count > 1]
#
#     if overlapping_nodes:
#         print("Nodes with overlapping occurrences:")
#         for node in overlapping_nodes:
#             print(list(node))
#     else:
#         print("No overlapping nodes found.")
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Check for node overlapping in pickle files
# check_node_overlapping(pickle_dir)



#
# import os
# import json
# import pickle
# from collections import defaultdict
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def check_node_overlapping(pickle_dir):
#     node_counts = defaultdict(int)
#     unique_nodes = {}
#
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             for node in data['nodes']:
#                 if node not in unique_nodes:
#                     unique_nodes[node] = 1
#                 else:
#                     unique_nodes[node] += 1
#
#     overlapping_nodes = [node for node, count in unique_nodes.items() if count > 1]
#
#     if overlapping_nodes:
#         print("Nodes with overlapping occurrences:")
#         for node in overlapping_nodes:
#             unique_nodes[node] = unique_nodes[node]  # Assign a unique value to the overlapping node
#             print(node, "->", unique_nodes[node])
#     else:
#         print("No overlapping nodes found.")
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Check for node overlapping in pickle files and assign unique values to overlapping nodes
# check_node_overlapping(pickle_dir)
#









#
# import os
# import json
# import networkx as nx
#
#
# def convert_asm_to_json(asm_dir, json_dir):
#     # Create the JSON directory if it doesn't exist
#     os.makedirs(json_dir, exist_ok=True)
#
#     # Iterate over the ASM files in the directory
#     for filename in os.listdir(asm_dir):
#         if filename.endswith('.asm'):
#             asm_file_path = os.path.join(asm_dir, filename)
#             json_file_path = os.path.join(json_dir, filename[:-4] + '.json')
#
#             # Parse the ASM file and convert it to JSON
#             parse_asm_file(asm_file_path, json_file_path)
#
#     print("ASM to JSON conversion completed.")
#
#
# def parse_asm_file(asm_file_path, json_file_path):
#     G = nx.DiGraph()
#
#     with open(asm_file_path, "r", encoding="utf-8") as asm_file:
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 G.add_node(current_function, type="function", instructions=[], num_instructions=0)
#             elif current_function is not None and line.startswith("loc_"):
#                 instruction_address = line.split(":")[0].strip()
#                 opcode = line.split(":")[1].strip()
#                 G.add_node(instruction_address, type="instruction", address=instruction_address)
#                 G.add_edge(current_function, instruction_address)
#                 G.nodes[current_function]["instructions"].append(instruction_address)
#                 G.nodes[current_function]["num_instructions"] += 1
#             elif current_function is not None and ("jmp" in line or "call" in line):
#                 source_address = line.split(":")[0].strip()
#                 target_address = line.split()[-1].strip()
#                 G.add_edge(source_address, target_address)
#
#     # Convert the graph to JSON format
#     graph_data = nx.node_link_data(G)
#     json_data = json.dumps(graph_data, indent=4)
#
#     # Save the JSON file
#     with open(json_file_path, "w") as json_file:
#         json_file.write(json_data)
#
#
# # Specify the directory paths for ASM and JSON files
# asm_dir = 'D:\\Downloads(D)\\Testing1\\asm_files'
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
#
# # Convert ASM files to JSON files
# convert_asm_to_json(asm_dir, json_dir)
#




# import os
# import json
# import pickle
#
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     # Create the pickle directory if it doesn't exist
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     # Iterate over the JSON files in the directory
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             # Load the JSON file
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             # Remove unhashable types from the data
#             clean_data = remove_unhashable(data)
#
#             # Save the clean data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(clean_data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def remove_unhashable(data):
#     if isinstance(data, dict):
#         return {k: remove_unhashable(v) for k, v in data.items() if hashable(v)}
#     elif isinstance(data, list):
#         return [remove_unhashable(item) for item in data]
#     else:
#         return data
#
#
# def hashable(value):
#     try:
#         hash(value)
#         return True
#     except TypeError:
#         return False




#
#
# import os
# import json
# import pickle
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     # Create the pickle directory if it doesn't exist
#     if not os.path.exists(pickle_dir):
#         os.makedirs(pickle_dir)
#
#     # Iterate through the JSON files in the directory
#     for filename in os.listdir(json_dir):
#         if filename.endswith(".json"):
#             json_path = os.path.join(json_dir, filename)
#
#             # Load the JSON file
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             # Process the data as needed (e.g., check for node overlapping)
#             # ...
#
#             # Convert the data to pickle format
#             pickle_path = os.path.join(pickle_dir, os.path.splitext(filename)[0] + ".pickle")
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#             print(f"Converted {json_path} to {pickle_path}")
#
# def check_node_overlapping(pickle_dir):
#     # Iterate through the pickle files in the directory
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith(".pickle"):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             # Load the pickle file
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             # Check for node overlapping in the data
#             # ...
#
#             print(f"Checking node overlapping in {pickle_path}")
#             # Perform node overlapping check and print the result
#             if has_node_overlapping(data):
#                 print("Node overlapping detected!")
#             else:
#                 print("No node overlapping.")
#
# def has_node_overlapping(data):
#     # Perform the node overlapping check on the data
#     # Return True if node overlapping is detected, False otherwise
#     # ...
#
#     # Example implementation: Check if any two nodes have the same ID
#     node_ids = set()
#     for node in data['nodes']:
#         if node['id'] in node_ids:
#             return True
#         node_ids.add(node['id'])
#     return False
#
# # Specify the directories for JSON and pickle files
# json_directory = 'D:\Downloads(D)\Testing1\json_files'
# pickle_directory = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_directory, pickle_directory)
#
# # Check for node overlapping in pickle files
# check_node_overlapping(pickle_directory)
#







#
#
# import os
# import json
# import pickle
# from collections import defaultdict
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def check_node_overlapping(pickle_dir):
#     node_counts = defaultdict(int)
#     unique_nodes = {}
#
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             for node in data['nodes']:
#                 node_key = tuple(sorted(node.items()))
#                 if node_key not in unique_nodes:
#                     unique_nodes[node_key] = 1
#                 else:
#                     unique_nodes[node_key] += 1
#
#     overlapping_nodes = [node for node, count in unique_nodes.items() if count > 1]
#
#     if overlapping_nodes:
#         print("Nodes with overlapping occurrences:")
#         for node in overlapping_nodes:
#             unique_value = unique_nodes[node]
#             print(node, "-> Unique Value:", unique_value)
#     else:
#         print("No overlapping nodes found.")
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Check for node overlapping in pickle files and assign unique values to overlapping nodes
# check_node_overlapping(pickle_dir)







#
#
# import os
# import json
# import pickle
# from collections import defaultdict
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def check_node_overlapping(pickle_dir):
#     node_counts = defaultdict(int)
#     unique_nodes = {}
#
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             for node in data['nodes']:
#                 node_key = tuple(sorted(node.items()))
#                 if node_key not in unique_nodes:
#                     unique_nodes[node_key] = 1
#                 else:
#                     unique_nodes[node_key] += 1
#
#     overlapping_nodes = [node for node, count in unique_nodes.items() if count > 1]
#
#     if overlapping_nodes:
#         print("Nodes with overlapping occurrences:")
#         for node in overlapping_nodes:
#             unique_value = unique_nodes[node]
#             print(node, "-> Unique Value:", unique_value)
#     else:
#         print("No overlapping nodes found.")
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Check for node overlapping in pickle files and assign unique values to overlapping nodes
# check_node_overlapping(pickle_dir)







#
# import os
# import json
# import pickle
# from collections import defaultdict
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def check_node_overlapping(pickle_dir):
#     node_counts = defaultdict(int)
#     unique_nodes = {}
#
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             for node in data['nodes']:
#                 node_key = json.dumps(node, sort_keys=True)
#                 if node_key not in unique_nodes:
#                     unique_nodes[node_key] = 1
#                 else:
#                     unique_nodes[node_key] += 1
#
#     overlapping_nodes = [node for node, count in unique_nodes.items() if count > 1]
#
#     if overlapping_nodes:
#         print("Nodes with overlapping occurrences:")
#         for node in overlapping_nodes:
#             unique_value = unique_nodes[node]
#             print(node, "-> Unique Value:", unique_value)
#     else:
#         print("No overlapping nodes found.")
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Check for node overlapping in pickle files and assign unique values to overlapping nodes
# check_node_overlapping(pickle_dir)
# import os
# import json
# import pickle
# from collections import defaultdict
#
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     # Create the pickle directory if it doesn't exist
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     # Iterate over the JSON files in the directory
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             # Load the JSON file
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             # Save the data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def check_node_overlapping(pickle_dir):
#     node_counts = defaultdict(int)
#     overlapping_occurs = False
#
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             for node in data['nodes']:
#                 node_key = json.dumps(node, sort_keys=True)
#                 node_counts[node_key] += 1
#
#     overlapping_nodes = [node for node, count in node_counts.items() if count > 1]
#
#     if overlapping_nodes:
#         overlapping_occurs = True
#
#     if overlapping_occurs:
#         print("Overlapping nodes occur.")
#     else:
#         print("No overlapping nodes found.")
#
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Check for node overlapping in pickle files
# check_node_overlapping(pickle_dir)








# import os
# import json
# import pickle
# from collections import defaultdict
#
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     # Create the pickle directory if it doesn't exist
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     # Iterate over the JSON files in the directory
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             # Load the JSON file
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             # Save the data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def check_node_overlapping(pickle_dir):
#     node_counts = defaultdict(int)
#     overlapping_files = []
#
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             for node in data['nodes']:
#                 node_key = json.dumps(node, sort_keys=True)
#                 node_counts[node_key] += 1
#
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             overlapping_nodes = [node for node in data['nodes'] if node_counts[json.dumps(node, sort_keys=True)] > 1]
#
#             if overlapping_nodes:
#                 overlapping_files.append(filename)
#
#     if overlapping_files:
#         print("Node overlapping occurs in the following files:")
#         for filename in overlapping_files:
#             print(filename)
#     else:
#         print("No overlapping nodes found.")
#
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Check for node overlapping in pickle files
# check_node_overlapping(pickle_dir)









#
#
#
# import os
# import json
# import pickle
# from collections import defaultdict
#
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     # Create the pickle directory if it doesn't exist
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     # Iterate over the JSON files in the directory
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             # Load the JSON file
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             # Save the data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def handle_node_overlapping(pickle_dir):
#     # Create a defaultdict to store the counts of each node
#     node_counts = defaultdict(int)
#
#     # Iterate over the pickle files in the directory
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             # Load the pickle file
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             # Count the number of occurrences of each node
#             for node in data['nodes']:
#                 node_counts[str(node)] += 1
#
#     # Check if there are any nodes with overlapping occurrences
#     overlapping_nodes = [node for node, count in node_counts.items() if count > 1]
#
#     # Print the overlapping nodes
#     if overlapping_nodes:
#         print("Nodes with overlapping occurrences:")
#         for node in overlapping_nodes:
#             print(node)
#     else:
#         print("No overlapping nodes found.")
#
#     # Handle node overlapping by assigning unique values
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             # Load the pickle file
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             # Update the nodes with unique values
#             for i, node in enumerate(data['nodes']):
#                 data['nodes'][i] = str(node) + f"_{i+1}"
#
#             # Save the updated data as a new pickle file
#             new_pickle_path = os.path.join(pickle_dir, filename[:-7] + '_updated.pickle')
#             with open(new_pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("Node overlapping handled and updated pickle files created.")
#
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Handle node overlapping in pickle files
# handle_node_overlapping(pickle_dir)




# import os
# import json
# import pickle
# from collections import defaultdict
#
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     # Create the pickle directory if it doesn't exist
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     # Iterate over the JSON files in the directory
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             # Load the JSON file
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             # Save the data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def convert_nodes_to_hashable(nodes):
#     # Recursively convert nodes to a hashable format
#     if isinstance(nodes, list):
#         return tuple(convert_nodes_to_hashable(node) for node in nodes)
#     elif isinstance(nodes, dict):
#         return tuple((key, convert_nodes_to_hashable(value)) for key, value in nodes.items())
#     else:
#         return nodes
#
#
# def handle_node_overlapping(data):
#     nodes = data['nodes']
#     node_counts = defaultdict(int)
#
#     # Count the number of occurrences of each node
#     for node in nodes:
#         node_counts[node] += 1
#
#     # Check for overlapping nodes
#     overlapping_nodes = [node for node, count in node_counts.items() if count > 1]
#
#     # Assign unique values to the overlapping nodes
#     for node in overlapping_nodes:
#         count = node_counts[node]
#         for i in range(1, count + 1):
#             node['unique_id'] = f"{node['id']}-{i}"
#             nodes.append(node.copy())
#
#     # Remove the original overlapping nodes
#     data['nodes'] = [node for node in nodes if node not in overlapping_nodes]
#
#
# def check_node_overlapping(pickle_dir):
#     # Iterate over the pickle files in the directory
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             # Load the pickle file
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             # Convert the nodes to a hashable format
#             nodes = convert_nodes_to_hashable(data['nodes'])
#
#             # Update the data to handle overlapping nodes
#             handle_node_overlapping(data)
#
#             # Save the updated data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#             print(f"Handled node overlapping in file: {pickle_path}")
#
#     print("Node overlapping handling completed.")
#
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Handle node overlapping in pickle files
# check_node_overlapping(pickle_dir)




# JSON TO PICKLE
# import os
# import json
# import pickle
# from collections import defaultdict
#
#
# def convert_json_to_pickle(json_dir, pickle_dir):
#     # Create the pickle directory if it doesn't exist
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     # Iterate over the JSON files in the directory
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             # Load the JSON file
#             with open(json_path, 'r') as f:
#                 data = json.load(f)
#
#             # Save the data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def convert_nodes_to_hashable(nodes):
#     # Recursively convert nodes to a hashable format
#     if isinstance(nodes, list):
#         return tuple(convert_nodes_to_hashable(node) for node in nodes)
#     elif isinstance(nodes, dict):
#         return tuple((key, convert_nodes_to_hashable(value)) for key, value in nodes.items())
#     else:
#         return nodes
#
#
# def handle_node_overlapping(data):
#     nodes = convert_nodes_to_hashable(data['nodes'])
#     node_counts = defaultdict(int)
#
#     # Count the number of occurrences of each node
#     for node in nodes:
#         node_counts[node] += 1
#
#     # Check for overlapping nodes
#     overlapping_nodes = [node for node, count in node_counts.items() if count > 1]
#
#     # Assign unique values to the overlapping nodes
#     for node in overlapping_nodes:
#         count = node_counts[node]
#         for i in range(1, count + 1):
#             node_copy = node.copy()
#             node_copy['unique_id'] = f"{node['id']}-{i}"
#             nodes.append(node_copy)
#
#     # Remove the original overlapping nodes
#     data['nodes'] = [node for node in nodes if node not in overlapping_nodes]
#
#
# def check_node_overlapping(pickle_dir):
#     # Iterate over the pickle files in the directory
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             # Load the pickle file
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             # Update the data to handle overlapping nodes
#             handle_node_overlapping(data)
#
#             # Save the updated data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#             print(f"Handled node overlapping in file: {pickle_path}")
#
#     print("Node overlapping handling completed.")
#
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files
# convert_json_to_pickle(json_dir, pickle_dir)
#
# # Handle node overlapping in pickle files
# check_node_overlapping(pickle_dir)





# import networkx as nx
# import pickle
#
# def check_node_overlapping(pickle_file_path):
#     # Load the graph from the pickle file
#     with open(pickle_file_path, "rb") as pickle_file:
#         G = pickle.load(pickle_file)
#
#     # Check for node overlapping
#     is_planar, embedding = nx.check_planarity(G)
#     if is_planar:
#         print("No node overlapping detected. The graph is planar.")
#     else:
#         print("Node overlapping detected. The graph is not planar.")
#
# # Usage example
# pickle_file_path = "D:\\Downloads(D)\\Testing\\asm2graph.pickle"
# check_node_overlapping(pickle_file_path)

#
# import json
# import networkx as nx
# import pickle
#
# def generate_pickle(json_file_path, pickle_file_path):
#     # Load the JSON file
#     with open(json_file_path, "r") as json_file:
#         graph_data = json.load(json_file)
#
#     # Create a graph from the JSON data
#     G = nx.node_link_graph(graph_data)
#
#     # Check for node overlapping
#     is_planar, embedding = 
# #         print("Node overlapping detected. The graph is not planar.")
# #
# #     # Save the graph as a pickle file
# #     with open(pickle_file_path, "wb") as pickle_file:
# #         pickle.dump(G, pickle_file)nx.check_planarity(G)
#     if is_planar:
#         print("No node overlapping detected. The graph is planar.")
#     else:
#
# # Usage example
# json_file_path = "D:\\Downloads(D)\\Testing\\Windows.json"
# pickle_file_path = "D:\\Downloads(D)\\Testing\\asm2graph1.pickle"
# generate_pickle(json_file_path, pickle_file_path)



# import json
# import networkx as nx
# 
# def parse_asm_file(asm_file_path, json_file_path):
#     G = nx.DiGraph()
# 
#     with open(asm_file_path, "r", encoding="utf-8") as asm_file:
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 G.add_node(current_function, type="function", instructions=[], num_instructions=0)
#             elif current_function is not None and line.startswith("loc_"):
#                 instruction_address = line.split(":")[0].strip()
#                 opcode = line.split(":")[1].strip()
#                 G.add_node(instruction_address, type="instruction", address=instruction_address)
#                 G.add_edge(current_function, instruction_address)
#                 G.nodes[current_function]["instructions"].append(instruction_address)
#                 G.nodes[current_function]["num_instructions"] += 1
#             elif current_function is not None and ("jmp" in line or "call" in line):
#                 source_address = line.split(":")[0].strip()
#                 target_address = line.split()[-1].strip()
#                 G.add_edge(source_address, target_address)
# 
#     # Convert the graph to JSON format
#     graph_data = nx.node_link_data(G)
#     json_data = json.dumps(graph_data, indent=4)
# 
#     # Save the JSON file
#     with open(json_file_path, "w") as json_file:
#         json_file.write(json_data)
# 
# # Usage example
# asm_file_path = "D:\Downloads(D)\Testing\Windows.asm"
# json_file_path = "D:\\Downloads\\Testing\\asm2json.json"
# parse_asm_file(asm_file_path, json_file_path)




# ASM TO GSON GNNN
# import os
# import json
# import networkx as nx
#
# def convert_asm_to_json(asm_file_path, output_dir):
#     # Create output directory if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)
#
#     # Generate the JSON file path
#     asm_file_name = os.path.splitext(os.path.basename(asm_file_path))[0]
#     json_file_path = os.path.join(output_dir, asm_file_name + ".json")
#
#     G = nx.DiGraph()
#
#     with open(asm_file_path, "r", encoding="utf-8") as asm_file:
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 G.add_node(current_function, type="function", instructions=[], num_instructions=0)
#             elif current_function is not None and line.startswith("loc_"):
#                 instruction_address = line.split(":")[0].strip()
#                 opcode = line.split(":")[1].strip()
#                 G.add_node(instruction_address, type="instruction", address=instruction_address)
#                 G.add_edge(current_function, instruction_address)
#                 G.nodes[current_function]["instructions"].append(instruction_address)
#                 G.nodes[current_function]["num_instructions"] += 1
#             elif current_function is not None and ("jmp" in line or "call" in line):
#                 source_address = line.split(":")[0].strip()
#                 target_address = line.split()[-1].strip()
#                 G.add_edge(source_address, target_address)
#
#     # Convert NetworkX graph to JSON format
#     data = nx.node_link_data(G)
#
#     # Save the graph data as a JSON file
#     with open(json_file_path, "w") as json_file:
#         json.dump(data, json_file)
#
# # Directory paths
# asm_directory = "D:\\Downloads(D)\\Testing1\\asm_files"
# output_directory = "D:\\Downloads(D)\\Testing1\\json_files_GNN"
#
# # Get all ASM files in the directory
# asm_files = [f for f in os.listdir(asm_directory) if f.endswith(".asm")]
#
# # Process each ASM file
# for asm_file in asm_files:
#     asm_file_path = os.path.join(asm_directory, asm_file)
#     convert_asm_to_json(asm_file_path, output_directory)



#
# import os
# import pickle
# import networkx as nx
#
# def convert_asm_to_pickle(asm_file_path, output_dir):
#     # Create output directory if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)
#
#     # Generate the pickle file path
#     asm_file_name = os.path.splitext(os.path.basename(asm_file_path))[0]
#     pickle_file_path = os.path.join(output_dir, asm_file_name + ".pickle")
#
#     G = nx.DiGraph()
#
#     with open(asm_file_path, "r", encoding="utf-8") as asm_file:
#         current_function = None
#         for line in asm_file:
#             line = line.strip()
#             if line.startswith("sub_"):
#                 current_function = line.split()[0].strip()
#                 G.add_node(current_function, type="function", instructions=[], num_instructions=0)
#             elif current_function is not None and line.startswith("loc_"):
#                 instruction_address = line.split(":")[0].strip()
#                 opcode = line.split(":")[1].strip()
#                 G.add_node(instruction_address, type="instruction", address=instruction_address)
#                 G.add_edge(current_function, instruction_address)
#                 G.nodes[current_function]["instructions"].append(instruction_address)
#                 G.nodes[current_function]["num_instructions"] += 1
#             elif current_function is not None and ("jmp" in line or "call" in line):
#                 source_address = line.split(":")[0].strip()
#                 target_address = line.split()[-1].strip()
#                 G.add_edge(source_address, target_address)
#
#     # Save the NetworkX graph as a pickle file with necessary attributes
#     graph_data = {
#         "graph": G,
#         "node_features": nx.get_node_attributes(G, "type"),
#         "edge_indices": list(G.edges()),
#         "labels": nx.get_node_attributes(G, "type")
#     }
#
#     with open(pickle_file_path, "wb") as pickle_file:
#         pickle.dump(graph_data, pickle_file)
#
# # Directory paths
# asm_directory = "D:\\Downloads(D)\\Testing1\\asm_files"
# output_directory = "D:\\Downloads(D)\\Testing1\\pickle_files_GNN"
#
# # Get all ASM files in the directory
# asm_files = [f for f in os.listdir(asm_directory) if f.endswith(".asm")]
#
# # Process each ASM file
# for asm_file in asm_files:
#     asm_file_path = os.path.join(asm_directory, asm_file)
#     convert_asm_to_pickle(asm_file_path, output_directory)






























# import os
# import json
# import pickle
#
#
# def convert_json_to_pickle(json_dir, pickle_dir, encoding='utf-8'):
#     # Create the pickle directory if it doesn't exist
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     # Iterate over the JSON files in the directory
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             # Load the JSON file
#             with open(json_path, 'r', encoding=encoding) as f:
#                 data = json.load(f)
#
#             # Save the data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\\Downloads(D)\\Testing1\\json_files'
# pickle_dir = 'D:\\Downloads(D)\Testing1\\pickle_files_json_utf8'
#
# # Convert JSON files to pickle files using UTF-8 encoding
# convert_json_to_pickle(json_dir, pickle_dir, encoding='utf-8')








# import os
# import json
# import pickle
# from collections import defaultdict
#
#
# def convert_json_to_pickle(json_dir, pickle_dir, encoding='utf-8'):
#     # Create the pickle directory if it doesn't exist
#     os.makedirs(pickle_dir, exist_ok=True)
#
#     # Iterate over the JSON files in the directory
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             json_path = os.path.join(json_dir, filename)
#             pickle_path = os.path.join(pickle_dir, filename[:-5] + '.pickle')
#
#             # Load the JSON file
#             with open(json_path, 'r', encoding=encoding) as f:
#                 data = json.load(f)
#
#             # Save the data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#     print("JSON to pickle conversion completed.")
#
#
# def handle_node_overlapping(data):
#     nodes = data['nodes']
#     node_counts = defaultdict(int)
#
#     # Count the number of occurrences of each node
#     for node in nodes:
#         node_counts[tuple(sorted(node.items()))] += 1
#
#     # Check for overlapping nodes
#     overlapping_nodes = [node for node, count in node_counts.items() if count > 1]
#
#     # Assign unique values to the overlapping nodes
#     for node in overlapping_nodes:
#         count = node_counts[node]
#         for i in range(1, count + 1):
#             node_copy = dict(node)
#             node_copy['unique_id'] = f"{node['id']}-{i}"
#             nodes.append(node_copy)
#
#     # Remove the original overlapping nodes
#     data['nodes'] = [node for node in nodes if tuple(sorted(node.items())) not in overlapping_nodes]
#
#
# def check_node_overlapping(pickle_dir):
#     # Iterate over the pickle files in the directory
#     for filename in os.listdir(pickle_dir):
#         if filename.endswith('.pickle'):
#             pickle_path = os.path.join(pickle_dir, filename)
#
#             # Load the pickle file
#             with open(pickle_path, 'rb') as f:
#                 data = pickle.load(f)
#
#             # Update the data to handle overlapping nodes
#             handle_node_overlapping(data)
#
#             # Save the updated data as a pickle file
#             with open(pickle_path, 'wb') as f:
#                 pickle.dump(data, f)
#
#             print(f"Handled node overlapping in file: {pickle_path}")
#
#     print("Node overlapping handling completed.")
#
#
# # Specify the directory paths for JSON and pickle files
# json_dir = 'D:\Downloads(D)\Testing1\json_files'
# pickle_dir = 'D:\Downloads(D)\Testing1\pickle_files_json'
#
# # Convert JSON files to pickle files using UTF-8 encoding
# convert_json_to_pickle(json_dir, pickle_dir, encoding='utf-8')
#
# # Handle node overlapping in pickle files
# check_node_overlapping(pickle_dir)















# import pickle
#
# def check_utf8_encoding(pickle_file):
#     try:
#         with open(pickle_file, 'rb') as f:
#             pickle_data = pickle.load(f, encoding='utf-8')
#         print(f"The pickle file '{pickle_file}' is UTF-8 encoded.")
#     except UnicodeDecodeError:
#         print(f"The pickle file '{pickle_file}' is not UTF-8 encoded.")
#
# # Usage example
# pickle_file = "D:\\Downloads(D)\\Testing1\\pickle_files_json\\d40e907c1bdfc0458f709c0e72d54752.pickle"
# check_utf8_encoding(pickle_file)
#
# import re
# import json
# import os
#
# def asm_to_json(asm_file):
#     with open(asm_file, 'r', encoding='utf-8', errors='ignore') as f:
#         asm_data = f.read()
#
#     # Initialize variables to store the extracted information
#     edges = []
#     nodes = []
#     labels = []
#
#     # Regular expressions to match the relevant lines in the assembly code
#     label_regex = r'^([a-zA-Z_][a-zA-Z0-9_]*:)'
#     edge_regex = r'^\s+(\w+)\s+(\w+),?\s*(\w+)?'
#     node_regex = r'^(\w+)\s+(segment|ends)'
#
#     # Process each line of the assembly code
#     for line in asm_data.split('\n'):
#         line = line.strip()
#
#         # Check if the line matches a label definition
#         label_match = re.match(label_regex, line)
#         if label_match:
#             label = label_match.group(1)
#             labels.append(label)
#
#         # Check if the line matches an edge definition
#         edge_match = re.match(edge_regex, line)
#         if edge_match:
#             source = edge_match.group(2)
#             destination = edge_match.group(3)
#             edges.append({'source': source, 'destination': destination})
#
#         # Check if the line matches a node definition
#         node_match = re.match(node_regex, line)
#         if node_match:
#             node = node_match.group(1)
#             nodes.append(node)
#
#     # Create a dictionary to store the extracted information
#     asm_dict = {
#         'edges': edges,
#         'nodes': nodes,
#         'labels': labels
#     }
#
#     # Generate the JSON file path based on the ASM file path
#     json_file = os.path.splitext(asm_file)[0] + '.json'
#
#     # Save the dictionary to a JSON file
#     with open(json_file, 'w') as f:
#         json.dump(asm_dict, f, indent=4)
#
#     return
#
# # Usage example
# asm_file = "D:\\Downloads(D)\\Testing1\\TestASMJSON\\26fae9900410053ddc14abdbdf90f856.asm"
# asm_to_json(asm_file)
# print("JSON data saved.")




#
#
#
# import json
#
# def parse_asm_to_json(asm_file):
#     # Read the ASM file
#     with open(asm_file, 'r', encoding='utf-8') as file:
#         asm_code = file.read()
#
#     # Split the assembly code into lines
#     lines = asm_code.split('\n')
#
#     # Initialize variables
#     edges = []
#     nodes = []
#     label = None
#
#     for line in lines:
#         line = line.strip()
#
#         # Check for label keywords to assign the label
#         if 'benign' in line:
#             label = 'benign'
#         elif 'malicious' in line:
#             label = 'malicious'
#
#         # Extract edges from the assembly code
#         if 'jmp' in line or 'call' in line:
#             parts = line.split()
#             if len(parts) >= 2:
#                 source = parts[0]
#                 target = parts[1]
#                 edges.append({'source': source, 'target': target})
#
#         # Extract nodes from the assembly code
#         if 'proc' in line or 'segment' in line or 'endp' in line:
#             parts = line.split()
#             if len(parts) >= 2:
#                 node = parts[1]
#                 nodes.append(node)
#
#     # Create the JSON object
#     json_data = {
#         'edges': edges,
#         'nodes': nodes,
#         'label': label
#     }
#
#     # Write JSON data to a file
#     json_file = asm_file + '.json'
#     with open(json_file, 'w') as file:
#         json.dump(json_data, file, indent=4)
#
#     return json_file
#
# # Example usage
# asm_file = "D:\\Downloads(D)\\Testing1\\TestASMJSON\\26fae9900410053ddc14abdbdf90f856.asm"
# json_file = parse_asm_to_json(asm_file)
# print(f'JSON file created: {json_file}')









#
#
# import re
#
# def parse_asm_to_json(asm_file):
#     with open(asm_file, 'r', encoding='utf-8') as f:
#         asm_code = f.read()
#
#     lines = asm_code.split('\n')
#     nodes = []
#     edges = []
#     label = None
#
#     # Regex patterns to match nodes and edges
#     node_pattern = r'^([a-zA-Z0-9_]+)\s+.*$'
#     edge_pattern = r'^\s*.*call\s+([a-zA-Z0-9_]+)\s+.*$'
#
#     node_id = 1  # Unique ID counter for nodes
#
#     for line in lines:
#         # Check if line matches node pattern
#         node_match = re.match(node_pattern, line)
#         if node_match:
#             node_name = node_match.group(1)
#             node = {'id': str(node_id), 'name': node_name}
#             nodes.append(node)
#             node_id += 1
#
#         # Check if line matches edge pattern
#         edge_match = re.match(edge_pattern, line.strip())
#         if edge_match:
#             source_node = edge_match.group(1)
#             target_node = edge_match.group(2)  # Extract target node
#             edge = {'source': source_node, 'target': target_node}
#             edges.append(edge)
#
#     # Create JSON object with nodes and edges
#     data = {'nodes': nodes, 'edges': edges}
#
#     # Extract label from file address
#     if 'benign' in asm_file:
#         label = 'benign'
#     elif 'malware' in asm_file:
#         label = 'malware'
#
#     # Add label to JSON data
#     data['label'] = label
#
#     # Convert data to JSON string
#     json_data = '{\n'
#     json_data += '  "nodes": [\n'
#     for i, node in enumerate(data['nodes']):
#         json_data += f'    {{"id": "{node["id"]}", "name": "{node["name"]}"}}'
#         if i < len(data['nodes']) - 1:
#             json_data += ','
#         json_data += '\n'
#     json_data += '  ],\n'
#
#     json_data += '  "edges": [\n'
#     for i, edge in enumerate(data['edges']):
#         json_data += f'    {{"source": "{edge["source"]}", "target": "{edge["target"]}"}}'
#         if i < len(data['edges']) - 1:
#             json_data += ','
#         json_data += '\n'
#     json_data += '  ],\n'
#
#     json_data += f'  "label": "{data["label"]}"\n'
#     json_data += '}\n'
#
#     return json_data
#
# # Input and output file paths
# input_asm_file = 'D:\\Downloads(D)\\Testing1\\TestASMJSON\\26fae9900410053ddc14abdbdf90f856.asm'
# output_json_file = 'D:\\Downloads(D)\\Testing1\\TestASMJSON\\26fae9900410053ddc14abdbdf90f856.asm.json'
#
# # Parse ASM to JSON
# json_data = parse_asm_to_json(input_asm_file)
#
# # Write JSON data to output file
# with open(output_json_file, 'w') as f:
#     f.write(json_data)
#
# print(f"Successfully converted {input_asm_file} to {output_json_file}.")
#
#
#
#
#
#
#
#
#
#
#
#










# import re
# def parse_asm_to_json(asm_file):
#     with open(asm_file, 'r', encoding='utf-8') as f:
#         asm_code = f.read()
#
#     lines = asm_code.split('\n')
#     nodes = []
#     edges = []
#     label = None
#
#     # Regex patterns to match nodes and edges
#     node_pattern = r'^([a-zA-Z0-9_]+)\s+.*$'
#     edge_pattern = r'^\s*.*call\s+([a-zA-Z0-9_]+)\s+.*$'
#
#     node_id = 1  # Unique ID counter for nodes
#
#     for line in lines:
#         # Check if line matches node pattern
#         node_match = re.match(node_pattern, line)
#         if node_match:
#             node_name = node_match.group(1)
#             node = {'id': str(node_id), 'name': node_name}
#             nodes.append(node)
#             node_id += 1
#
#         # Check if line matches edge pattern
#         edge_match = re.match(edge_pattern, line)
#         if edge_match:
#             source_node = edge_match.group(1)
#
#             # Find the target node using label or function call
#             target_node = None
#             for i, next_line in enumerate(lines):
#                 # Check if next line contains a label
#                 label_match = re.match(r'^([a-zA-Z0-9_]+):', next_line)
#                 if label_match and label_match.group(1) == source_node:
#                     target_node = lines[i + 1].split(':')[0].strip()
#                     break
#
#                 # Check if next line contains a function call
#                 function_match = re.match(r'^\s*call\s+([a-zA-Z0-9_]+)\s+.*$', next_line)
#                 if function_match and function_match.group(1) == source_node:
#                     target_node = lines[i + 1].split(':')[0].strip()
#                     break
#
#             if target_node:
#                 edge = {'source': source_node, 'target': target_node}
#                 edges.append(edge)
#
#     # Create JSON object with nodes and edges
#     data = {'nodes': nodes, 'edges': edges}
#
#     # Extract label from file address
#     if 'benign' in asm_file:
#         label = 'benign'
#     elif 'malware' in asm_file:
#         label = 'malware'
#
#     # Add label to JSON data
#     data['label'] = label
#
#     # Convert data to JSON string
#     json_data = '{\n'
#     json_data += '  "nodes": [\n'
#     for i, node in enumerate(data['nodes']):
#         json_data += f'    {{"id": "{node["id"]}", "name": "{node["name"]}"}}'
#         if i < len(data['nodes']) - 1:
#             json_data += ','
#         json_data += '\n'
#     json_data += '  ],\n'
#
#     json_data += '  "edges": [\n'
#     for i, edge in enumerate(data['edges']):
#         json_data += f'    {{"source": "{edge["source"]}", "target": "{edge["target"]}"}}'
#         if i < len(data['edges']) - 1:
#             json_data += ','
#         json_data += '\n'
#     json_data += '  ],\n'
#
#     json_data += f'  "label": "{data["label"]}"\n'
#     json_data += '}\n'
#
#     return json_data
#
# # Input and output file paths
# input_asm_file = 'D:\\Downloads(D)\\Testing1\\TestASMJSON\\26fae9900410053ddc14abdbdf90f856.asm'
# output_json_file = 'D:\\Downloads(D)\\Testing1\\TestASMJSON\\26fae9900410053ddc14abdbdf90f856.asm.json'
#
# # Parse ASM to JSON
# json_data = parse_asm_to_json(input_asm_file)
#
# # Write JSON data to output file
# with open(output_json_file, 'w') as f:
#     f.write(json_data)
#
# print(f"Successfully converted {input_asm_file} to {output_json_file}.")








# import re
# import json
#
# def parse_asm_to_json(asm_file):
#     with open(asm_file, 'r', encoding='utf-8') as f:
#         asm_code = f.read()
#
#     # Process ASM code
#     json_output = parse_asm(asm_code)
#
#     # Save output as JSON file
#     output_file = asm_file + '.json'
#     with open(output_file, 'w') as file:
#         file.write(json_output)
#
#     print("JSON output saved as:", output_file)
#
#
# def parse_asm(asm_code):
#     # Initialize data structures
#     node_dict = {}
#     edges = []
#
#     # Regular expressions for pattern matching
#     node_pattern = r"([a-zA-Z_]+\d+)\s+proc\s+near"
#     call_pattern = r"call\s+(\w+)"
#     jmp_pattern = r"jmp\s+(\w+)"
#     data_xref_pattern = r"DATA\s+XREF:\s+(\w+)"
#     code_xref_pattern = r"CODE\s+XREF:\s+(\w+)"
#
#     # Find all nodes and their addresses
#     nodes = re.findall(node_pattern, asm_code)
#     for node in nodes:
#         node_id = len(node_dict) + 1  # Generate unique node ID
#         node_dict[node_id] = {"node_name": node}
#
#     # Find edges between nodes
#     for match in re.finditer(call_pattern, asm_code):
#         source_node = match.group(1)
#         target_node = None
#
#         # Check if call target is a known node
#         for node_id, node_data in node_dict.items():
#             if node_data["node_name"] == source_node:
#                 source_node_id = node_id
#
#         # Find the address referenced by the call instruction
#         call_addr = match.start() + match.group().index(match.group(1))
#         target_match = re.search(data_xref_pattern, asm_code[call_addr:])
#         if target_match:
#             target_node = target_match.group(1)
#
#         if target_node:
#             # Check if target node is a known node
#             for node_id, node_data in node_dict.items():
#                 if node_data["node_name"] == target_node:
#                     target_node_id = node_id
#
#             # Add edge between source and target nodes
#             edges.append((source_node_id, target_node_id))
#
#     for match in re.finditer(jmp_pattern, asm_code):
#         source_node = match.group(1)
#         target_node = None
#
#         # Check if jmp target is a known node
#         for node_id, node_data in node_dict.items():
#             if node_data["node_name"] == source_node:
#                 source_node_id = node_id
#
#         # Find the address referenced by the jmp instruction
#         jmp_addr = match.start() + match.group().index(match.group(1))
#         target_match = re.search(code_xref_pattern, asm_code[jmp_addr:])
#         if target_match:
#             target_node = target_match.group(1)
#
#         if target_node:
#             # Check if target node is a known node
#             for node_id, node_data in node_dict.items():
#                 if node_data["node_name"] == target_node:
#                     target_node_id = node_id
#
#             # Add edge between source and target nodes
#             edges.append((source_node_id, target_node_id))
#
#     # Assign labels based on ASM file type
#     file_type = "benign" if asm_code.startswith("beingn") else "malicious"
#
#     # Create JSON object
#     json_data = {
#         "node_dict": node_dict,
#         "edges": edges,
#         "label": file_type
#     }
#
#     # Convert JSON object to string
#     json_str = json.dumps(json_data, indent=4)
#     return json_str
#
#
# # Example usage
# asm_file = 'D:\\Downloads(D)\\Testing1\\TestASMJSON\\26fae9900410053ddc14abdbdf90f856.asm'
# parse_asm_file(asm_file)













#
# import re
# import json
# import os
#
# def parse_asm(asm_code):
#     # Initialize data structures
#     node_dict = {}
#     edges = []
#
#     # Regular expressions for pattern matching
#     node_pattern = r"([a-zA-Z_]+\d+)\s+proc\s+near"
#     call_pattern = r"call\s+(\w+)"
#     jmp_pattern = r"jmp\s+(\w+)"
#     data_xref_pattern = r"DATA\s+XREF:\s+(\w+)"
#     code_xref_pattern = r"CODE\s+XREF:\s+(\w+)"
#
#     # Find all nodes and their addresses
#     nodes = re.findall(node_pattern, asm_code)
#     for node in nodes:
#         node_dict[node] = {"node_name": node}
#
#     # Find edges between nodes
#     for match in re.finditer(call_pattern, asm_code):
#         source_node = match.group(1)
#         target_node = None
#
#         # Check if call target is a known node
#         if source_node in node_dict:
#             # Find the address referenced by the call instruction
#             call_addr = match.start() + match.group().index(match.group(1))
#             target_match = re.search(data_xref_pattern, asm_code[call_addr:])
#             if target_match:
#                 target_node = target_match.group(1)
#
#         if target_node:
#             # Add edge between source and target nodes
#             edges.append((source_node, target_node))
#
#     for match in re.finditer(jmp_pattern, asm_code):
#         source_node = match.group(1)
#         target_node = None
#
#         # Check if jmp target is a known node
#         if source_node in node_dict:
#             # Find the address referenced by the jmp instruction
#             jmp_addr = match.start() + match.group().index(match.group(1))
#             target_match = re.search(code_xref_pattern, asm_code[jmp_addr:])
#             if target_match:
#                 target_node = target_match.group(1)
#
#         if target_node:
#             # Add edge between source and target nodes
#             edges.append((source_node, target_node))
#
#     # Create JSON object
#     json_data = {
#         "node_dict": node_dict,
#         "edges": edges
#     }
#
#     return json_data
#
# # Example usage
# asm_file = 'D:\\Downloads(D)\\Testing1\\TestASMJSON\\26fae9900410053ddc14abdbdf90f856.asm'  # Replace with the path to your ASM file
#
# # Read the ASM code from file
# with open(asm_file, 'r', encoding='utf-8') as f:
#     asm_code = f.read()
#
# # Parse the ASM code and get the JSON data
# json_data = parse_asm(asm_code)
#
# # Create the output directory if it doesn't exist
# output_dir = 'output'
# os.makedirs(output_dir, exist_ok=True)
#
# # Generate the JSON file path
# json_file = os.path.join(output_dir, 'output.json')
#
# # Save the JSON data to file
# with open(json_file, 'w') as file:
#     json.dump(json_data, file, indent=4)
#
# print(f"JSON file saved at: {json_file}")

#
# import json
#
#
# def parse_asm_to_cfg(asm_file_path):
#     # Step 1: Read the assembly file and extract instructions
#     with open(asm_file_path, 'r', encoding='utf-8') as asm_file:
#         asm_lines = asm_file.readlines()
#
#     # Step 2: Parse instructions and extract relevant information
#     node_list = {}
#     edge_list = []
#     current_node = None
#
#     for line in asm_lines:
#         line = line.strip()
#
#         if line.startswith("/*") and line.endswith("*/"):
#             # This line contains node information
#             node_data = json.loads(line[2:-2])
#             node_list[node_data['node_address']] = node_data
#             current_node = node_data['node_address']
#         elif line.startswith("[") and line.endswith("]"):
#             # This line contains edge information
#             edge_data = json.loads(line[1:-1])
#             edge_list.append(edge_data)
#         elif line.startswith("[[") and line.endswith("]]"):
#             # This line contains instruction information
#             instruction_data = json.loads(line[2:-2])
#             node_list[current_node]['insns'] = instruction_data
#
#     # Step 3: Build the control flow graph (CFG)
#     cfg_data = {
#         "node_list": node_list,
#         "edge_list": edge_list,
#         "label": "malware",
#         "startpoint": None,
#         "endpoints": []
#     }
#
#     # Set the startpoint and endpoints
#     cfg_data['startpoint'] = edge_list[0][0]
#     cfg_data['endpoints'] = [edge[1] for edge in edge_list if edge[1] not in node_list]
#
#     return cfg_data
#
#
# def write_cfg_to_json(cfg_data, json_file_path):
#     with open(json_file_path, 'w') as json_file:
#         json.dump(cfg_data, json_file, indent=2)
#
#
# # Usage example
# asm_file_path = "D:\\Downloads(D)\\Testing1\\TestASMJSON\\26fae9900410053ddc14abdbdf90f856.asm"
# json_file_path = "D:\\Downloads(D)\\Testing1\\TestASMJSON\\26fae9900410053ddc14abdbdf90f856.asm.json"
#
# cfg_data = parse_asm_to_cfg(asm_file_path)
# write_cfg_to_json(cfg_data, json_file_path)










# import json
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_list": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Open the binary file
# with open("binary.exe", "rb") as f:
#     # Read the binary contents
#     binary = f.read()
#
#     # Disassemble the binary code
#     instructions = md.disasm(binary, 0)
#
#     # Process each instruction
#     for insn in instructions:
#         address = insn.address
#         mnemonic = insn.mnemonic
#         operands = insn.op_str
#
#         # Add the instruction to the node list
#         data["node_list"][address] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": "",
#             "insns": [[address, mnemonic, operands]]
#         }
#
#         # Add an edge to the previous instruction
#         if address > 0:
#             data["edge_list"].append([address - 4, address])
#
# # Write the JSON output to a file
# with open("output.json", "w") as f:
#     json.dump(data, f, indent=4)



# import json
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_list": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Prompt for the binary path
# binary_path = input("Enter the path to the binary file: ")
#
# # Open the binary file
# with open(binary_path, "rb") as f:
#     # Read the binary contents
#     binary = f.read()
#
#     # Disassemble the binary code
#     instructions = md.disasm(binary, 0)
#
#     # Process each instruction
#     for insn in instructions:
#         address = insn.address
#         mnemonic = insn.mnemonic
#         operands = insn.op_str
#
#         # Add the instruction to the node list
#         data["node_list"][address] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": "",
#             "insns": [[address, mnemonic, operands]]
#         }
#
#         # Add an edge to the previous instruction
#         if address > 0:
#             data["edge_list"].append([address - 4, address])
#
# # Write the JSON output to a file
# output_path = "output.json"
# with open(output_path, "w") as f:
#     json.dump(data, f, indent=4)
#
# print(f"JSON output generated: {output_path}")














# import json
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Prompt for the binary path
# binary_path = input("Enter the path to the binary file: ")
#
# # Open the binary file
# with open(binary_path, "rb") as f:
#     # Read the binary contents
#     binary = f.read()
#
#     # Disassemble the binary code
#     instructions = md.disasm(binary, 0)
#
#     # Process each instruction
#     for insn in instructions:
#         address = insn.address
#         mnemonic = insn.mnemonic
#         operands = insn.op_str
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(insn.size)
#         data["node_dict"][address] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, operands]]
#         }
#
#         # Add an edge to the previous instruction
#         if address > 0:
#             if address - 4 in data["node_dict"]:
#                 data["edge_list"].append([address - 4, address])
#
#     # Set the endpoint as the last instruction address
#     endpoint = address
#     data["endpoints"].append(endpoint)
#
# # Write the JSON output to a file
# output_path = "output1.json"
# with open(output_path, "w") as f:
#     json.dump(data, f, indent=4)
#
# print(f"JSON output generated: {output_path}")
























#
# import json
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Prompt for the binary path
# binary_path = input("Enter the path to the binary file: ")
#
# # Open the binary file
# with open(binary_path, "rb") as f:
#     # Read the binary contents
#     binary = f.read()
#
#     # Disassemble the binary code
#     instructions = md.disasm(binary, 0)
#
#     # Track the lowest negative address
#     lowest_negative_address = float("inf")
#
#     # Process each instruction
#     for insn in instructions:
#         address = insn.address
#         mnemonic = insn.mnemonic
#         operands = insn.op_str
#
#         # Check if the address is negative
#         if address < 0 and address < lowest_negative_address:
#             lowest_negative_address = address
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(insn.size)
#         data["node_dict"][address] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, operands]]
#         }
#
#         # Add an edge to the previous instruction
#         if address > 0:
#             prev_address = address - 4
#             data["edge_list"].append([prev_address, address])
#
#     # Adjust the addresses in the edge list
#     offset = abs(lowest_negative_address) if lowest_negative_address < 0 else 0
#     data["edge_list"] = [[src + offset, dest + offset] for src, dest in data["edge_list"]]
#
#     # Set the endpoint as the last instruction address
#     endpoint = address + offset
#     data["endpoints"].append(endpoint)
#
# # Write the JSON output to a file
# output_path = "output2.json"
# with open(output_path, "w") as f:
#     json.dump(data, f, indent=4)
#
# print(f"JSON output generated: {output_path}")















# import json
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Prompt for the binary path
# binary_path = input("Enter the path to the binary file: ")
#
# # Open the binary file
# with open(binary_path, "rb") as f:
#     # Read the binary contents
#     binary = f.read()
#
#     # Disassemble the binary code
#     instructions = md.disasm(binary, 0)
#
#     # Track the node index and the current instruction address
#     node_index = 0
#     current_address = None
#
#     # Process each instruction
#     for insn in instructions:
#         address = insn.address
#         mnemonic = insn.mnemonic
#         operands = insn.op_str
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(insn.size)
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, operands]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
# # Write the JSON output to a file
# output_path = "output3.json"
# with open(output_path, "w") as f:
#     json.dump(data, f, indent=4)
#
# print(f"JSON output generated: {output_path}")






















#
# import json
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32
# import lief
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Prompt for the binary path
# binary_path = input("Enter the path to the binary file: ")
#
# # Disassemble the binary and convert it to ASM
# binary = lief.parse(binary_path)
# asm = binary.disasm
#
# # Track the node index and the current instruction address
# node_index = 0
# current_address = None
#
# # Process each instruction
# for insn in asm:
#     address = insn.address
#     mnemonic = insn.mnemonic
#     operands = ', '.join(str(op) for op in insn.operands)
#
#     # Add the instruction to the node_dict with the node label
#     node_label = str(insn.size)
#     data["node_dict"][node_index] = {
#         "node_name": f"main+0x{address:02x}",
#         "node_label": node_label,
#         "insns": [[address, mnemonic, operands]]
#     }
#
#     # Add an edge to the previous instruction
#     if current_address is not None:
#         data["edge_list"].append((current_address, node_index))
#
#     # Update the current instruction address and increment the node index
#     current_address = node_index
#     node_index += 1
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
# # Write the JSON output to a file
# output_path = "output4.json"
# with open(output_path, "w") as f:
#     json.dump(data, f, indent=4)
#
# print(f"JSON output generated: {output_path}")









# import subprocess
# import json
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Prompt for the binary path
# binary_path = input("Enter the path to the binary file: ")
#
# # Define the output file paths
# asm_file = "output4.asm"
# json_file = "output4.json"
#
# # Convert the binary to assembly code using a disassembler
# subprocess.run(["objdump", "-d", binary_path, "-M", "intel", "-o", asm_file])
#
# # Read the assembly code file
# with open(asm_file, "r") as f:
#     # Track the node index and the current instruction address
#     node_index = 0
#     current_address = None
#
#     # Process each line in the assembly code
#     for line in f:
#         # Parse the assembly instruction
#         parts = line.strip().split('\t')
#         if len(parts) >= 2:
#             address = int(parts[0], 16)
#             opcode = parts[1]
#
#             # Disassemble the opcode to get mnemonic and operands
#             instructions = md.disasm(bytes.fromhex(opcode), address)
#             for insn in instructions:
#                 mnemonic = insn.mnemonic
#                 operands = insn.op_str
#
#                 # Add the instruction to the node_dict with the node label
#                 node_label = str(insn.size)
#                 data["node_dict"][node_index] = {
#                     "node_name": f"main+0x{insn.address:02x}",
#                     "node_label": node_label,
#                     "insns": [[insn.address, mnemonic, operands]]
#                 }
#
#                 # Add an edge to the previous instruction
#                 if current_address is not None:
#                     data["edge_list"].append((current_address, node_index))
#
#                 # Update the current instruction address and increment the node index
#                 current_address = node_index
#                 node_index += 1
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
# # Write the JSON output to a file
# with open(json_file, "w") as f:
#     json.dump(data, f, indent=4)
#
# print(f"JSON output generated: {json_file}")


# import subprocess
# import json
# import hashlib
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Prompt for the binary path
# binary_path = input("Enter the path to the binary file: ")
#
# # Generate a unique start point based on the binary file's hash
# with open(binary_path, "rb") as f:
#     binary_data = f.read()
#     hash_object = hashlib.md5(binary_data)
#     hash_value = hash_object.hexdigest()
#     data["startpoint"] = int(hash_value, 16)
#
# # Define the output file paths
# asm_file = "output5.asm"
# json_file = "output5.json"
#
# # Convert the binary to assembly code using a disassembler
# subprocess.run(["objdump", "-d", binary_path, "-M", "intel"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
# output = subprocess.check_output(["objdump", "-d", binary_path, "-M", "intel"])
#
# # Write the assembly code to a file
# with open(asm_file, "w") as f:
#     f.write(output.decode())
#
# # Read the assembly code file
# with open(asm_file, "r") as f:
#     # Track the node index and the current instruction address
#     node_index = data["startpoint"]
#     current_address = None
#
#     # Process each line in the assembly code
#     for line in f:
#         # Parse the assembly instruction
#         parts = line.strip().split('\t')
#         if len(parts) >= 2:
#             address = int(parts[0], 16)
#             opcode = parts[1]
#
#             # Disassemble the opcode to get mnemonic and operands
#             instructions = md.disasm(bytes.fromhex(opcode), address)
#             for insn in instructions:
#                 mnemonic = insn.mnemonic
#                 operands = insn.op_str
#
#                 # Add the instruction to the node_dict with the node label
#                 node_label = str(insn.size)
#                 data["node_dict"][node_index] = {
#                     "node_name": f"main+0x{insn.address:02x}",
#                     "node_label": node_label,
#                     "insns": [[insn.address, mnemonic, operands]]
#                 }
#
#                 # Add an edge to the previous instruction
#                 if current_address is not None:
#                     data["edge_list"].append((current_address, node_index))
#
#                 # Update the current instruction address and increment the node index
#                 current_address = node_index
#                 node_index += 1
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
# # Write the JSON output to a file
# with open(json_file, "w") as f:
#     json.dump(data, f, indent=4)
#
# print(f"JSON output generated: {json_file}")














# import json
# import hashlib
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Prompt for the binary path
# binary_path = input("Enter the path to the binary file: ")
#
# # Generate a unique start point based on the binary file's hash
# with open(binary_path, "rb") as f:
#     binary_data = f.read()
#     hash_object = hashlib.md5(binary_data)
#     hash_value = hash_object.hexdigest()
#     data["startpoint"] = int(hash_value, 16)
#
# # Disassemble the binary code and collect asm
# instructions = md.disasm(binary_data, 0)
# asm = []
# for insn in instructions:
#     asm.append((insn.address, insn.mnemonic, insn.op_str))
#
# # Track the node index and the current instruction address
# node_index = data["startpoint"]
# current_address = None
#
# # Process each instruction
# for address, mnemonic, operands in asm:
#     # Add the instruction to the node_dict with the node label
#     node_label = str(len(asm))
#     data["node_dict"][node_index] = {
#         "node_name": f"main+0x{address:02x}",
#         "node_label": node_label,
#         "insns": [[address, mnemonic, operands]]
#     }
#
#     # Add an edge to the previous instruction
#     if current_address is not None:
#         data["edge_list"].append((current_address, node_index))
#
#     # Update the current instruction address and increment the node index
#     current_address = node_index
#     node_index += 1
#
# # Set the endpoint as the last node index
# endpoint = current_address
# data["endpoints"].append(endpoint)
#
# # Add the asm code to the data structure
# data["asm"] = asm
#
# # Write the JSON output to a file
# output_path = "output6.json"
# with open(output_path, "w") as f:
#     json.dump(data, f, indent=4)
#
# print(f"JSON output generated: {output_path}")
#
# # Save the assembly code to a separate file
# asm_file = "output6.asm"
# with open(asm_file, "w") as f:
#     for address, mnemonic, operands in asm:
#         f.write(f"{address:08x}  {mnemonic:6s} {operands}\n")
#
# print(f"Assembly code saved to: {asm_file}")






















#
#
# import json
# import hashlib
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Prompt for the binary path
# binary_path = input("Enter the path to the binary file: ")
#
# # Generate a unique start point based on the binary file's hash
# with open(binary_path, "rb") as f:
#     binary_data = f.read()
#     hash_object = hashlib.md5(binary_data)
#     hash_value = hash_object.hexdigest()
#     data["startpoint"] = int(hash_value, 16)
#
# # Disassemble the binary code and collect asm
# instructions = md.disasm(binary_data, 0)
# asm = []
# for insn in instructions:
#     asm.append((insn.address, insn.mnemonic, insn.op_str))
#
# # Track the node index and the current instruction address
# node_index = data["startpoint"]
# current_address = None
#
# # Process each instruction
# for address, mnemonic, operands in asm:
#     # Add the instruction to the node_dict with the node label
#     node_label = str(len(asm))
#     data["node_dict"][node_index] = {
#         "node_name": f"main+0x{address:02x}",
#         "node_label": node_label,
#         "insns": [[address, mnemonic, operands]]
#     }
#
#     # Add an edge to the previous instruction
#     if current_address is not None:
#         data["edge_list"].append((current_address, node_index))
#
#     # Update the current instruction address and increment the node index
#     current_address = node_index
#     node_index += 1
#
# # Set the endpoint as the last node index
# endpoint = current_address
# data["endpoints"].append(endpoint)
#
# # Write the JSON output to a file
# output_path = "output7.json"
# with open(output_path, "w") as f:
#     json.dump(data, f, indent=4)
#
# print(f"JSON output generated: {output_path}")
#
# # Save the assembly code to a separate file
# asm_file = "output7.asm"
# with open(asm_file, "w") as f:
#     for address, mnemonic, operands in asm:
#         f.write(f"{address:08x}  {mnemonic:6s} {operands}\n")
#
# print(f"Assembly code saved to: {asm_file}")

# import os
# import json
# import hashlib
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32
#
# # Define the directories for input binaries, output assembly code, and JSON files
# input_directory = "D:\\Downloads(D)\\EXE Folder"
# output_asm_directory = "D:\\Downloads(D)\\EXE Folder\\ASM_OUTPUT"
# output_json_directory = "D:\\Downloads(D)\\EXE Folder\\Output"
#
# # Create the output directories if they don't exist
# os.makedirs(output_asm_directory, exist_ok=True)
# os.makedirs(output_json_directory, exist_ok=True)
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Process each binary file in the input directory
# for filename in os.listdir(input_directory):
#     # Skip non-binary files
#     if not filename.endswith(".exe"):
#         continue
#
#     # Define the data structure for instructions, nodes, and edges
#     data = {
#         "node_dict": {},
#         "edge_list": [],
#         "label": "benign",
#         "startpoint": 0,
#         "endpoints": []
#     }
#
#     # Generate a unique start point based on the binary file's hash
#     binary_path = os.path.join(input_directory, filename)
#     with open(binary_path, "rb") as f:
#         binary_data = f.read()
#         hash_object = hashlib.md5(binary_data)
#         hash_value = hash_object.hexdigest()
#         data["startpoint"] = int(hash_value, 16)
#
#     # Disassemble the binary code and collect asm
#     instructions = md.disasm(binary_data, 0)
#     asm = []
#     for insn in instructions:
#         asm.append((insn.address, insn.mnemonic, insn.op_str))
#
#     # Track the node index and the current instruction address
#     node_index = data["startpoint"]
#     current_address = None
#
#     # Process each instruction
#     for address, mnemonic, operands in asm:
#         # Add the instruction to the node_dict with the node label
#         node_label = str(len(asm))
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, operands]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
#     # Write the JSON output to a file
#     output_json_path = os.path.join(output_json_directory, f"{os.path.splitext(filename)[0]}.json")
#     with open(output_json_path, "w") as f:
#         json.dump(data, f, indent=4)
#
#     print(f"JSON output generated: {output_json_path}")
#
#     # Save the assembly code to a separate file
#     output_asm_path = os.path.join(output_asm_directory, f"{os.path.splitext(filename)[0]}.asm")
#     with open(output_asm_path, "w") as f:
#         for address, mnemonic, operands in asm:
#             f.write(f"{address:08x}  {mnemonic:6s} {operands}\n")
#
#     print(f"Assembly code saved to: {output_asm_path}")


# import json
# import hashlib
# from capstone import Cs, CS_ARCH_X86, CS_MODE_32, CS_GRP_JUMP, CS_GRP_CALL
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Initialize the disassembler
# md = Cs(CS_ARCH_X86, CS_MODE_32)
#
# # Prompt for the binary directory and output directory
# binary_directory = input("Enter the path to the directory containing binary files: ")
# output_directory = input("Enter the path to the output directory: ")
#
# # Process each binary file in the directory
# import os
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     # Generate a unique start point based on the binary file's hash
#     with open(binary_path, "rb") as f:
#         binary_data = f.read()
#         hash_object = hashlib.md5(binary_data)
#         hash_value = hash_object.hexdigest()
#         start_point = int(hash_value, 16)
#
#     # Disassemble the binary code and collect asm
#     instructions = list(md.disasm(binary_data, start_point))
#     asm = [(insn.address, insn.mnemonic, insn.op_str) for insn in instructions]
#
#     # Track the node index and the current instruction address
#     node_index = start_point
#     current_address = None
#
#     # Process each instruction
#     for address, mnemonic, operands in asm:
#         # Add the instruction to the node_dict with the node label
#         node_label = str(len(asm))
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, operands]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#         # Check if the instruction is a control flow instruction
#         groups = md.insn_group_ids(insn)
#         if any(group in (CS_GRP_JUMP, CS_GRP_CALL) for group in groups):
#             # Resolve the branch target and add an edge to the target address
#             branch_target = int(operands, 0)  # Assuming the branch target is a direct address
#             data["edge_list"].append((current_address, branch_target))
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
#     # Write the JSON output to a file
#     output_json = os.path.join(output_directory, f"{filename}.json")
#     with open(output_json, "w") as f:
#         json.dump(data, f, indent=4)
#
#     # Save the assembly code to a separate file
#     output_asm = os.path.join(output_directory, f"{filename}.asm")
#     with open(output_asm, "w") as f:
#         for address, mnemonic, operands in asm:
#             f.write(f"{address:08x}  {mnemonic:6s} {operands}\n")
#
#     print(f"Output generated for: {filename}")
#
# print("All binary files processed.")






#
# import hashlib
# import json
# import os
# import r2pipe
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Prompt for the binary directory and output directory
# binary_directory = input("Enter the path to the directory containing binary files: ")
# output_directory = input("Enter the path to the output directory: ")
#
# # Process each binary file in the directory
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     # Generate a unique start point based on the binary file's hash
#     with open(binary_path, "rb") as f:
#         binary_data = f.read()
#         hash_object = hashlib.md5(binary_data)
#         hash_value = hash_object.hexdigest()
#         start_point = int(hash_value, 16)
#
#     # Initialize radare2
#     r2 = r2pipe.open(binary_path)
#
#     # Disassemble the binary code and collect asm
#     asm = r2.cmdj("pdj 99999")  # Disassemble maximum 99999 instructions
#
#     # Track the node index and the current instruction address
#     node_index = start_point
#     current_address = None
#
#     # Process each instruction
#     for insn in asm:
#         address = int(insn["offset"], 16)
#         mnemonic = insn["opcode"]
#         operands = insn["opcode"]
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(len(asm))
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, operands]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#         # Check if the instruction is a control flow instruction
#         if insn["type"] in ("call", "jmp"):
#             # Resolve the branch target and add an edge to the target address
#             branch_target = int(insn["jump"], 16)
#             data["edge_list"].append((current_address, branch_target))
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
#     # Write the JSON output to a file
#     output_json = os.path.join(output_directory, f"{filename}.json")
#     with open(output_json, "w") as f:
#         json.dump(data, f, indent=4)
#
#     # Save the assembly code to a separate file
#     output_asm = os.path.join(output_directory, f"{filename}.asm")
#     with open(output_asm, "w") as f:
#         for address, mnemonic, operands in asm:
#             f.write(f"{address:08x}  {mnemonic:6s} {operands}\n")
#
#     print(f"Output generated for: {filename}")
#
# print("All binary files processed.")
















# import hashlib
# import json
# import os
# import r2pipe
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Prompt for the binary directory and output directory
# binary_directory = input("Enter the path to the directory containing binary files: ")
# output_directory = input("Enter the path to the output directory: ")
#
# # Process each binary file in the directory
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     # Generate a unique start point based on the binary file's hash
#     with open(binary_path, "rb") as f:
#         binary_data = f.read()
#         hash_object = hashlib.md5(binary_data)
#         hash_value = hash_object.hexdigest()
#         start_point = int(hash_value, 16)
#
#     # Initialize radare2
#     r2 = r2pipe.open(binary_path)
#
#     # Disassemble the binary code and collect asm
#     asm = r2.cmdj("pdj 299999")  # Disassemble maximum 299999 instructions
#
#     # Track the node index and the current instruction address
#     node_index = start_point
#     current_address = None
#
#     # Process each instruction
#     for insn in asm:
#         address = insn["offset"]
#         mnemonic = insn["opcode"]
#         operands = insn["opcode"]
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(len(asm))
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, operands]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#         # Check if the instruction is a control flow instruction
#         if insn["type"] in ("call", "jmp"):
#             # Resolve the branch target and add an edge to the target address
#             branch_target = insn["jump"]
#             data["edge_list"].append((current_address, branch_target))
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
#     # Write the JSON output to a file
#     output_json = os.path.join(output_directory, f"{filename}.json")
#     with open(output_json, "w") as f:
#         json.dump(data, f, indent=4)
#
#     # Save the assembly code to a separate file
#     output_asm = os.path.join(output_directory, f"{filename}.asm")
#     with open(output_asm, "w") as f:
#         for insn in asm:
#             address = insn["offset"]
#             mnemonic = insn["opcode"]
#             operands = insn["opcode"]
#             f.write(f"{address:08x}  {mnemonic:6s} {operands}\n")
#
#     print(f"Output generated for: {filename}")
#
# print("All binary files processed.")















#
#
# #working
# #
#
# import hashlib
# import json
# import os
# import r2pipe
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Prompt for the binary directory and output directory
# binary_directory = "D:\\Downloads(D)\EXE Folder"
# output_directory = "D:\\Downloads(D)\\EXE Folder\\Output1"
#
# # Process each binary file in the directory
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     # Generate a unique start point based on the binary file's hash
#     with open(binary_path, "rb") as f:
#         binary_data = f.read()
#         hash_object = hashlib.md5(binary_data)
#         hash_value = hash_object.hexdigest()
#         start_point = int(hash_value, 16)
#
#     # Initialize radare2
#     r2 = r2pipe.open(binary_path)
#
#     # Disassemble the binary code and collect asm
#     asm = r2.cmdj("pdj 99999")  # Disassemble maximum 99999 instructions
#
#     # Track the node index and the current instruction address
#     node_index = start_point
#     current_address = None
#
#     # Process each instruction
#     for insn in asm:
#         address = insn.get("offset", insn.get("addr"))
#         mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#         bytes_str = insn.get("bytes", "")
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(len(asm))
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, bytes_str]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#         # Check if the instruction is a control flow instruction
#         if insn.get("type") in ("call", "jmp"):
#             # Resolve the branch target and add an edge to the target address
#             branch_target = insn.get("jump")
#             data["edge_list"].append((current_address, branch_target))
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
#     # Write the JSON output to a file
#     output_json = os.path.join(output_directory, f"{filename}.json")
#     with open(output_json, "w") as f:
#         json.dump(data, f, indent=4)
#
#     # Save the assembly code to a separate file
#     output_asm = os.path.join(output_directory, f"{filename}.asm")
#     with open(output_asm, "w") as f:
#         for insn in asm:
#             address = insn.get("offset", insn.get("addr", ""))
#             mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#             bytes_str = insn.get("bytes", "")
#             f.write(f"{address:08x}  {mnemonic:6s} {bytes_str}\n")
#
#     print(f"Output generated for: {filename}")
#
# print("All binary files processed.")







#
#
#
#
# import hashlib
# import json
# import os
# import r2pipe
#
# # Prompt for the binary directory and output directory
# binary_directory = "D:\\Downloads(D)\\EXE Folder"
# output_directory = "D:\\Downloads(D)\\EXE Folder\\Output1"
#
# # Process each binary file in the directory
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     # Generate a unique start point based on the binary file's hash
#     with open(binary_path, "rb") as f:
#         binary_data = f.read()
#         hash_object = hashlib.md5(binary_data)
#         hash_value = hash_object.hexdigest()
#         start_point = int(hash_value, 16)
#
#     # Initialize radare2
#     radare2_executable = "C:\\Program Files\\radare2\\radare2-5.8.8-w64\\bin\\radare2.exe"
#     r2 = r2pipe.open(radare2_executable + " " + binary_path)
#
#     # Define the data structure for instructions, nodes, and edges
#     data = {
#         "node_dict": {},
#         "edge_list": [],
#         "label": "malware",
#         "startpoint": start_point,
#         "endpoints": []
#     }
#
#     # Disassemble the binary code and collect asm
#     asm = r2.cmdj("pdj 99999")  # Disassemble maximum 99999 instructions
#
#     # Track the node index and the current instruction address
#     node_index = start_point
#     current_address = None
#
#     # Process each instruction
#     for insn in asm:
#         address = insn.get("offset", insn.get("addr"))
#         mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#         bytes_str = insn.get("bytes", "")
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(len(asm))
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, bytes_str]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#         # Check if the instruction is a control flow instruction
#         if insn.get("type") in ("call", "jmp"):
#             # Resolve the branch target and add an edge to the target address
#             branch_target = insn.get("jump")
#             data["edge_list"].append((current_address, branch_target))
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
#     # Write the JSON output to a file
#     output_json = os.path.join(output_directory, f"{filename}.json")
#     with open(output_json, "w") as f:
#         json.dump(data, f, indent=4)
#
#     # Save the assembly code to a separate file
#     output_asm = os.path.join(output_directory, f"{filename}.asm")
#     with open(output_asm, "w") as f:
#         for insn in asm:
#             address = insn.get("offset", insn.get("addr", ""))
#             mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#             bytes_str = insn.get("bytes", "")
#             f.write(f"{address:08x}  {mnemonic:6s} {bytes_str}\n")
#
#     print(f"Output generated for: {filename}")
#
# print("All binary files processed.")


# import hashlib
# import json
# import os
# import shutil
# import subprocess
# import sys
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Prompt for the binary directory and output directory
# binary_directory = input("Enter the path to the directory containing binary files: ")
# output_directory = input("Enter the path to the output directory: ")
#
# # Ensure the output directory exists, create it if necessary
# os.makedirs(output_directory, exist_ok=True)
#
# # Process each binary file in the directory
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     # Generate a unique start point based on the binary file's hash
#     with open(binary_path, "rb") as f:
#         binary_data = f.read()
#         hash_object = hashlib.md5(binary_data)
#         hash_value = hash_object.hexdigest()
#         start_point = int(hash_value, 16)
#
#     # Use radare2 to disassemble the binary code and collect asm
#     radare2_path = "C:\\Program Files\\radare2\\radare2-5.8.8-w64\\bin\\radare2.exe"
#     command = [radare2_path, "-A", "-a", "x86", "-q", "-i", sys.executable, "-"]
#     radare_input = f"\"aa;pdfj @ {binary_path}\""
#     radare_output = subprocess.check_output(command, input=radare_input, universal_newlines=True)
#
#     # Parse radare2 output to extract asm instructions
#     asm = []
#     try:
#         json_output = json.loads(radare_output)
#         for function in json_output["functions"]:
#             for block in function["blocks"]:
#                 for insn in block["disasm"]:
#                     address = insn["offset"]
#                     mnemonic = insn["opcode"].split()[0]
#                     bytes_str = insn["bytes"]
#                     asm.append({"address": address, "mnemonic": mnemonic, "bytes": bytes_str})
#     except (json.JSONDecodeError, KeyError):
#         print(f"Cannot parse radare2 output for '{binary_path}'")
#         continue
#
#     # Track the node index and the current instruction address
#     node_index = start_point
#     current_address = None
#
#     # Process each instruction
#     for insn in asm:
#         address = insn["address"]
#         mnemonic = insn["mnemonic"]
#         bytes_str = insn["bytes"]
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(len(asm))
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, bytes_str]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#         # Check if the instruction is a control flow instruction
#         if mnemonic in ("call", "jmp"):
#             # Resolve the branch target and add an edge to the target address
#             branch_target = int(bytes_str, 16)
#             data["edge_list"].append((current_address, branch_target))
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
#     # Write the JSON output to a file
#     output_json = os.path.join(output_directory, f"{filename}.json")
#     with open(output_json, "w") as f:
#         json.dump(data, f, indent=4)
#
#     # Save the assembly code to a separate file
#     output_asm = os.path.join(output_directory, f"{filename}.asm")
#     with open(output_asm, "w") as f:
#         for insn in asm:
#             address = insn["address"]
#             mnemonic = insn["mnemonic"]
#             bytes_str = insn["bytes"]
#             f.write(f"{address:08x}  {mnemonic:6s} {bytes_str}\n")
#
#     print(f"Output generated for: {filename}")
#
# print("All binary files processed.")




#
# %More accurate


#
#
# import hashlib
# import json
# import os
# import r2pipe
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Prompt for the binary directory and output directory
# binary_directory = "D:\\Downloads(D)\\EXE Folder"
# output_directory = "D:\\Downloads(D)\\EXE Folder\\Output1"
#
# # Process each binary file in the directory
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     # Generate a unique start point based on the binary file's hash
#     with open(binary_path, "rb") as f:
#         binary_data = f.read()
#         hash_object = hashlib.md5(binary_data)
#         hash_value = hash_object.hexdigest()
#         start_point = int(hash_value, 16)
#
#     # Initialize radare2
#     r2 = r2pipe.open(binary_path)
#
#     # Disassemble the binary code and collect asm
#     asm = r2.cmdj("pdj 99999")  # Disassemble maximum 99999 instructions
#
#     # Track the node index and the current instruction address
#     node_index = start_point
#     current_address = None
#
#     # Process each instruction
#     for insn in asm:
#         address = insn.get("offset", insn.get("addr"))
#         mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#         bytes_str = insn.get("bytes", "")
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(len(asm))
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, bytes_str]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#         # Check if the instruction is a control flow instruction
#         if insn.get("type") in ("call", "jmp"):
#             # Resolve the branch target and add an edge to the target address
#             branch_target = insn.get("jump")
#             data["edge_list"].append((current_address, branch_target))
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
#     # Write the JSON output to a file
#     output_json = os.path.join(output_directory, f"{filename}.json")
#     with open(output_json, "w") as f:
#         json.dump(data, f, indent=4)
#
#     # Save the assembly code to a separate file
#     output_asm = os.path.join(output_directory, f"{filename}.asm")
#     with open(output_asm, "w") as f:
#         for insn in asm:
#             address = insn.get("offset", insn.get("addr", ""))
#             mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#             bytes_str = insn.get("bytes", "")
#             f.write(f"{address:08x}  {mnemonic:6s} {bytes_str}\n")
#
#     print(f"Output generated for: {filename}")
#
# print("All binary files processed.")
#
#






# import hashlib
# import json
# import os
# import r2pipe
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Prompt for the binary directory and output directory
# binary_directory = "D:\\Downloads(D)\\Testing1\\EXE Files"
# output_directory = "D:\\Downloads(D)\\Testing1\\EXE Files"
#
# # Process each binary file in the directory
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     # Generate a unique start point based on the binary file's hash
#     with open(binary_path, "rb") as f:
#         binary_data = f.read()
#         hash_object = hashlib.md5(binary_data)
#         hash_value = hash_object.hexdigest()
#         start_point = int(hash_value, 16)
#
#     # Initialize radare2
#     try:
#         r2 = r2pipe.open(binary_path)
#     except Exception as e:
#         print(f"Error opening file: {filename}")
#         print(e)
#         continue
#
#     # Disassemble the binary code and collect asm
#     asm = r2.cmdj("pdj 99999")  # Disassemble maximum 99999 instructions
#
#     # Track the node index and the current instruction address
#     node_index = start_point
#     current_address = None
#
#     # Process each instruction
#     for insn in asm:
#         address = insn.get("offset", insn.get("addr"))
#         mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#         bytes_str = insn.get("bytes", "")
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(len(asm))
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, bytes_str]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#         # Check if the instruction is a control flow instruction
#         if insn.get("type") in ("call", "jmp"):
#             # Resolve the branch target and add an edge to the target address
#             branch_target = insn.get("jump")
#             data["edge_list"].append((current_address, branch_target))
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
#     # Write the JSON output to a file
#     output_json = os.path.join(output_directory, f"{filename}.json")
#     with open(output_json, "w") as f:
#         json.dump(data, f, indent=4)
#
#     # Save the assembly code to a separate file
#     output_asm = os.path.join(output_directory, f"{filename}.asm")
#     with open(output_asm, "w") as f:
#         for insn in asm:
#             address = insn.get("offset", insn.get("addr", ""))
#             mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#             bytes_str = insn.get("bytes", "")
#             f.write(f"{address:08x}  {mnemonic:6s} {bytes_str}\n")
#
#     print(f"Output generated for: {filename}")
#
# print("All binary files processed.")


# import hashlib
# import json
# import os
# import r2pipe
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Prompt for the binary directory and output directory
# binary_directory = "D:\\Downloads(D)\\Testing1\\EXE Files"
# output_directory = "D:\\Downloads(D)\\Testing1\\EXE Files"
#
# # Process each binary file in the directory
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     try:
#         # Generate a unique start point based on the binary file's hash
#         with open(binary_path, "rb") as f:
#             binary_data = f.read()
#             hash_object = hashlib.md5(binary_data)
#             hash_value = hash_object.hexdigest()
#             start_point = int(hash_value, 16)
#
#         # Initialize radare2
#         r2 = r2pipe.open(binary_path)
#
#         # Disassemble the binary code and collect asm
#         asm = r2.cmdj("pdj 99999")  # Disassemble maximum 99999 instructions
#
#         # Track the node index and the current instruction address
#         node_index = start_point
#         current_address = None
#
#         # Process each instruction
#         for insn in asm:
#             address = insn.get("offset", insn.get("addr"))
#             mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#             bytes_str = insn.get("bytes", "")
#
#             # Add the instruction to the node_dict with the node label
#             node_label = str(len(asm))
#             data["node_dict"][node_index] = {
#                 "node_name": f"main+0x{address:02x}",
#                 "node_label": node_label,
#                 "insns": [[address, mnemonic, bytes_str]]
#             }
#
#             # Add an edge to the previous instruction
#             if current_address is not None:
#                 data["edge_list"].append((current_address, node_index))
#
#             # Update the current instruction address and increment the node index
#             current_address = node_index
#             node_index += 1
#
#             # Check if the instruction is a control flow instruction
#             if insn.get("type") in ("call", "jmp"):
#                 # Resolve the branch target and add an edge to the target address
#                 branch_target = insn.get("jump")
#                 data["edge_list"].append((current_address, branch_target))
#
#         # Set the endpoint as the last node index
#         endpoint = current_address
#         data["endpoints"].append(endpoint)
#
#         # Write the JSON output to a file
#         output_json = os.path.join(output_directory, f"{filename}.json")
#         with open(output_json, "w") as f:
#             json.dump(data, f, indent=4)
#
#         # Save the assembly code to a separate file
#         output_asm = os.path.join(output_directory, f"{filename}.asm")
#         with open(output_asm, "w") as f:
#             for insn in asm:
#                 address = insn.get("offset", insn.get("addr", ""))
#                 mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#                 bytes_str = insn.get("bytes", "")
#                 f.write(f"{address:08x}  {mnemonic:6s} {bytes_str}\n")
#
#         print(f"Output generated for: {filename}")
#
#     except Exception as e:
#         print(f"Error processing file: {filename}")
#         print(f"Error message: {str(e)}")
#
# print("All binary files processed.")


# import hashlib
# import json
# import os
# import idaapi
# import idc
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Prompt for the binary directory and output directory
# binary_directory = "D:\\Downloads(D)\\EXE Folder"
# output_directory = "D:\\Downloads(D)\\EXE Folder\\Output1"
#
# # Process each binary file in the directory
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     try:
#         # Generate a unique start point based on the binary file's hash
#         with open(binary_path, "rb") as f:
#             binary_data = f.read()
#             hash_object = hashlib.md5(binary_data)
#             hash_value = hash_object.hexdigest()
#             start_point = int(hash_value, 16)
#
#         # Load the binary file in IDA Pro
#         idaapi.auto_wait()
#         idc.LoadFile(binary_path)
#
#         # Disassemble the binary code and collect asm
#         start_address = idc.MinEA()
#         end_address = idc.MaxEA()
#         asm = []
#
#         for address in range(start_address, end_address):
#             if idc.isCode(idc.GetFlags(address)):
#                 mnemonic = idc.GetMnem(address)
#                 operands = idc.GetOpnd(address, 0)
#                 asm.append((address, mnemonic, operands))
#
#         # Track the node index and the current instruction address
#         node_index = start_point
#         current_address = None
#
#         # Process each instruction
#         for address, mnemonic, operands in asm:
#             # Add the instruction to the node_dict with the node label
#             node_label = str(len(asm))
#             data["node_dict"][node_index] = {
#                 "node_name": f"main+0x{address:02x}",
#                 "node_label": node_label,
#                 "insns": [[address, mnemonic, operands]]
#             }
#
#             # Add an edge to the previous instruction
#             if current_address is not None:
#                 data["edge_list"].append((current_address, node_index))
#
#             # Update the current instruction address and increment the node index
#             current_address = node_index
#             node_index += 1
#
#             # Check if the instruction is a control flow instruction
#             if idc.isFlow(idc.GetFlags(address)):
#                 # Get the branch target and add an edge to the target address
#                 branch_target = idc.GetOperandValue(address, 0)
#                 data["edge_list"].append((current_address, branch_target))
#
#         # Set the endpoint as the last node index
#         endpoint = current_address
#         data["endpoints"].append(endpoint)
#
#         # Write the JSON output to a file
#         output_json = os.path.join(output_directory, f"{filename}.json")
#         with open(output_json, "w") as f:
#             json.dump(data, f, indent=4)
#
#         # Save the assembly code to a separate file
#         output_asm = os.path.join(output_directory, f"{filename}.asm")
#         with open(output_asm, "w") as f:
#             for address, mnemonic, operands in asm:
#                 f.write(f"{address:08x}  {mnemonic:6s} {operands}\n")
#
#         print(f"Output generated for: {filename}")
#
#     except Exception as e:
#         print(f"Error processing file: {filename}")
#         print(f"Error message: {str(e)}")
#
# print("All binary files processed.")


#
# import hashlib
# import json
# import os
# import r2pipe
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Prompt for the binary directory and output directory
# binary_directory = "D:\\Downloads(D)\\EXE Folder"
# output_directory = "D:\\Downloads(D)\\EXE Folder\\Output1"
#
# # Process each binary file in the directory
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     # Generate a unique start point based on the binary file's hash
#     with open(binary_path, "rb") as f:
#         binary_data = f.read()
#         hash_object = hashlib.md5(binary_data)
#         hash_value = hash_object.hexdigest()
#         start_point = int(hash_value, 16)
#
#     # Initialize radare2
#     # r2_path = r"D:\Downloads(D)\radare2\radare2-5.8.8-w64\bin\r2.bat"  # Replace with the correct path to the r2.bat file
#     # r2 = r2pipe.open(r2_path + " " + binary_path)
#     r2 = r2pipe.open(binary_path)
#
#     # Disassemble the binary code and collect asm
#     asm = r2.cmdj("pdj 99999")  # Disassemble maximum 99999 instructions
#
#     # Track the node index and the current instruction address
#     node_index = start_point
#     current_address = None
#
#     # Process each instruction
#     for insn in asm:
#         address = insn.get("offset", insn.get("addr"))
#         mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#         bytes_str = insn.get("bytes", "")
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(len(asm))
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, bytes_str]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#         # Check if the instruction is a control flow instruction
#         if insn.get("type") in ("call", "jmp"):
#             # Resolve the branch target and add an edge to the target address
#             branch_target = insn.get("jump")
#             data["edge_list"].append((current_address, branch_target))
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
#     # Write the JSON output to a file
#     output_json = os.path.join(output_directory, f"{filename}.json")
#     with open(output_json, "w") as f:
#         json.dump(data, f, indent=4)
#
#     # Save the assembly code to a separate file
#     output_asm = os.path.join(output_directory, f"{filename}.asm")
#     with open(output_asm, "w") as f:
#         for insn in asm:
#             address = insn.get("offset", insn.get("addr", ""))
#             mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#             bytes_str = insn.get("bytes", "")
#             f.write(f"{address:08x}  {mnemonic:6s} {bytes_str}\n")
#
#     print(f"Output generated for: {filename}")
#
# print("All binary files processed.")
# #


# import hashlib
# import json
# import os
# import r2pipe
#
# # Define the data structure for instructions, nodes, and edges
# data = {
#     "node_dict": {},
#     "edge_list": [],
#     "label": "malware",
#     "startpoint": 0,
#     "endpoints": []
# }
#
# # Prompt for the binary directory and output directory
# binary_directory = "D:\\Downloads(D)\\EXE Folder"
# output_directory = "D:\\Downloads(D)\\EXE Folder\\Output1"
#
# # Process each binary file in the directory
# for filename in os.listdir(binary_directory):
#     binary_path = os.path.join(binary_directory, filename)
#
#     # Generate a unique start point based on the binary file's hash
#     with open(binary_path, "rb") as f:
#         binary_data = f.read()
#         hash_object = hashlib.md5(binary_data)
#         hash_value = hash_object.hexdigest()
#         start_point = int(hash_value, 16)
#
#     # Initialize radare2
#     r2 = r2pipe.open(binary_path)
#
#     # Disassemble the binary code and collect asm
#     try:
#         asm = r2.cmdj("pdj 99999")  # Disassemble maximum 99999 instructions
#     except r2pipe.cmdj.Error as e:
#         print(f"Error disassembling {filename}: {str(e)}")
#         continue
#
#     if asm is None:
#         print(f"Error disassembling {filename}: Empty disassembly")
#         continue
#
#     # Track the node index and the current instruction address
#     node_index = start_point
#     current_address = None
#
#     # Process each instruction
#     for insn in asm:
#         address = insn.get("offset", insn.get("addr"))
#         mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#         bytes_str = insn.get("bytes", "")
#
#         # Add the instruction to the node_dict with the node label
#         node_label = str(len(asm))
#         data["node_dict"][node_index] = {
#             "node_name": f"main+0x{address:02x}",
#             "node_label": node_label,
#             "insns": [[address, mnemonic, bytes_str]]
#         }
#
#         # Add an edge to the previous instruction
#         if current_address is not None:
#             data["edge_list"].append((current_address, node_index))
#
#         # Update the current instruction address and increment the node index
#         current_address = node_index
#         node_index += 1
#
#         # Check if the instruction is a control flow instruction
#         if insn.get("type") in ("call", "jmp"):
#             # Resolve the branch target and add an edge to the target address
#             branch_target = insn.get("jump")
#             data["edge_list"].append((current_address, branch_target))
#
#     # Set the endpoint as the last node index
#     endpoint = current_address
#     data["endpoints"].append(endpoint)
#
#     # Write the JSON output to a file
#     output_json = os.path.join(output_directory, f"{filename}.json")
#     with open(output_json, "w") as f:
#         json.dump(data, f, indent=4)
#
#     # Save the assembly code to a separate file
#     output_asm = os.path.join(output_directory, f"{filename}.asm")
#     with open(output_asm, "w") as f:
#         for insn in asm:
#             address = insn.get("offset", insn.get("addr", ""))
#             mnemonic = insn.get("mnemonic", insn.get("opcode", ""))
#             bytes_str = insn.get("bytes", "")
#             f.write(f"{address:08x}  {mnemonic:6s} {bytes_str}\n")
#
#     print(f"Output generated for: {filename}")
#
# print("All binary files processed.")


import os
import sys
import lib2to3.main


def update_files_to_python3(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                backup_path = file_path + ".bak"  # Create a backup of the original file
                try:
                    # Create a backup of the original file
                    os.rename(file_path, backup_path)

                    # Run 2to3 tool to convert the file
                    sys.argv = ["", "-n", "-W", "-o", root, backup_path]
                    lib2to3.main.main()

                    # Remove the backup file
                    os.remove(backup_path)

                    print(f"Updated: {file_path}")
                except Exception as e:
                    print(f"Error updating {file_path}: {str(e)}")


# Example usage
directory_path = "D:\\Downloads(D)\\ItwillWork_IA\\raw-feature-extractor"  # Replace with the path to your directory
update_files_to_python3(directory_path)
