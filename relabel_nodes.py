import json

def relabel_routing_node(annotations):
    """Apply relabeling rules to routing-node based on other annotations."""
    
    # Extract relevant labels
    labels = {ann['id']: ann.get('label') for ann in annotations}
    
    function_outcome = labels.get('function_for_outcome')
    intent = labels.get('intent')
    stage = labels.get('conversation_stage')
    
    # Apply rules in order
    # Rule 1
    if function_outcome == 'establish_contact' and (stage == 'greeting' or intent == 'greeting'):
        return 'introduction'
    
    # Rule 2
    if function_outcome == 'establish_contact' and stage == 'introduction':
        return 'confirm_interest'
    
    # Rule 3
    if function_outcome == 'handle_rejection' or intent == 'closing' or intent == 'rejection':
        return 'close'
    
    # Rule 4
    if function_outcome == 'confirm_interest':
        return 'transfer_to_officer'
    
    # Rule 5 (default)
    return 'transfer_to_officer'


def process_json(data):
    """Process JSON data and relabel routing-node annotations."""
    
    for conversation in data.get('conversations', []):
        for turn in conversation.get('turns', []):
            annotations = turn.get('annotations', [])
            
            # Find routing-node annotation and update its label
            for ann in annotations:
                if ann.get('id') == 'routing-node':
                    ann['label'] = relabel_routing_node(annotations)
    
    return data


# Main execution
if __name__ == '__main__':
    # Load JSON file
    with open('/Users/kamenpavlov/Desktop/Projects/sentient-autonomics/codebase/conversation-service-landing-page/dist/data/conversations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Process and relabel
    data = process_json(data)
    
    # Save updated JSON
    with open('/Users/kamenpavlov/Desktop/Projects/sentient-autonomics/codebase/conversation-service-landing-page/dist/data/output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("Relabeling complete. Output saved to output.json")