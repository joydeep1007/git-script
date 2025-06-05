import random
from datetime import datetime

def get_quotes():
    with open('quotes.md', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract quotes from the Quote History section
    history_section = content.split('## Quote History')[1].strip()
    quotes = [q.strip() for q in history_section.split('\n-') if q.strip()]
    return quotes

def update_quote_file(new_quote):
    with open('quotes.md', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content at the Today's Quote section
    parts = content.split("Today's Quote:")
    header = parts[0]
    rest = parts[1].split('## Quote History')[1]
    
    # Create new content with updated quote
    new_content = f"{header}Today's Quote:\n> {new_quote}\n\n## Quote History{rest}"
    
    with open('quotes.md', 'w', encoding='utf-8') as file:
        file.write(new_content)

def main():
    quotes = get_quotes()
    today_quote = random.choice(quotes)
    update_quote_file(today_quote)

if __name__ == "__main__":
    main()
