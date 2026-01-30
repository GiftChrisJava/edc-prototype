
import os
import re

base_dir = r'c:\Users\giftz\OneDrive\Desktop\Tasks\Web\edc-one'

def update_services():
    path = os.path.join(base_dir, 'services.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix invisible text in white card (inside red section)
    # text-text-main -> text-slate-900
    # text-text-muted -> text-slate-500
    new_content = content.replace('text-text-main', 'text-slate-900')
    new_content = new_content.replace('text-text-muted', 'text-slate-600')
    
    if content != new_content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated services.html contrast")

def update_team():
    path = os.path.join(base_dir, 'team.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Fix Hero Button (Blue on Blue -> White on Blue)
    # Target: bg-primary hover:bg-primary/90 text-white
    # Replacement: bg-white text-primary hover:bg-slate-100
    # Search specific button in hero
    # It has "Join the Team" text.
    
    # Regex to find the button link
    pattern = r'(<a href="contact.html"[^>]*class="[^"]*bg-primary[^"]*"[^>]*>\s*<span>Join\s+the\s+Team</span></a>)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        old_tag = match.group(1)
        # We replace bg-primary with bg-white, text-white with text-primary
        new_tag = old_tag.replace('bg-primary', 'bg-white').replace('text-white', 'text-primary').replace('hover:bg-primary/90', 'hover:bg-slate-100')
        new_content = content.replace(old_tag, new_tag)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated team.html hero button")
    else:
        print("Could not find team.html hero button to update")

def update_portfolio():
    path = os.path.join(base_dir, 'portfolio.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Make Hero Section Blue (bg-primary text-white)
    # Look for <section class="mb-16 max-w-4xl">
    # This is the hero container.
    # We want to make the BACKGROUND the full width. 
    # Currently `main` has `px-4 md:px-10 py-12`.
    # And the section is inside main.
    # To make it full width, we might need to restructure or just make the card blue?
    # Or, we can make the <header> blue? No, header is sticky.
    # Let's make the Hero text section Blue? 
    # Structure:
    # <main class="... flex flex-col">
    #   <section class="mb-16 max-w-4xl"> ... </section>
    
    # If we add class "bg-primary text-white" to the section, it will be a blue box *inside* the padding.
    # That is acceptable and professional. Or we can make it a rounded card.
    # Let's try adding `bg-primary text-white p-8 rounded-2xl` to the section.
    
    pattern = r'<section class="mb-16 max-w-4xl">'
    replacement = r'<section class="mb-16 max-w-4xl bg-primary text-white p-8 md:p-12 rounded-2xl shadow-lg">'
    
    if pattern in content:
        new_content = content.replace(pattern, replacement)
        # Also need to fix inner text colors if they are slate-900
        new_content = new_content.replace('text-slate-900', 'text-white') # Hero Title
        new_content = new_content.replace('text-slate-600', 'text-slate-200') # Hero description
        new_content = new_content.replace('<span class="text-primary">Excellence</span>', '<span class="text-accent">Excellence</span>') # Contrast fix
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated portfolio.html hero section")
    else:
        print("Could not find portfolio.html hero section")

update_services()
update_team()
update_portfolio()
