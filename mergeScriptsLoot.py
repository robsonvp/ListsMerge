import re

def parse_input_from_file(filename):
    with open(filename, 'r') as file:
        input_str = file.read()
    
    # Regex to match the pattern of the items
    pattern = r'\{ itemName = "(.*?)", clientId = (\d+), (.*?) \},'
    matches = re.findall(pattern, input_str.strip())
    
    items = []
    for match in matches:
        item = {
            'itemName': match[0],
            'clientId': int(match[1]),
        }
        # Handle buy/sell attributes
        attributes = match[2].split(', ')
        for attr in attributes:
            key, value = attr.split(' = ')
            item[key] = int(value)
        
        items.append(item)
    
    return items

def format_output_to_file(items, filename):
    output_lines = []
    for item in items:
        attributes = ', '.join([f'{key} = {value}' for key, value in item.items() if key not in ['itemName', 'clientId']])
        line = f'{{ itemName = "{item["itemName"]}", clientId = {item["clientId"]}, {attributes} }},'
        output_lines.append(line)
    
    with open(filename, 'w') as file:
        file.write('\n'.join(output_lines))

def merge_lists(list1, list2):
    merged_list = list1 + list2
    unique_items = {item['clientId']: item for item in merged_list}.values()
    return list(unique_items)

# Read the input files and parse them into lists of dictionaries
list1 = parse_input_from_file('input1.txt')
list2 = parse_input_from_file('input2.txt')

# Merge the lists and remove duplicates
merged_list = merge_lists(list1, list2)

# Write the formatted output to a file
format_output_to_file(merged_list, 'output.txt')

print("Merging completed. The result is saved in 'output.txt'.")
