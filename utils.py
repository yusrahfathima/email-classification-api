import re

def mask_email(email_text):
    patterns = {
        'full_name': r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b',
        'email': r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+',
        'phone_number': r'\b\d{10}\b',
        'dob': r'\b\d{2}/\d{2}/\d{4}\b',
        'aadhar_num': r'\b\d{4}\s\d{4}\s\d{4}\b',
        'credit_debit_no': r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b',
        'cvv_no': r'\b\d{3}\b',
        'expiry_no': r'\b(0[1-9]|1[0-2])\/\d{2,4}\b'
    }

    masked_text = email_text
    entities = []
    offset = 0

    for ent_type, pattern in patterns.items():
        for match in re.finditer(pattern, email_text):
            entity = match.group()
            start = match.start() + offset
            end = start + len(f"[{ent_type}]")
            entities.append({
                "position": [start, end],
                "classification": ent_type,
                "entity": entity
            })
            masked_text = masked_text.replace(entity, f"[{ent_type}]")
            offset += len(f"[{ent_type}]") - len(entity)

    return masked_text, entities
