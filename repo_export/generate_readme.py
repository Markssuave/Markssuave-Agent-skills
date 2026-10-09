import os, yaml, re

skills_dir = r'C:\Users\Mark Vasquez\Documents\Agent Skills\Markssuave-Agent-skills\skills'
readme_path = r'C:\Users\Mark Vasquez\Documents\Agent Skills\Markssuave-Agent-skills\README.md'

skills = []

for item in os.listdir(skills_dir):
    skill_path = os.path.join(skills_dir, item, 'SKILL.md')
    if os.path.isfile(skill_path):
        try:
            with open(skill_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # extract frontmatter
                match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
                if match:
                    frontmatter = yaml.safe_load(match.group(1))
                    name = frontmatter.get('name', item)
                    desc = frontmatter.get('description', 'No description provided.')
                    skills.append((name, desc, item))
                else:
                    skills.append((item, 'No description provided.', item))
        except Exception as e:
            skills.append((item, f'Error reading description: {e}', item))

skills.sort(key=lambda x: x[0])

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write('# Markssuave Agent Skills\n\n')
    f.write('A collection of 128 custom agent skills to supercharge your workflow!\n\n')
    f.write('## What are these?\n')
    f.write('These are specialized AI agent "skills" — pre-packaged sets of instructions, guidelines, and context that give AI agents specific roles, like a strict frontend designer, a rigorous backend tester, or a token-saving minimalist coder. You can install these into your own agent setup.\n\n')
    f.write('## The Skills (In Layman\'s Terms)\n\n')
    for name, desc, folder in skills:
        origin = 'Custom System Skill'
        if 'impeccable' in name.lower() or 'ui-' in name.lower():
            origin = 'Impeccable UI/UX Suite'
        elif 'caveman' in name.lower() or 'ops-optimize' in name.lower() or 'stats-' in name.lower():
            origin = 'Caveman Token Optimization Suite'
        elif 'ponytail' in name.lower() or 'dev-minimal' in name.lower() or 'review-bloat' in name.lower():
            origin = 'Ponytail Minimalist Dev Suite'
        elif 'pocock' in name.lower() or 'tdd' in name.lower() or 'qa-' in name.lower() or 'plan-' in name.lower() or 'arch-' in name.lower() or 'dev-' in name.lower():
            origin = 'Matt Pocock Engineering Suite'
        elif 'brag' in name.lower() or 'show-video' in name.lower():
            origin = 'Brag Launch Video Suite'
        elif 'plugin' in name.lower() or 'generative' in name.lower() or 'automation' in name.lower() or 'ui-extension' in name.lower() or 'agy-' in name.lower():
            origin = 'Antigravity Built-in Capabilities'
        
        desc_clean = desc.replace('\n', ' ').strip()
        f.write(f'### `{name}`\n')
        f.write(f'- **Origin:** {origin}\n')
        f.write(f'- **What it does:** {desc_clean}\n')
        f.write(f'- **Folder:** `skills/{folder}`\n\n')

print(f'Generated README with {len(skills)} skills.')
